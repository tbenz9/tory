#!/usr/bin/python

import psutil

totalRam = psutil.virtual_memory()[0]

print(totalRam)
