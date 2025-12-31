#!/bin/bash
xrandr --output eDP-1 --rotate normal
xinput set-prop "Elan Touchscreen" "Coordinate Transformation Matrix" 1 0 0  0 1 0  0 0 1

