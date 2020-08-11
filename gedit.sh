#!/bin/bash 

HISTFILE=~/.bash_history
set -o history
history | grep -i "あえうあえう"

echo $?
if [ $? == 0 ]
then
    echo "PASS"
else
    echo "FAIL"
fi

