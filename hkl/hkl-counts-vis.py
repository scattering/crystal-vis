"""
Program name: hkl-counts-vis.py
Authors: Ryan Cho and Telon Yan

Makes .savg files for 3D Visualization of hkl points and how often
they are visited over some number of simulations
"""

import os

os.system("source /usr/local/HEV/.bashhev")
os.system("hev")				#for some reason this keeps yelling at us
os.system("rm *.savg")
os.system("touch khlCounts.savg")

#List of hkls as Strings, e.g. ["1 1 1", "1 3 1", "1 3 3"]
hklCounts = {}
NUM_FILES = 500

print("Reading...")

sxtal_file = open("prnio.int", "r")

#Gets rid of the header
line = sxtal_file.readline()
line = sxtal_file.readline()
line = sxtal_file.readline()

print(line)

sxtal_hkls = {}
while (line != ""):
    splitLine = line.split()
    print(splitLine)
    sxtal_hkls[splitLine[0] + " " + splitLine[1] + " " + splitLine[2]] = 0
    line = sxtal_file.readline()

sxtal_file.close()

for i in range(NUM_FILES):
    file = open("epGreedyResults" + str(i) +".txt", "r")			#Whatever filename your data is in

    #gets rid of the first line of the file (headers)
    line = file.readline()

    #read in the first line of data (the second line of the file, for the while loop)
    line = file.readline()

    #read the rest of the file, line by line
    while (line != ""):
	#Split up the line into the data components
	splitLine = line.split()
	print(splitLine)

	#Get data from the line into our lists (list function is written at instantiation)
	hkl = splitLine[0] + " " + splitLine[1] + " " + splitLine[2]
	sxtal_hkls[hkl] += 1

	#Read in the next line
	line = file.readline()

	file.close()

print("Generating model...")

#Create a string that can be run in the shell command
for i in sxtal_hkls:
    #Create the spheres (HKL points)
    os.system("savg-sphere | savg-scale 0.2 | savg-translate " + hklCoords[i] + " | savg-color -r 1  -g " + str(1.0 - sxtal_hkls[i]/NUM_FILES) + " -b " + str(1.0 - sxtal_hkls[i]/NUM_FILES) + " >> hklCounts.savg")

print("Done")
