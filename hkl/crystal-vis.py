"""
Program name: crystal-vis.py
Authors: Ryan Cho and Telon Yan
Render a 3D visualization of any hkl path taken given a .int file
Draws lines between subsequent hkls
"""
import os

hklCoords = []

#Read every x,y,z coordinate for each row
file = open("hkl.txt", "r")
line = file.readline()
while line != "":
	splitLine = line.split()
	print(splitLine)
	hklCoords.append(str(float(int(splitLine[0]))) + " " + str(float(int(splitLine[1]))) + " " + str(float(int(splitLine[2]))))
	line = file.readline()

os.system("source /usr/local/HEV/.bashhev")
os.system("hev")
#os.system("cat > master.sh")
os.system("rm molecule.savg")
os.system("touch molecule.savg")

#Create a string that can be run in the shell command
for i in range(len(hklCoords)):
	os.system("savg-sphere | savg-scale 0.02 | savg-translate " + hklCoords[i] + " >> molecule.savg")

os.system("irisfly --ex molecule.savg")
