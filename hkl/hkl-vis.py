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
rewardChangeList = []

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
	rewardChangeList.append(splitLine[3])
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
	if (rewardList[i] > 0):
		os.system("savg-sphere | savg-scale 0.2 | savg-translate " + hklCoords[i] + \
			  " | savg-color -r 1  -g " + str(1.0 - rewardListA[i]/maxR) + " -b " + str(1.0 - rewardListA[i]/maxR) + " >> molecule.savg")
	else:
		os.system("savg-sphere | savg-scale 0.2 | savg-translate " + hklCoords[i] + \
                          " | savg-color -r " + str(1.0 - rewardListA[i]/maxR) + " -g " + str(1.0 - rewardListA[i]/maxR) + " -b 1 >> molecule.savg")

	#For the paths between HKL points
	if (i != 0):
		file2.write("lines\n")
		#change in reward
		if (rewardChangeList[i] == "0.5"):
			file2.write(hklCoords[i-1] + " 1.0 0.4 0.0 1.0 \n" + hklCoords[i] + " 1.0 0.4 0.0 1.0 \n")
		else:
			file2.write(hklCoords[i-1] + " 0.0 1.0 0.0 1.0 \n" + hklCoords[i] + " 0.0 1.0 0.0 1.0 \n")

file.close()
file2.close()
