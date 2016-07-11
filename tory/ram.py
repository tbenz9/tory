#!/usr/bin/python

import psutil
import pprint
import os
from human_read import find_units

def get_os_vers():
    f = open("/etc/redhat-release", "r")
    return f.readline().strip("\n").strip(" ")

def get_ram_partitions():

	ram = psutil.virtual_memory()

	ramOS_info = {}

	for x in ram:
		total_ram = ram[0]
		free_ram = ram[1]
		swap_space = psutil.swap_memory()[2]
		kernel_version = os.uname()[2]
		hostname = os.uname()[1]

		ramOS_info = {"total_ram": find_units(total_ram),
			      "free_ram": find_units(free_ram), 
			      "swap_space": find_units(swap_space), 
			      "os_version": get_os_vers(),
			      "kernel_version": kernel_version,
			      "hostname": hostname}
		
		return ramOS_info

