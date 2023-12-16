# PS1='[\u@\h \W]\$ '
PS1='\[\e[1;34m\]\W \[\e[0m\]  '

# Starship
eval "$(starship init bash)"

# Vi
set -o vi

# Environment variables
export STARSHIP_CONFIG=$HOME/.config/starship/starship-bash.toml

# Shell config
source $HOME/.config/shell/shellrc
