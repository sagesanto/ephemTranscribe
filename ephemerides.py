#program assumes n arguments, all of which are the names of objects, exactly as they appear on the ephemerides webpage, in the exact order they appear on the ephemerides webpage
#assume downloaded text file of a ephemerides page titled "ephems.txt" in root directory

#separate out by name: identify the relevant text for each and write each to own text file in subfolder
#then invoke awk command to transform each to telescope readable format in subfolder
import sys
import os
if len(sys.argv) == 1:
    raise Exception("Program expects the number of objects as an argument")
numObjects = sys.argv[1]
filenames = []
os.mkdir("ephemeridesDir")
with open('ephems.txt') as f:
    for i in range(int(numObjects)):
        l = f.readline()
        filenames.append(l.replace('\n', ''))
        w = open('ephemeridesDir/' + filenames[-1] + '_ephem.txt', 'w')
        w.write(l)
        while True:
            l = f.readline()
            if l == " \n":
                w.close()
                break
            w.write(l) #put this after line 14 if the file needs to end with the whitespace
for name in filenames:
    os.system("awk -f MPC_scheduler_script_1.awk ephemeridesDir/" + name + "_ephem.txt > /ephemeridesDir" + name + "_scheduler.txt")
# probably wont be able to find the files because they're in the ephemeridesDir directory
#  -> needs to be fixed when I can test on a linux vbox