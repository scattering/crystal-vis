"""
Program name: crystal-vis.py
Authors: Ryan Cho and Telon Yan
Render a 3D visualization of any given crystal given a .ctl file
Color codes individual atoms by element
"""
import os

#make a dictionary of all the elements and their respective "-r __ -g __ -b __ -a __" strings. -a may not be necessary
elementColors = {"H" : "-r 0.999 -g 0.999 -b 0.999",
                 "B" : "-r 0.999 -g 0.707 -b 0.707",
                 "C" : "-r 0.400 -g 0.400 -b 0.400",
                 "N" : "-r 0.001 -g 0.001 -b 0.999",
		 "O" : "-r 0.999 -g 0.001 -b 0.001",
                 "F" : "-r 0.500 -g 0.700 -b 0.999",
                 "AL": "-r 0.746 -g 0.650 -b 0.650",
                 "SI": "-r 0.500 -g 0.600 -b 0.600",
                 "P" : "-r 0.999 -g 0.500 -b 0.001",
                 "S" : "-r 0.700 -g 0.700 -b 0.001",
                 "CL": "-r 0.117 -g 0.938 -b 0.117",
                 "LI": "-r 0.800 -g 0.500 -b 0.999",
                 "NA": "-r 0.667 -g 0.360 -b 0.950",
                 "K" : "-r 0.560 -g 0.250 -b 0.828",
                 "RB": "-r 0.438 -g 0.180 -b 0.688",
                 "CS": "-r 0.340 -g 0.090 -b 0.560",
                 "FR": "-r 0.258 -g 0.001 -b 0.400",
                 "BE": "-r 0.758 -g 0.999 -b 0.001",
                 "MG": "-r 0.540 -g 0.999 -b 0.001",
                 "CA": "-r 0.250 -g 0.999 -b 0.001",
                 "SR": "-r 0.001 -g 0.999 -b 0.001",
                 "BA": "-r 0.001 -g 0.800 -b 0.001",
                 "RA": "-r 0.001 -g 0.500 -b 0.001",
                 "HE": "-r 0.848 -g 0.999 -b 0.999",
                 "NE": "-r 0.700 -g 0.887 -b 0.957",
                 "AR": "-r 0.500 -g 0.816 -b 0.887",
                 "KR": "-r 0.360 -g 0.719 -b 0.816",
                 "XE": "-r 0.258 -g 0.617 -b 0.688",
                 "RN": "-r 0.258 -g 0.508 -b 0.590",
                 "LU": "-r 0.001 -g 0.600 -b 0.120",
		 "PR": "-r 0.848 -g 0.999 -b 0.777",
		 "NI": "-r 0.309 -g 0.816 -b 0.309"}
rgbStrings = []
xyzCoords = []

#Read every x,y,z coordinate for each row
file = open("coordinates.txt", "r")
line = file.readline()
while line != "":
	splitLine = line.split()
	print(splitLine)
	xyzCoords.append(splitLine[3] + " " + splitLine[4] + " " + splitLine[5])
	rgbStrings.append(elementColors[splitLine[2]])
	line = file.readline()

os.system("source /usr/local/HEV/.bashhev")
os.system("hev")
#os.system("cat > master.sh")
os.system("rm molecule.savg")
os.system("touch molecule.savg")

#Create a string that can be run in the shell command
for i in range(len(rgbStrings)):
	os.system("savg-sphere | savg-scale 0.02 | savg-translate " + xyzCoords[i] + " | savg-color " + rgbStrings[i] + ">> molecule.savg")

os.system("irisfly --ex molecule.savg")
