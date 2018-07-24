#!/bin/bash

hev-moo hklCounts.savg > demo.iris
hev-frameGrabberControl hklCounts.savg >> demo.iris
irisfly --ex demo.iris 
