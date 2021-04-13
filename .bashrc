#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1="\[\033[01;34m\]\w\[\033[00m\] "

if [ -f ~/.bash_aliases ]; then
. ~/.bash_aliases
fi

# Exports
export LANG="en_US.UTF-8"
export EDITOR="nvim"
export TERMINAL="urxvt"
export BROWSER="qutebrowser"
export TERM="rxvt-unicode-256color"
