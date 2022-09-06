#!/usr/bin/env bash
# ex: set fdm=marker
# usage {{{1 
#/ Usage: 
#/    -h|-?|--help)
#/       show this help and exit
#/
# 1}}} 
# environment {{{1 
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PROJECT=${PROJECT:-"Some Project Name in $DIR"}
# 1}}} 
# functions {{{1 
banner() { # {{{2
  # make a static banner with embeded color codes
  # BANNER=$(cat <<EOF\n  EOF;
  # for a simple banner use
  # BANNER="The \n$PROJECT\n\t script"
  # or have a little funn
  # BANNER=$(figlet "$PROJECT" | cowsay)
  # or do some coloring
  BANNER="\\e[32m$PROJECT\\e[39m"
  echo -e "$BANNER"
} # 2}}} 
die() { # {{{2 
  echo -e "\\e[31mFAILURE:\\e[39m $1"
  exit 1
} # 2}}} 
warn() { # {{{2 
  echo -e "\\e[33mWARNING:\\e[39m $1"
} # 2}}}
info() { # {{{2
  echo -e "\\e[32mINFO:\\e[39m $1"
} # 2}}}
show_help() { # {{{2 
  grep '^#/' "${BASH_SOURCE[0]}" | cut -c4- || \
    die "Failed to display usage information"
} # 2}}} 
# 1}}} 
# arguments {{{1 
while :; do
  case $1 in # check arguments {{{2 
    install) # install {{{3
      info "Beginning installation"
      git pull
      python3 -m ensurepip
      python3 -m pip install --upgrade pip
      python3 -m pip install -r requirements.txt
      pip install .
      python3 setup.py clean --all
      info "Finished installation"
      shift
      ;; # 3}}}
    -h|-\?|--help) # help {{{3 
      banner
      show_help
      exit
      ;; # 3}}} 
    -?*) # unknown argument {{{3 
      warn "Unknown option (ignored): $1"
      shift
      ;; # 3}}} 
    *) # default {{{3 
      break # 3}}} 
  esac # 2}}} 
done
# 1}}} 
# logic {{{1 
banner
# 1}}} 
