#/usr/local/bin/env bash

# Kill the program if already running
pkill walli

# Wait until the processes have been shut down
while pgrep -x walli >/dev/null; do sleep 1; done

# You might need to modify the below information
# The Syntax is: 
#   walli $(folder with images) $(location of current background image) $(time between changes) $(transparency)
$HOME/bin/walli $HOME/.config/walli/images $HOME/.config/walli/background 300 85


