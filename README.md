# crystal-vis

Python code for visualizing crystals given a .cfl

All software used for the visualization is internal to NIST's ITL Laboratory.
All code written in a centOS 7 terminal.

## Important shell commands
Write into shell:
```shell
$ source /usr/local/HEV/.bashhev
$ hev
```
This sets up the HEV environment for .osg.

## Prerequisite work:
### For x,y,z coordinates
Highlight the desired rows with the mouse and copy.

Write into shell:
```shell
$ cat > coordinates.txt
```
Then paste into the shell and hit Ctrl + D. 
This copies the rows into a text file, which can be plugged into a python read() function.

Simply run crystal-vis.py for the desired visualization. 
### For hkl Rewards
Highlight the desired rows with the mouse and copy.

Write into shell:
```shell
$ cat > hkl.txt
```
Then paste into the shell and hit Ctrl + D. 
This copies the rows into a text file, which can be plugged into a python read() function.

There exist two files to run, one for writing the data (hkl-vis.py) and one for running the visualization (run.sh).
First run the write code (hkl-rewards-vis.py) until it terminates, then write into shell:
```shell
$ chmod +x run_count.sh
$ ./run_count.sh
```
This will output the desired visualization. 

### For hkl Counts
Copy and Paste the folder containing data for a single simulation inside of Github/crystal-vis/hkl. Make sure the .txt data files within the folder are named "epGreedyResults" + <some integer> + ".txt". 
  
Use any text editor to edit hkl-count-vis.py by changing variable 'foldername' to your data folder's name. 

Run the write code (hkl-counts-vis.py) until it terminates, then write into shell:
```shell
$ chmod +x run_count.sh
$ ./run_count.sh
```
This is currently hard coded to work for epGreedyResults data and the axes have a fixed size, but can be easily changed to it with actor-critic and q-learning data.
