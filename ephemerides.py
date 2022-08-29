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
os.mkdir("ephemerides")
with open('ephems.txt') as f:
    for i in range(int(numObjects)):
        l = f.readline()
        filenames.append(l.replace('\n', '') + '.txt')
        w = open('ephemerides/' + filenames[-1], 'w')
        w.write(l)
        while True:
            l = f.readline()
            if l == " \n":
                w.close()
                break
            w.write(l) #put this after line 14 if the file needs to end with the whitespace
#cmd = ""
for name in filenames:
    #cmd.append("")
# os.system(cmd) deal with the command here!!!
#might be easier to not add on the .txt extension on line 16?
