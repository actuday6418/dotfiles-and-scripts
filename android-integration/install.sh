#!/bin/bash

#Run as root
if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    echo -e "Not running as root..\nExiting.."
    exit
fi

yay -S scrcpy
cp sndcpy /usr/bin
cp -r sndcpy-exec /opt/

