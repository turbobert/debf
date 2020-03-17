#!/bin/bash


# am I a symlink?
SCRIPT_SRC=$(readlink $0)
if [[ $? = 0 ]]; then
    SCRIPT_DIR=$(dirname $SCRIPT_SRC)
    ( cd $SCRIPT_DIR && exec pipenv run python debf.py "$@" )
fi
