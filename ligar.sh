#!/bin/sh
export DISPLAY=:0
xrandr --output LVDS1 --off
python ~/Datashow/ligar.py 
kodi
