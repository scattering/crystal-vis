"""
Program name: crystal-vis.py
Authors: Ryan Cho and Telon Yan
Render a 3D visualization of any given crystal given a .ctl file
Color codes individual atoms by element
"""
import os

#make a dictionary of all the elements and their respective "-r __ -g __ -b __ -a __" strings. -a may not be necessary
elementColors = {"H" : "-r 1 -g 1 -b 1",
		 "O" : "-r 0.99 -g 0.001 -b 0.001",
		 "PR": "-r 0.8 -g 0.8 -b 0.1",
		 "NI": "-r 0.5 -g 0.5 -b 0.5"}
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
