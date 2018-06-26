"""
Program name: crystal-vis.py
Authors: Ryan Cho and Telon Yan
Render a 3D visualization of any given crystal given a .ctl file
Color codes individual atoms by element
"""
import os

#make a dictionary of all the elements and their respective "-r __ -g __ -b __ -a __" strings. -a may not be necessary
elementColors = {"H" : "-r 1 -g 1 -b 1"}
rgbStrings = []
xyzCoords = []

#Read every x,y,z coordinate for each row
file = open("file.txt", "r")
line = file.readline()
while line != "":
	splitLine = line.split()
	print(splitLine)
	xyzCoords.append(str(splitLine[3] + " " + splitLine[4] + " " + splitLine[5]))
	currentRGBString = elementColors[splitLine[1]]
	rgbStrings.append(currentRGBString)
	line = file.readline()

os.system("source /usr/local/HEV/.bashhev")
os.system("hev")
os.system("cat > master.sh")

#Create a string that can be run in the shell command
for i in range(len(rgbStrings)):
	os.system("savg-sphere | savg-scale 0.02 | savg-translate " + xyzCoords[i] + " | savg-color " + rgbStrings[i])
