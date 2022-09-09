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
PYTHON_TEST_SERVER="http://localhost:8000"
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
      pip install .[dev,postgres]
      python3 setup.py clean --all
      info "Finished installation"
      shift
      ;; # 3}}}
    uninstall) # uninstall {{{3
      warn "Uninstalling depy."
      pip uninstall depy
      warn "Uninstall complete."
      shift
      ;; # 3}}}
    clean) # clean {{{3
      info "Cleaning."
      find . -type f -name '*.py[co]' -delete \
        -o -type d -name __pycahce__ -delete
      rm -rf depy.egg-info/
      info "Finished cleaning."
      shift
      ;; # 3}}}
    test) # test {{{3
      warn "Testing"
      pytest --cov=depy --cov-report term-missing tests/
      shift
      ;; # 3}}}
    test-server) # test-server {{{3
      warn "Testing"
      pytest --cov=depy --cov-report=html || die
      cd htmlcov || die "no htmlcov dir available"
      python3 -m http.server 8000 &
      w3m "$PYTHON_TEST_SERVER" || xdg-open "$PYTHON_TEST_SERVER" || \
        open "$PYTHON_TEST_SERVER"
      shift
      ;; # 3}}}
    down-test-server) # spin down the test server {{{3
      warn "Spin down the test server."
      kill $(ps -e -o pid,command | \
        grep -oP "\d+\s(?=python3 -m http.server 8000)") || \
        die "Server is not running."
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
