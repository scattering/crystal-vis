"""
Program name: crystal-vis.py
Authors: Ryan Cho and Telon Yan
Render a 3D visualization of any hkl path taken given a .int file
Draws lines between subsequent hkls
"""
import os

os.system("source /usr/local/HEV/.bashhev")
os.system("hev")
os.system("rm molecule.savg")
os.system("touch molecule.savg")
os.system("rm lines.savg")

#List of Strings, e.g. ["1 1 1", "1 3 1", "1 3 3"]
hklCoords = []

#Read every x,y,z coordinate for each row
file = open("hkl.txt", "r")
file2 = open("lines.savg", "w")

line = file.readline()

while line != "":
	splitLine = line.split()
	print(splitLine)
	hklCoords.append(str(float(int(splitLine[0]))) + " " + str(float(int(splitLine[1]))) + " " + str(float(int(splitLine[2]))))
	line = file.readline()


#Create a string that can be run in the shell command
for i in range(len(hklCoords)):
	#For the spheres/HKL points
	os.system("savg-sphere | savg-scale 0.2 | savg-translate " + hklCoords[i] + " >> molecule.savg")

	#For the paths between HKL points
	if (i != 0):
		file2.write("lines\n")
		file2.write(hklCoords[i-1] + "\n" + hklCoords[i] + "\n")

file.close()
file2.close()
