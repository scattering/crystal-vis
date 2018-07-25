#!/bin/bash

#hev-moo hklCounts.savg > demo.iris
#hev-frameGrabberControl hklCounts.savg >> demo.iris
#irisfly --ex demo.iris 

irisfly --ex hklCounts.savg xAxis.savg yAxis.savg zAxis.savg
