#!/bin/bash

verse=$(python random_line.py)

convert -background none -size 500x116 -font "Liberation-Mono-Bold" -gravity center -fill white caption:"$verse" image.png
composite image.png wallpaper.png -gravity south -geometry +0+100 final.png

rm image.png

feh --bg-scale final.png
