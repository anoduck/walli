#!/usr/bin/env python
import os, time, sys, random, shutil
from subprocess import call

#See if there is the right amount of arguments
if len(sys.argv)==4:
    #Sets the wallpaper directory
    DIR = sys.argv[1]
    #Sets the pictuers destination
    DST1 = DIR + "/background1"
    #  DST2 = "$DIR/background2"
    #Sets the time to pause
    TIME = float(sys.argv[2])
    #Sets directory to the image directory
    os.chdir(DIR)
    #Waits till the time is set
    while True:
        time.sleep(TIME)
        #Selects a random image file
        FILE1 = random.choice(os.listdir(DIR))
        #  FILE2 = random.choice(os.listdir(DIR))
        #  while FILE2 == FILE1:
            #  FILE2 = random.choice(os.listdir(DIR))
        #Deletes the image in the pictuers distanation
        #os.remove(DST)
        #Copies the file
        shutil.copy2(FILE1, DST1)
        #  shutil.copy2(FILE2, DST2)
        #Reseats i3wm
        call(["wal", "-c", "-i", DIR, "-a " + sys.argv[3]])
        call(["hsetroot", "-screens", "1", "-cover", DST1])
        #  call(["hsetroot", "-screens", "2", "-cover", DST2])

else:
    print("Please make sure that you have 3 arguments at the end of the command")
