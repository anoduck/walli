#!/usr/bin/env python

import os
import time
import argparse
import psutil
import pywal

#####################
## Setup Variables ##
#####################
from pywal.settings import CACHE_DIR

CONFIG_DIR = os.path.expanduser('~/.config/walli/')
DEFAULT_DIR = os.path.expanduser('~/.config/walli/images/')

################################
## Kill other walli processes ##
################################
PROCNAME = "walli"


def kill_wall():
    for proc in psutil.process_iter():
        # check that the process name matches
        if proc.name() == PROCNAME:
            proc.kill()


##############################
## Set Wallpaper - The Beef ##
##############################

def set_wall(args):
    # Sets directory to the image directory
    os.chdir(args.d)
    # Define image
    image = pywal.image.get(args.d)
    time.sleep(args.t)
    pywal.wallpaper.change(image)


##########
## Main ##
##########

def main():
    ap = argparse.ArgumentParser(description='A Friendly Wallpaper Changer for I3 in Python',
                                 epilog='Rotates desktop wallpaper by defined time from defined directory with defined opacity.')
    ap.add_argument('-d', metavar='Working Directory', action='store_const', const=str,
                    help='The directory containing images to use for wallpapers.', default=DEFAULT_DIR)
    ap.add_argument('-t', metavar='Time', type=int, help='Time between wallpaper changes', default=150)
    args = ap.parse_args()
    kill_wall()
    set_wall(args)


###########
## Start ##
###########

if __name__ == '__main__':
    main()
