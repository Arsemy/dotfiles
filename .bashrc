#
# ~/.bashrc
#

#PS1='[\u@\h \W]\$ '
PS1='\[\e[1;34m\]\W \[\e[0m\]  '

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Path to mps-youtube
export PATH=$HOME/.local/bin:$PATH

## Archive extraction function ##
### Usage: ex <file> ###
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip  $1   ;;
      *.tar)       tar xf  $1   ;;
      *.tar.zst)   zstd -d $1   ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip   $1   ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x    $1   ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

# Start programs with bash
echo "          To-do "
todo list
echo

# Tty commands
alias x='startx'

# Basic terminal commands
alias la='ls -a'
alias ll='ls -l'
alias lla='ls -la'
alias ls='ls --color=auto'
alias rm='rm -r'

# Config commands
alias bashrc='nvim $HOME/.bashrc'
alias xinitrc='nvim $HOME/.xinitrc'
alias bspwmrc='nvim $HOME/.config/bspwm/bspwmrc'
alias sxhkdrc='nvim $HOME/.config/sxhkd/sxhkdrc'
alias picomconf='nvim $HOME/.config/picom/picom.conf'
alias yml='nvim $HOME/.config/alacritty/alacritty.yml'
alias polyconfig='nvim $HOME/.config/polybar/config.ini'

# Other commands
alias stpl1='mpv --no-video https://youtube.com/playlist?list=PL3ZislPZVGMgeuQYpgC_4WY7TgdEpdQgU'
alias stpl2='mpv --no-video https://www.youtube.com/playlist?list=PL3ZislPZVGMi2MsmKMd3Ow4KZY5ZoRKkn'
alias stopwatch='termdown --font big'
function countdown { termdown "$1" --font big -B; mpv --no-video --loop --volume=80 alarm.mp3; }
