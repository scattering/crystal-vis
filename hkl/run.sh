#!/bin/bash

#Displays the model made in hkl-vis.py
hev-moo hklCoords.savg > demo.iris
hev-animatorIRIS line *.savg >> demo.iris
hev-animatorIRIS -nogeometry line *.savg >> demo.iris
hev-animatorMCP test_animator.iris > animator.mcp
irisfly --ex demo.iris animator.mcp

