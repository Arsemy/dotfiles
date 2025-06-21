# Configuration file
*mentalcalculation* saves its settings in a configuration file:
On Linux/or any unix-like

    ~/.config/mentalcalculation/mentalcalculation.ini
On Windows Vista and above

    C:\Users\<your_user_name>\AppData\Roaming\mentalcalculation\mentalcalculation.ini

You might need to change the options of the *Windows explorer* to be able to see hidden files and directories
to be able to access the configuration file.

You need to run *mentalcalculation* (and close it), at least once so that the configuration file is written to disk.

Note: It does not do anything to the Windows registry at all !

## Customization
The default configuration file looks like this:

    ; comments are lost after mentalcalculation starts
    [General]
    digits=1
    rows=5
    timeout=1500
    flash=500
    hands_free=false
    neg=false
    no_plus_sign=false
    uuid=xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxx

    [GUI]
    font_color=#000000
    background_color=transparent

    [Sound]
    one_digit=false
    speech=false
    annoying_sound=false
    lang=en-us

## Colors

You can change font and background colors in the ``[GUI]`` section. Change `font_color` and/or `background_color` to valid HTML color codes or use explicit name.

If you look for a way to choose a color, you could use the color picker of your favorite graphic software, or go online at https://www.colorpicker.com/, or https://html-color-codes.info/.

## Fonts

One can use a custom font for the display of number. Add a `font` variable in the ``[GUI]`` section. The variable should only hold a family font name. For example:

    font=Times New Roman

## Sound

Change `annoying_sound` variable in the ``[Sound]`` section to true to get a sound every time a number is displayed on screen.

The sound is played only if you don't use the speak synthesis system.

By default, the file called *annoying-sound.mp3* in the sound directory of *mentalcalculation* is used. You can change it to any sound you like.

## Plus sign

One can remove the + sign in front of numbers if using subtraction by using this snippet in the conf. file

    noplussign=true

in the ``[General]`` section of the *mentalcalculation.ini*

## Opt-out from tracking

Yo can opt-out from trakcing usage of mentalcalculation by adding:

    uuid=opt-out

in the ``[General]`` section; you can also use any of the following values: no, No, none, None, false, False, optout or leave it empty.

Or if the line is already there, just change the value of uuid to one of the string mentionned above to opt-out.

