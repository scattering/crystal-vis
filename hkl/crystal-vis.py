"""
Program name: crystal-vis.py
Authors: Ryan Cho and Telon Yan
Render a 3D visualization of any hkl path taken given a .int file
Draws lines between subsequent hkls
"""
import os

#List of Strings, e.g. ["1 1 1", "1 3 1", "1 3 3"]
hklCoords = []
#List of float lists (h, k, l)
hklRealCoords = []

#Read every x,y,z coordinate for each row
file = open("hkl.txt", "r")
file2 = open("lines.txt", "w")

line = file.readline()

while line != "":
	splitLine = line.split()
	print(splitLine)
	hklRealCoords.append([float(int(splitLine[0])), float(int(splitLine[1])), float(int(splitLine[2]))])
	hklCoords.append(str(float(int(splitLine[0]))) + " " + str(float(int(splitLine[1]))) + " " + str(float(int(splitLine[2]))))
	line = file.readline()

os.system("source /usr/local/HEV/.bashhev")
os.system("hev")
#os.system("cat > master.sh")
os.system("rm molecule.savg")
os.system("touch molecule.savg")
os.system("rm lines.savg")
os.system("touch lines.savg")

#write "lines" into this file
#os.system("lines > lines.savg")
#file2.write("lines\n")

#Create a string that can be run in the shell command
for i in range(len(hklCoords)):
	os.system("savg-sphere | savg-scale 0.2 | savg-translate " + hklCoords[i] + " >> molecule.savg")
	#file2.write(hklRealCoords[i][0] + " " + hklRealCoords[i][1] + " " + hklRealCoords[i][2])
	if (i % 2 == 0):
		file2.write("lines\n")
	file2.write(hklCoords[i] + "\n")

os.system("irisfly --ex molecule.savg")
#os.system("irisfly --ex lines.txt")

file.close()
file2.close()
