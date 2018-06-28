#!/bin/bash

#Displays the model made in hkl-vis.py
hev-moo hklCoords.savg lines.savg > demo.iris
irisfly --ex demo.iris
