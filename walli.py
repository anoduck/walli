#!/usr/bin/env python

import os
import time
import argparse
import psutil
import pywal

#####################
## Setup Variables ##
#####################
CONFIG_DIR = os.path.expanduser('~/.config/walli/')
DEFAULT_DIR = os.path.expanduser('~/.config/walli/images/')
BACKGROUND_FILE = os.path.join(os.environ['HOME'], '.config/walli/background1')
PREV_IMAGE = os.path.join(os.environ['HOME'], '.cache/wal/wal')


################################
## Kill other walli processes ##
################################
PROCNAME = "walli"

def kill_wall():
    for proc in psutil.process_iter():
        #check that the process name matches
        if proc.name() == PROCNAME:
            proc.kill()

##############################
## Set Wallpaper - The Beef ##
##############################

def set_wall(args):
    #Sets the wallpaper directory
    DIR = args.d
    #Sets the pictuers destination
    DST1 = args.f
    #Sets the time to pause
    TIME = float(args.t)
    #Sets directory to the image directory
    os.chdir(DIR)
    ## Get File Size of previous
    PRWALL = os.path.getsize(PREV_IMAGE)
    #Waits till the time is set
    WAL_SET = bool(PRWALL > 60)
    #Performs the command after time.
    if WAL_SET is False:
        image = pywal.image.get(DIR)
        pywal.wallpaper.change(image)
    # Else wait for Time, check previous wallpaper
    else:
        time.sleep(TIME)
        image = pywal.image.get(DIR, DST1)
        pywal.wallpaper.change(image)

##########
## Main ##
##########

def main():
    ap = argparse.ArgumentParser(description='A Friendly Wallpaper Changer for I3 in Python', epilog='Rotates desktop wallpaper by defined time from defined directory with defined opacity.')
    ap.add_argument('-d', metavar='Working Directory', action='store_const', const=str, help='The directory containing images to use for wallpapers.', default=DEFAULT_DIR)
    ap.add_argument('-f', metavar='Current Wallpaper', type=argparse.FileType('w', encoding='UTF-8'), help='Destination to save current wallpaper', default=BACKGROUND_FILE)
    ap.add_argument('-t', metavar='Time', type=int, help='Time between wallpaper changes', default=150)
    ap.add_argument('-o', metavar='Opacity', type=int, help='Opacity Level', default=85)
    args = ap.parse_args()
    kill_wall()
    set_wall(args)

###########
## Start ##
###########

if __name__ == '__main__':
    main()
