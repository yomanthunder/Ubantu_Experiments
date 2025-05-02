#!/bin/bash

folder="$HOME/Pictures/s"
mkdir -p "$folder"

# Count existing files matching s<number>.png
count=$(ls "$folder"/s*.png 2>/dev/null | wc -l)

# Increment by 1
next_num=$((count + 1))
filename="s${next_num}.png"

# Take screenshot
gnome-screenshot -f "$folder/$filename"
