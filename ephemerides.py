# Sage Santomenna, Pomona, 2022
# program assumes copy-pasted text file of an ephemerides page titled "ephems.txt" in root directory

import sys
import os
import fileinput
import re


# this little function looks for and attempts to fix an issue that occurred on 2022 09 28 with target C835WW2 where MPC_scheduler_script_1.awk
# failed to handle an overflow in dRA that led RA=0.087 (three decimals) and Dec = -10.97 to be interpreted as dRA = 0.087-10.97
def replace(path):
    with open(path, 'r') as file:
        filedata = file.read()
    filedata = (re.sub('\S\-', lambda m: m.group(0).replace('-', '') + ' -', filedata))
    with open(path, 'w') as file:
        file.write(filedata)


if len(sys.argv) == 1:
    raise Exception("Program expects the number of objects as its only argument")
numObjects = sys.argv[1]
filenames = []
os.mkdir("ephemeridesDir")
with open('ephems.txt') as f:
    for i in range(int(numObjects)):
        l = f.readline()
        l = f.readline()
        filenames.append(l.replace('\n', ''))
        print("found name " + l.replace('\n', ''))
        w = open('ephemeridesDir/' + filenames[-1] + '_ephem.txt', 'w')
        w.write(l)
        while True:
            l = f.readline()
            if l == " \n":
                w.close()
                break
            w.write(l)  # put this after line 14 if the file needs to end with the whitespace
for name in filenames:
    replace('ephemeridesDir/' + name + "_ephem.txt")
    os.system("awk -f MPC_scheduler_script_1.awk ephemeridesDir/" + name + "_ephem.txt > ephemeridesDir/" + name + "_scheduler.txt")

