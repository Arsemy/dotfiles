#!/usr/bin/python3
# -*- coding: utf-8 -*-

# mentalcalculation - version 0.5.2
# Copyright (C) 2008-2021, solsTiCe d'Hiver <solstice.dhiver@gmail.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# In addition, as a special exception, the copyright holders give
# permission to link the code of portions of this program with the
# OpenSSL library under certain conditions as described in each
# individual source file, and distribute linked combinations
# including the two.
#
# You must obey the GNU General Public License in all respects for
# all of the code used other than OpenSSL.  If you modify file(s)
# with this exception, you may extend this exception to your version
# of the file(s), but you are not obligated to do so.  If you do not
# wish to do so, delete this exception statement from your version.
# If you delete this exception statement from all source files in the
# program, then also delete it here.
#

import sys
import pathlib
import os
import json
import urllib.request, urllib.parse, urllib.error
import certifi
import ssl
from threading import Thread

import argparse
from tempfile import mkstemp, NamedTemporaryFile
try:
    from random import SystemRandom
    IS_SYSTEMRANDOM_AVAILABLE = True
except ImportError:
    from random import randint

try:
    from PyQt5 import QtGui,QtCore,QtWidgets
except ImportError:
    print('Error: you need PyQt5 to run this software', file=sys.stderr)
    sys.exit(1)
IS_SOUND_AVAILABLE = True
try:
    from PyQt5 import QtMultimedia
except ImportError:
    IS_SOUND_AVAILABLE = False

from gui import settings, main

DIGIT = dict([(i,(int('1'+'0'*(i-1)), int('9'*i))) for i in range(1,10)])

appName = 'mentalcalculation'
appVersion = '0.5.2'

SHARE_PATH = '.'
SHARE_PATH = pathlib.Path(SHARE_PATH).absolute()
BELL = str(SHARE_PATH / 'sound/bell.mp3')
BELL_DURATION = 600
THREEBELLS = str(SHARE_PATH / 'sound/3bells.mp3')
THREEBELLS_DURATION = 1000
ANNOYING_SOUND = str(SHARE_PATH / 'sound/annoying-sound.mp3')
ANNOYING_SOUND_DURATION = 150
GOOD = str(SHARE_PATH / 'sound/good.mp3')
BAD = str(SHARE_PATH / 'sound/bad.mp3')
WELCOME = str(SHARE_PATH / 'img/soroban.png')
SMILE = str(SHARE_PATH / 'img/face-smile.png')
SAD = str(SHARE_PATH / 'img/face-sad.png')
RESTART = str(SHARE_PATH / 'img/restart.png')

APIURL = 'https://www.sorobanexam.org/tools/tts'
#APIURL = 'http://localhost:8080/tools/tts'
# Google TTS API available voice languages (hard coded). See f'{APIURL}?lang_list=1' for a current version
LANG_LIST = [
    "af-ZA", "ar-XA", "bg-BG", "bn-IN", "ca-ES", "cmn-CN", "cmn-TW", "cs-CZ", "da-DK", "de-DE",
    "el-GR", "en-AU", "en-GB", "en-IN", "en-US", "es-ES", "es-US", "fi-FI", "fil-PH", "fr-CA", "fr-FR",
    "gu-IN", "hi-IN", "hu-HU", "id-ID", "is-IS", "it-IT", "ja-JP", "kn-IN", "ko-KR", "lv-LV", "ml-IN",
    "nb-NO", "nl-NL", "pl-PL", "pt-BR", "pt-PT", "ro-RO", "ru-RU", "sk-SK", "sr-RS", "sv-SE", "ta-IN",
    "te-IN", "th-TH", "tr-TR", "uk-UA", "vi-VN", "yue-HK"
]
LANG = 'en'

nb_dleds = 0 # global variable to hold number of downloaded sounds: TODO: do it better ?

ssl_context = ssl.create_default_context(cafile=certifi.where())

class Settings(QtWidgets.QDialog):
    def __init__(self, mysettings, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = settings.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText(self.tr('Ok'))
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText(self.tr('Cancel'))
        self.importSettings(mysettings)
        self.ui.sb_flash.setEnabled(not self.ui.cb_speech.isChecked())
        self.ui.cb_onedigit.setEnabled(self.ui.cb_speech.isChecked())
        self.accepted.connect(self.exportSettings)
        self.ui.cb_speech.clicked.connect(self.updateSound)
        if IS_SOUND_WORKING:
            self.ui.cb_speech.setEnabled(True)
            self.ui.pm_warning.hide()
        elif not IS_SOUND_AVAILABLE:
            self.ui.pm_warning.setToolTip(self.tr('Sound is not working with Pyqt5/QtMultimedia/Gstreamer'))
        self.adjustSize()

    def importSettings(self, mysettings):
        self.ui.sb_flash.setValue(mysettings['flash'])
        self.ui.sb_timeout.setValue(mysettings['timeout'])
        self.ui.sb_digits.setValue(mysettings['digits'])
        self.ui.sb_rows.setValue(mysettings['rows'])
        self.ui.cb_speech.setChecked(mysettings['speech'])
        self.ui.cb_language.addItems(LANG_LIST)
        if mysettings['speech']:
            try:
                indx = LANG_LIST.index(mysettings['lang'])
                self.ui.cb_language.setCurrentIndex(indx)
            except ValueError:
                self.ui.cb_language.setCurrentIndex(-1)
            self.ui.l_language.setEnabled(True)
            self.ui.cb_language.setEnabled(True)
        self.ui.cb_onedigit.setChecked(mysettings['one_digit'])
        self.ui.cb_fullscreen.setChecked(mysettings['fullscreen'])
        self.ui.cb_handsfree.setChecked(mysettings['hands_free'])
        self.ui.cb_neg.setChecked(mysettings['neg'])
        self.mysettings = mysettings

    def exportSettings(self):
        mysettings = {}
        mysettings['flash'] = self.ui.sb_flash.value()
        mysettings['timeout'] = self.ui.sb_timeout.value()
        mysettings['digits'] = self.ui.sb_digits.value()
        mysettings['rows'] = self.ui.sb_rows.value()
        mysettings['speech'] = self.ui.cb_speech.isChecked()
        mysettings['lang'] = self.ui.cb_language.currentText()
        mysettings['fullscreen'] = self.ui.cb_fullscreen.isChecked()
        mysettings['hands_free'] = self.ui.cb_handsfree.isChecked()
        mysettings['one_digit'] = self.ui.cb_onedigit.isChecked()
        mysettings['neg'] = self.ui.cb_neg.isChecked()
        self.mysettings = mysettings

    def updateSound(self):
        sound = self.ui.sb_flash.isEnabled()
        self.ui.sb_flash.setEnabled(not sound)
        self.ui.cb_onedigit.setEnabled(sound)
        self.ui.l_language.setEnabled(sound)
        self.ui.cb_language.setEnabled(sound)

    def exec_(self):
        ok = QtWidgets.QDialog.exec_(self)
        return (ok, self.mysettings)

class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None, flag=QtCore.Qt.Widget):
        QtWidgets.QMainWindow.__init__(self, parent, flag)
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.score = (0,0)
        self.started = False
        self.sounds = {}
        self.query = {'number': '', 'lang': LANG}
        # default settings
        self.digits = 1
        self.rows = 5
        self.flash = 500
        self.timeout = 1500
        self.neg = False
        self.speech = False
        self.lang = 'en-US'
        self.lang_list = []
        self.one_digit = False
        self.fullscreen = False
        self.hands_free = False
        self.tmpwav= None
        self.replay = False
        self.noscore = False
        self.history = []
        self.font_color = None
        self.background_color = None
        self.annoying_sound = False
        self.no_plus_sign = False

        self.isLabelClearable = True
        self.geometryLabel = None

        self.timerUpdateLabel = QtCore.QTimer()
        self.timerUpdateLabel.setSingleShot(True)
        self.timerUpdateLabel.timeout.connect(self.updateLabel)
        self.timerShowAnswer = QtCore.QTimer()
        self.timerShowAnswer.setSingleShot(True)
        self.timerShowAnswer.timeout.connect(self.showAnswer)
        self.timerRestartPlay = QtCore.QTimer()
        self.timerRestartPlay.setSingleShot(True)
        self.timerRestartPlay.timeout.connect(self.restartPlay)

        if IS_SYSTEMRANDOM_AVAILABLE:
            self.randint = SystemRandom().randint
        else:
            self.randint = randint

        self.ui.label.clear()
        # using an inputmask gives a bug when double clicking in any other apps if le_answer has the focus
        #self.ui.le_answer.setInputMask('000000009')
        self.ui.l_total.hide()

        self.shortcut_F11 = QtWidgets.QShortcut(QtGui.QKeySequence('F11'), self)
        self.shortcut_F11.activated.connect(self.updateFullScreen)
        self.shortcut_Enter = QtWidgets.QShortcut(QtGui.QKeySequence('Enter'), self)
        self.shortcut_Enter.activated.connect(self.ui.pb_start.click)

        self.ui.pb_check.clicked.connect(self.updateAnswer)
        self.ui.pb_settings.clicked.connect(self.changeSettings)
        self.ui.pb_exit.clicked.connect(self.close)
        self.ui.pb_start.clicked.connect(self.startPlay)
        self.ui.pb_replay.clicked.connect(self.redisplaySequence)

        self.ui.label.setPixmap(QtGui.QPixmap(WELCOME))

        if IS_SOUND_AVAILABLE:
            self.player = QtMultimedia.QMediaPlayer()
            self.player.setAudioRole(QtMultimedia.QAudio.VoiceCommunicationRole)

        # add url in statusbar
        self.ui.statusbar.showMessage('www.sorobanexam.org')

        self.importSettings()
        # change background and foreground color if needed
        stylesheet = []
        if self.background_color is not None and self.background_color != 'transparent':
            stylesheet.append('background-color: %s' % self.background_color)
        if self.font_color is not None:
            stylesheet.append('color: %s' % self.font_color)
        if stylesheet != []:
            self.ui.label.setStyleSheet(';'.join(stylesheet))

        if self.fullscreen:
            self.showFullScreen()
        else:
            self.showNormal()

        # resize font
        font = self.ui.label.font()
        # width is the size of of '+9999' in the current font
        width = QtGui.QFontMetrics(font).width('+'+'9'*(self.digits+2))
        # the factor to multiply by to use the max. space
        factor = float(self.ui.gb_number.width())/width
        newPointSize = min(int(font.pointSize()*factor), self.ui.gb_number.height())
        font.setPointSize(newPointSize)
        self.ui.label.setFont(font)

    def importSettings(self):
        # restore settings from the settings file if the settings exist
        settings = QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope, appName, appName)
        if settings.contains('digits'):
            # these value have been written by the program, so then should be ok
            self.digits = int(settings.value('digits'))
            self.rows = int(settings.value('rows'))
            self.timeout = int(settings.value('timeout'))
            self.flash = int(settings.value('flash'))
            self.hands_free = eval(settings.value('hands_free').capitalize())
            self.neg = eval(settings.value('neg').capitalize())
            if settings.contains('no_plus_sign'):
                self.no_plus_sign = eval(settings.value('no_plus_sign').capitalize())

        # GUI settings
        if settings.contains('GUI/fullscreen'):
            self.fullscreen = eval(settings.value('GUI/fullscreen').capitalize())
        if settings.contains('GUI/font'):
            font = str(settings.value('GUI/font'))
            self.ui.label.setFont(QtGui.QFont(font, 72, QtGui.QFont.Bold))
        if settings.contains('GUI/font_color'):
            self.font_color = str(settings.value('GUI/font_color'))
        if settings.contains('GUI/background_color'):
            self.background_color = str(settings.value('GUI/background_color'))

        # Sound settings
        if settings.contains('Sound/speech'):
            self.speech = eval(settings.value('Sound/speech').capitalize())
        if settings.contains('Sound/one_digit'):
            self.one_digit = eval(settings.value('Sound/one_digit').capitalize())
        if settings.contains('Sound/annoying_sound'):
            self.annoying_sound = eval(settings.value('Sound/annoying_sound').capitalize())
        if settings.contains('Sound/lang'):
            self.lang = str(settings.value('Sound/lang'))

        # uuid
        self.uuid = ''
        if settings.contains('uuid'):
            self.uuid = str(settings.value('uuid'))
        else:
            import uuid
            self.uuid = str(uuid.uuid4())
        if self.uuid.lower() not in ('', 'no', 'none', 'false', 'opt-out', 'optout'):
            # call home
            try:
                settings.setValue('uuid', QtCore.QVariant(self.uuid))
                #url = 'http://localhost:8080/mentalcalculation/ping?uuid=%s&version=%s' % (self.uuid, appVersion)
                url = f'https://www.sorobanexam.org/mentalcalculation/ping?uuid={self.uuid}&version={appVersion}'
                ret = urllib.request.urlopen(url, context=ssl_context)
                if ret.getcode() == 200:
                    latest_version = json.loads(ret.read().decode('utf-8'))['latest']
                    if latest_version > appVersion:
                        self.ui.statusbar.showMessage('A new version is available at www.sorobanexam.org/anzan.html')
                # stop tracking if url returns 404
                if ret.getcode() == 404:
                    settings.setValue('uuid', QtCore.QVariant('opt-out'))
            except urllib.error.URLError:
                pass

    def changeSettings(self):
        if not self.started:
            mysettings = {}
            mysettings['flash'] = self.flash
            mysettings['timeout'] = self.timeout
            mysettings['digits'] = self.digits
            mysettings['rows'] = self.rows
            mysettings['speech'] = self.speech
            mysettings['fullscreen'] = self.fullscreen
            mysettings['hands_free'] = self.hands_free
            mysettings['one_digit'] = self.one_digit
            mysettings['neg'] = self.neg
            mysettings['lang'] = self.lang
            s = Settings(mysettings, parent=self)
            s.ui.cb_fullscreen.stateChanged.connect(self.updateFullScreen)
            ok, mysettings = s.exec_()
            if ok:
                self.flash = mysettings['flash']
                self.timeout = mysettings['timeout']
                if mysettings['digits'] != self.digits:
                    # resize font
                    font = self.ui.label.font()
                    # width is the size of of '+9999' in the current font
                    width = QtGui.QFontMetrics(font).width('+'+'9'*(mysettings['digits']+2))
                    # the factor to multiply by to use the max. space
                    factor = float(self.ui.gb_number.width())/width
                    newPointSize = min(int(font.pointSize()*factor), self.ui.gb_number.height())
                    font.setPointSize(newPointSize)
                    self.ui.label.setFont(font)
                self.digits = mysettings['digits']
                self.rows = mysettings['rows']
                self.speech = mysettings['speech']
                self.one_digit = mysettings['one_digit']
                self.hands_free = mysettings['hands_free']
                self.neg = mysettings['neg']
                self.lang = mysettings['lang']
                # always save settings when closing the settings dialog
                settings = QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope, appName, appName)
                settings.setValue('digits', QtCore.QVariant(self.digits))
                settings.setValue('rows', QtCore.QVariant(self.rows))
                settings.setValue('timeout', QtCore.QVariant(self.timeout))
                settings.setValue('flash', QtCore.QVariant(self.flash))
                settings.setValue('hands_free', QtCore.QVariant(self.hands_free))
                settings.setValue('neg', QtCore.QVariant(self.neg))
                settings.setValue('no_plus_sign', QtCore.QVariant(self.no_plus_sign))

                settings.setValue('GUI/font_color', QtCore.QVariant(self.font_color if self.font_color is not None else '#000000'))
                settings.setValue('GUI/background_color', QtCore.QVariant(self.background_color \
                        if self.background_color is not None else 'transparent'))

                settings.setValue('Sound/lang', QtCore.QVariant(self.lang))
                settings.setValue('Sound/one_digit', QtCore.QVariant(self.one_digit))
                settings.setValue('Sound/speech', QtCore.QVariant(self.speech))
                settings.setValue('Sound/lang', QtCore.QVariant(self.lang))
                settings.setValue('Sound/annoying_sound', QtCore.QVariant(self.annoying_sound))

                # disable replay button
                self.ui.pb_replay.setEnabled(False)
                # go to full screen if needed

    def updateFullScreen(self):
        self.fullscreen = not self.fullscreen
        settings = QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope, appName, appName)
        settings.setValue('GUI/fullscreen', QtCore.QVariant(self.fullscreen))

        if self.fullscreen:
            self.showFullScreen()
        else:
            self.showNormal()

    def clearLabel(self):
        if self.isLabelClearable:
            if IS_SOUND_AVAILABLE and self.player.state() != QtMultimedia.QMediaPlayer.StoppedState:
                return
            self.ui.label.clear()
            # something is wrong: the numbers of call to this function grow over time !
            # disconnect sender to try to fix this
            try:
                self.sender().disconnect()
            except TypeError as t:
                pass
            # display the next number after timeout
            self.timerUpdateLabel.setInterval(self.timeout)
            self.timerUpdateLabel.start()

    def restartPlay(self):
        if self.started:
            duration = self.timeout
            if self.speech and IS_SOUND_WORKING:
                self.player.stateChanged.disconnect(self.restartPlay)
                self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(THREEBELLS)))
                duration += THREEBELLS_DURATION
                self.player.play()
                self.player.stateChanged.connect(self.clearLabel)
            self.isLabelClearable = False
            self.started = False
            self.ui.label.clear()
            self.ui.l_total.hide()
            self.ui.pb_replay.setEnabled(False)
            self.ui.label.setPixmap(QtGui.QPixmap(RESTART))
            QtCore.QTimer.singleShot(duration, self.startPlay)

    def redisplaySequence(self):
        self.isLabelClearable = False
        self.started = False
        self.replay = True
        self.ui.pb_replay.setEnabled(False)
        self.timerUpdateLabel.stop()
        if self.hands_free:
            if self.speech and IS_SOUND_AVAILABLE:
                try:
                    self.player.stateChanged.disconnect(self.restartPlay)
                except TypeError as t:
                    pass
            self.timerShowAnswer.stop()
            self.timerRestartPlay.stop()
            self.ui.l_total.hide()
        self.startPlay()

    def startPlay(self):
        if not self.started:
            self.ui.statusbar.clearMessage()
            self.started = True
            self.isLabelClearable = True
            self.ui.label.clear()
            self.ui.l_total.hide()
            #self.ui.l_answer.setText('Your answer')
            self.ui.le_answer.clear()
            self.ui.le_answer.setEnabled(False)
            self.ui.pb_check.setEnabled(False)
            self.ui.pb_settings.setEnabled(False)
            try:
                self.shortcut_Enter.activated.disconnect(self.ui.pb_check.click)
            except TypeError:
                pass
            self.shortcut_Enter.activated.connect(self.ui.pb_start.click)
            self.count = 0
            # generate sequence
            if self.replay:
                self.replay = False
            else:
                self.makeHistory()
                if self.speech:
                    self.downloadSounds()
                self.noscore = False
                self.ui.pb_replay.setEnabled(False)
            # change pb_start to 'Stop' when starting display
            self.ui.pb_start.setText(self.tr('&Stop'))
            self.ui.pb_start.setToolTip(self.tr('Stop the sequence'))
            if IS_SOUND_AVAILABLE:
                if self.speech:
                    self.player.stop()
                elif self.annoying_sound:
                    self.player.stateChanged.disconnect(self.clearLabel)
                    self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(ANNOYING_SOUND)))
                    self.player.play()
                    self.player.stateChanged.connect(self.clearLabel)
            if self.hands_free:
                self.ui.l_answer.setEnabled(False)
            # wait 1s before starting the display
            self.timerUpdateLabel.setInterval(1000)
            self.timerUpdateLabel.start()
        else:
            # then stop it
            self.started = False
            self.isLabelClearable = False
            self.timerUpdateLabel.stop()
            if self.hands_free:
                if self.speech and IS_SOUND_AVAILABLE:
                    try:
                        self.player.stateChanged.disconnect(self.clearLabel)
                    except TypeError as t:
                        pass
                self.timerShowAnswer.stop()
                self.timerRestartPlay.stop()
                self.ui.l_answer.setEnabled(True)
                self.ui.l_total.hide()
            self.ui.pb_settings.setEnabled(True)
            self.ui.gb_number.setTitle('#')
            self.ui.pb_start.setText(self.tr('&Start'))
            self.ui.pb_start.setToolTip(self.tr('Start a sequence'))
            self.ui.label.clear()
            if args.verbose:
                print()
            if self.speech and IS_SOUND_WORKING:
                self.player.stop()
            if not self.hands_free:
                # reset history
                self.history = []

    def makeHistory(self):
        answer = 0
        self.history = []
        for i in range(self.rows):
            a,b = DIGIT[self.digits]
            neg = False
            if self.neg:
                neg = bool(self.randint(0,1))
            if neg:
                if answer > a:
                    b = min(b, answer)
                else:
                    neg = False
            n = self.randint(a, b)
            # avoid a n - n situation
            while neg and n == self.history[-1]:
                n = self.randint(a, b)
            if neg and answer - n >= 0:
                n = -n
            answer += n
            self.history.append(n)
        self.answer = answer

    def downloadSounds(self):
        nb_dls = len(self.history) + (1 if self.hands_free else 0)
        self.ui.statusbar.showMessage(self.tr('Downloading {} sounds').format(nb_dls))
        #self.sounds = {}
        threads = []
        global nb_dleds
        nb_dleds = 0
        for i,n in enumerate(self.history):
            t = '%d' % n
            if t in self.sounds and self.sounds[t] != BELL:
                nb_dls -= 1
                continue
            if self.neg and i > 0:
                t = '%+d' % n
            if self.no_plus_sign and t.startswith('+'):
                t = t[1:]
            if self.one_digit:
                t = ' '.join(list(t)).replace('- ', '-')
            if t not in self.sounds:
                self.query.update({'number': t, 'lang': self.lang})
                query_string = '&'.join(f'{k}={urllib.parse.quote(v)}' for k,v in self.query.items())
                url = f'{APIURL}?{query_string}'
                t = Thread(target=dl_thread, args=(url, t, self.sounds, self.ui.statusbar, self.tr, nb_dls))
                t.start()
                threads.append(t)

        if self.hands_free:
            t = '= %d' % self.answer
            if self.one_digit:
                t = ' '.join(list(t)).replace('- ', '-')
            if t not in self.sounds:
                self.query.update({'number': t, 'lang': self.lang})
                query_string = '&'.join(f'{k}={urllib.parse.quote(v)}' for k,v in self.query.items())
                url = f'{APIURL}?{query_string}'
                t = Thread(target=dl_thread, args=(url, t, self.sounds, self.ui.statusbar, self.tr, nb_dls))
                t.start()
                threads.append(t)

        for t in threads:
            t.join()
        self.ui.statusbar.clearMessage()

    def pronounceit(self, s):
        self.player.stop()
        try:
            self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(self.sounds[s])))
            self.player.play()
            self.player.stateChanged.connect(self.clearLabel)
        except KeyError:
            print(f'Error: {s} not found in sounds')
            QtCore.QTimer.singleShot(2000, self.clearLabel)

    def updateAnswer(self):
        if self.ui.le_answer.isEnabled():
            try:
                a = int(self.ui.le_answer.text())
            except ValueError:
                a = -100
            u,v = self.score
            v += 1
            if  a == self.answer:
                img = SMILE
                sound = GOOD
                msg = ':-)'
                u += 1
            else:
                msg = ':-('
                img = SAD
                sound = BAD
            # Don't score twice if replay
            if not self.noscore:
                self.score = u,v
            if msg == ':-)':
                self.noscore = True
            self.ui.l_total.show()
            self.ui.l_total.setText(self.tr('The correct answer is {}').format(self.answer))
            self.ui.le_answer.setDisabled(True)
            self.ui.pb_check.setDisabled(True)
            self.ui.label.setPixmap(QtGui.QPixmap(img))
            if self.speech and IS_SOUND_WORKING:
                self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(sound)))
                self.player.play()
            self.ui.statusbar.showMessage(self.tr('Score: {}/{}').format(u, v))
            self.shortcut_Enter.activated.disconnect(self.ui.pb_check.click)
            self.shortcut_Enter.activated.connect(self.ui.pb_start.click)

            if args.verbose:
                sys.stdout.flush()

    def showAnswer(self):
        if self.started:
            self.ui.l_total.show()
            self.ui.l_total.setText(self.tr('The correct answer is {}').format(self.answer))
            self.ui.label.setText('=%d' % self.answer)
            if self.speech and IS_SOUND_WORKING:
                # pronounce one digit at a time
                t = '= %d' % self.answer
                if args.verbose:
                    print(t)
                if self.one_digit:
                    t = ' '.join(list(t)).replace('- ', '-')
                self.player.stateChanged.disconnect(self.clearLabel)
                self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(self.sounds[t])))
                self.player.play()
                self.player.stateChanged.connect(self.restartPlay)
            else:
                QtCore.QTimer.singleShot(self.timeout+2000, self.ui.label.clear)
                QtCore.QTimer.singleShot(self.timeout+2000, self.ui.l_total.hide)
                self.timerRestartPlay.setInterval(2*self.flash+2000)
                self.timerRestartPlay.start()

    def updateLabel(self):
        if self.started:
            if self.count == self.rows:
                self.isLabelClearable = False
                if not self.hands_free:
                    self.started = False
                duration = self.timeout+2000
                if self.speech and IS_SOUND_WORKING:
                    self.player.stop()
                    self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(BELL)))
                    self.player.play()
                    self.player.stateChanged.connect(self.clearLabel)
                    duration += BELL_DURATION

                self.ui.label.setText('?')
                self.ui.gb_number.setTitle('#')
                self.ui.pb_replay.setEnabled(True)
                if self.hands_free:
                    self.timerShowAnswer.setInterval(duration)
                    self.timerShowAnswer.start()
                else:
                    self.ui.pb_start.setText(self.tr('&Start'))
                    self.ui.pb_start.setToolTip(self.tr('Start a sequence'))
                    self.ui.le_answer.setEnabled(True)
                    self.ui.le_answer.setFocus(QtCore.Qt.OtherFocusReason)
                    self.ui.le_answer.clear()
                    self.ui.pb_check.setEnabled(True)
                    self.ui.pb_settings.setEnabled(True)
                    try:
                        self.shortcut_Enter.activated.disconnect(self.ui.pb_start.click)
                    except TypeError:
                        pass
                    self.shortcut_Enter.activated.connect(self.ui.pb_check.click)
                if args.verbose:
                    print()
            else:
                self.count += 1
                self.ui.gb_number.setTitle(f'#{self.count} / {self.rows}')
                n = self.history[self.count-1]
                t = '%d' % n
                if self.neg and self.count > 1:
                    t = '%+d' % n
                if self.no_plus_sign and t.startswith('+'):
                    t = t[1:]
                self.ui.label.setText(t)
                # print the sequence in the console
                if args.verbose:
                    print(t, end=' ')
                # say it aloud
                if IS_SOUND_AVAILABLE:
                    if self.speech:
                        # pronounce one digit at a time
                        if self.one_digit:
                            t = ' '.join(list(t)).replace('- ', '-')
                        self.pronounceit(t)
                    else:
                        if self.annoying_sound:
                            self.player.stateChanged.disconnect(self.clearLabel)
                            self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(ANNOYING_SOUND)))
                            self.player.play()
                            self.player.stateChanged.connect(self.clearLabel)
                        else:
                            # clear the label after self.flash time
                            QtCore.QTimer.singleShot(self.flash, self.clearLabel)
                else:
                    QtCore.QTimer.singleShot(self.flash, self.clearLabel)

    def resizeEvent(self, e):
        QtWidgets.QMainWindow.resizeEvent(self, e)
        font = self.ui.label.font()
        # width is the size of of '+9999' in the current font
        width = QtGui.QFontMetrics(font).width('+'+'9'*(self.digits+2))

        # the factor to multiply by to use the max. space
        factor = float(self.ui.gb_number.width())/width
        newPointSize = min(int(font.pointSize()*factor), self.ui.gb_number.height())

        font.setPointSize(newPointSize)
        self.ui.label.setFont(font)

        if self.ui.label.pixmap == None and self.ui.label.text() == '':
            self.ui.label.setText('9'*self.digits)
            QtCore.QTimer.singleShot(150, self.ui.label.clear)

    def closeEvent(self, event):
        # stop the player
        if IS_SOUND_AVAILABLE and self.player:
            self.player.stop()
            self.player = None
        # delete all tmp files
        for fn in self.sounds.values():
            try:
                os.unlink(fn)
            except FileNotFoundError:
                pass
        QtWidgets.QMainWindow.closeEvent(self, event)

def dl_thread(url, t, sounds, statusbar, tr, nb_dls):
    global nb_dleds
    try:
        ret = urllib.request.urlopen(url, context=ssl_context)
        if ret.getcode() != 200:
            print(f"Error: can't download sound for {t}")
            statusbar.showMessage('An error occurred when downloading sound')
            sounds[t] = BELL
        else:
            data = ret.read()
            with NamedTemporaryFile(prefix='mentalcalculation', suffix='.mp3', delete=False) as f:
                f.write(data)
                sounds[t] = f.name
            nb_dleds += 1
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        print(f"Error: can't download sound for {t}")
        statusbar.showMessage('An error occurred when downloading sound')
        # use the bell sound instead
        with NamedTemporaryFile(prefix='mentalcalculation', suffix='.mp3', delete=False) as f:
            g = open(BELL, 'rb')
            # copy the file data
            f.write(g.read())
            g.close()
            sounds[t] = f.name

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Practice anzan/mentalcalculation')
    parser.add_argument('-v', '--verbose', action='store_true', help='be verbose: print in console each number displayed')
    args = parser.parse_args()

    IS_SOUND_WORKING = IS_SOUND_AVAILABLE

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('Mental Calculation')

    # initialize locale and load translation files if available
    locale = QtCore.QLocale()
    LOCALENAME = str(locale.system().name())
    translator = QtCore.QTranslator()
    translator.load(str(SHARE_PATH / f'i18n/{LOCALENAME}'), '.')
    app.installTranslator(translator)

    if LOCALENAME.find('_') > 0:
        LANG = LOCALENAME.replace('_', '-').lower()
    else:
        LANG = LOCALENAME

    # create main gui and display settings dialog
    f = Main()
    f.show()
    f.raise_() # for Mac Os X
    f.changeSettings()

    sys.exit(app.exec_())
