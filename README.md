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
### For hkl's
Highlight the desired rows with the mouse and copy.

Write into shell:
```shell
$ cat > hkl.txt
```
Then paste into the shell and hit Ctrl + D. 
This copies the rows into a text file, which can be plugged into a python read() function.

There exist two files to run, one for writing the data (hkl-vis.py) and one for running the visualization (run.sh).
First run the write code (hkl-vis.py) until it terminates, then write into shell:
```shell
$ chmod +x run.sh
$ ./run.sh
```
This will output the desired visualization. 
