# Extract any archive with "ex".
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

# Environment variables
export PATH=$HOME/.local/bin:$PATH
export PATH=$HOME/.local/bin/appimages:$PATH
export PATH=$HOME/.config/scripts:$PATH
export EDITOR=nvim
export STARSHIP_CONFIG=$HOME/.config/starship/starship-zsh.toml
export TIMEFMT=$'\nreal\t%*E\nuser\t%*U\nsys\t%*S'

# Configuration
source $HOME/.config/zsh/.zshconf

# Plugins
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

# Tty aliases
alias x='startx'

# Basic aliases
alias la='ls -a --color -h --group-directories-first'
alias ll='ls -l --color -h --group-directories-first'
alias lla='ls -la --color -h --group-directories-first'
alias ls='ls --color=auto --color -h --group-directories-first'
alias rm='rm -i'

# Config aliases
alias bashrc='nvim $HOME/.bashrc'
alias zshrc='nvim $HOME/.config/zsh/.zshrc'
alias zshenv='nvim $HOME/.zshenv'
alias zshconf='nvim $HOME/.config/zsh/.zshconf'
alias xinitrc='nvim $HOME/.xinitrc'
alias bspwmrc='nvim $HOME/.config/bspwm/bspwmrc'
alias sxhkdrc='nvim $HOME/.config/sxhkd/sxhkdrc'
alias picomconf='nvim $HOME/.config/picom/picom.conf'
alias critty='nvim $HOME/.config/alacritty/alacritty.yml'
alias polyconf='nvim $HOME/.config/polybar/config.ini'
alias kittyconf='nvim $HOME/.config/kitty/kitty.conf'

# Mpv
alias stpl1='mpv --no-video https://youtube.com/playlist?list=PL3ZislPZVGMgeuQYpgC_4WY7TgdEpdQgU'
alias stpl2='mpv --no-video https://www.youtube.com/playlist?list=PL3ZislPZVGMi2MsmKMd3Ow4KZY5ZoRKkn'
alias rain1='mpv --no-video --loop-file=inf https://www.youtube.com/watch?v=mPZkdNFkNps'
alias rain2='mpv --no-video --loop-file=inf https://www.youtube.com/watch?v=wRJdLJlyv9A'
alias storm1='mpv --no-video --loop-file=inf https://www.youtube.com/watch?v=sGkh1W5cbH4'
alias space1='mpv --no-video --loop-file=inf https://www.youtube.com/watch?v=bjQUCecur3w'
alias focus1='mpv --no-video --loop-file=inf https://www.youtube.com/watch?v=1_G60OdEzXs'

# Termdown
alias stopwatch='termdown --font big'
function countdown { termdown "$1" --font big -B; mpv --no-video --loop --volume=80 $HOME/others/media/assets/alarm.wav; }

# Others
alias sxev="xev | awk -F'[ )]+' '/^KeyPress/ { a[NR+2] } NR in a { printf \"%-3s %s\n\", \$5, \$8 }'"
# function code { alacritty -o window.opacity=1 window.padding.x=5 window.padding.y=0 window.dynamic_padding=true -e nvim "$1"; }
function code { kitty -o background_opacity=1 -o window_padding_width='0 5' -e nvim "$1"; }
