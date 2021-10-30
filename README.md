# KDEConnect wrapper
A slim bash script that wraps around kdeconnect-cli to simplify sharing files to other devices from the comfort of the terminal

## Usage 
1. ```mv send_file.sh ~/.configs/scripts/send_file.sh```
2. Use the script wherever you'd like to (Polybar for me)
3. OR add ```alias share ~/.configs/scripts/send_file.sh``` to your .bashrc
4. Reboot and ```share file.mp3```

# Android Integration
This is a modification of sndcpy and scrcpy with a script. It allows you to take complete control of your Android phone with a single command.

# Example
(This low quality GIF makes it looks choppy, but trust me, it's buttery smooth. You get keyboard and mouse control of your phone and audio is routed to your computer too. You can also set this up to work wirelessly.)

![output](https://user-images.githubusercontent.com/56124831/139525406-11571cd8-5d95-4086-82bf-f0828f423dfa.gif)

## Requirements:
1. The script uses yay to get scrcpy from the AUR, so you'll need to be on Arch
2. VLC ```pacman -S vlc```
3. ADB tools ```pacman -S adb-tools```
4. Root permissions for running the install script

## Usage
1. Run install.sh as root
2. Use the mirror script for starting the program. (Maybe map it to a button on polybar or something, or add it to your PATH variable)

# i3 and Polybar dotfiles
Try them. They're good.

