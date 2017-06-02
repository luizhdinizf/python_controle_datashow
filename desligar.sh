#!/bin/sh
export DISPLAY=:0
xrandr --output LVDS1 --auto
shutdown
python ~/Datashow/desligar.py
