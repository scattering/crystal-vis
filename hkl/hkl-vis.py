"""
Program name: crystal-vis.py
Authors: Ryan Cho and Telon Yan
Makes .savg files for 3D Visualization of hkl points and the agent path 
from a given .txt file with h k l values and cumulative reward
"""
import os

os.system("source /usr/local/HEV/.bashhev")
os.system("hev")
os.system("rm molecule.savg")
os.system("touch molecule.savg")
os.system("rm lines.savg")

#List of Strings, e.g. ["1 1 1", "1 3 1", "1 3 3"]
hklCoords = []
rewardList = []

#Read every x,y,z coordinate for each row
file = open("hkl2.txt", "r")
file2 = open("lines.savg", "w")


#gets rid of the first line (headers)
line = file.readline()

#read in the first data line
line = file.readline()

#read the rest of the file, line by line
while line != "":
	
	#Split up the line into the data components
	splitLine = line.split()
	print(splitLine)

	#Get data from the line into our lists
	hklCoords.append(splitLine[0] + " " + splitLine[1] + " " + splitLine[2])
	rewardList.append(float(splitLine[4]))

	#Whoa it's the next line
	line = file.readline()


#Scaling reward to determine color gradient
rewardListA = []
for i in range(len(rewardList)):
	rewardListA.append(abs(rewardList[i]))
maxR = max(rewardListA)
print(rewardList)

#Create a string that can be run in the shell command
for i in range(len(hklCoords)):
	#For the spheres/HKL points
	scaledReward = 0.5*rewardList[i]

	#The colors actually are supposed to be on the lines, not the atoms!!
	os.system("savg-sphere | savg-scale 0.2 | savg-translate " + hklCoords[i] + \
		  " | savg-color -r " + str(0.5 + scaledReward/maxR) + " -g 0 -b " + str(0.5 - scaledReward/maxR) + " >> molecule.savg")

	#For the paths between HKL points
	if (i != 0):
		file2.write("lines\n")
		file2.write(hklCoords[i-1] + "\n" + hklCoords[i] + "\n")

file.close()
file2.close()
