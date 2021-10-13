#!/usr/bin/env python
import os
import time
import sys
import random
import shutil
import psutil
import argparse
import pywal
from subprocess import call

#####################
## Setup Variables ##
#####################
CONFIG_DIR = os.path.expanduser('~/.config/walli/')
DEFAULT_DIR = os.path.expanduser('~/.config/walli/images/')
BACKGROUND_FILE = pywal.wallpaper.get()

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
    #Waits till the time is set
    while True:
        #Performs the command after time.
        time.sleep(TIME)
        #Selects a random image file
        image_try = pywal.image.get(DIR)
        while image_try == pywal.wallpaper.get():
            image_try = pywal.image.get(DIR)
        else:
            image = image_try
        pywal.wallpaper.change(image)

##########
## Main ##
##########

def main(**kwargs):
    ap = argparse.ArgumentParser(description='Something fantastic', epilog='Here is an epilog')
    ap.add_argument('-d', metavar='Working Directory', action='store_const', const=str, help='The directory containing images to use for wallpapers.', default=DEFAULT_DIR)
    ap.add_argument('-f', metavar='Current Wallpaper', type=argparse.FileType('w', encoding='UTF-8'), help='Destination to save current wallpaper', default=BACKGROUND_FILE)
    ap.add_argument('-t', metavar='Time', type=int, help='Time between wallpaper changes', default=210)
    ap.add_argument('-o', metavar='Opacity', type=int, help='Opacity Level', default=85)
    args = ap.parse_args()
    kill_wall()
    set_wall(args)

###########
## Start ##
###########

if __name__ == '__main__':
    main()
