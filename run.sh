#!/usr/bin/env bash

# Kill the program if already running
pkill walli

# Wait until the processes have been shut down
while pgrep -x walli >/dev/null; do sleep 1; done


## Variable
WALLI_BIN="$HOME/bin/walli"
IMG_DIR="$HOME/.config/walli/images"
TIME=210
TRANSP=85

# You might need to modify the below information
# The Syntax is: 
#   walli $(folder with images) $(time between changes) $(transparency)
# $HOME/bin/walli $HOME/.config/walli/images 300 85

# >>> Make this last <<<
exec $WALLI_BIN "$IMG_DIR" $TIME $TRANSP
