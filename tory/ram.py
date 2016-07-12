#!/usr/bin/python

import psutil
import pprint
import os
import os.path
from human_read import find_units

def get_os_vers(): # defined function to return OS Version from command
    
    

# testing out error checking 
	if os.path.exists("/etc/redhat-release"):
		f = open("/etc/redhat-release", "r")
        	return f.readline().strip("\n").strip(" ")
	else:
		print "There is no such file"

def get_ram_partitions(): # defined function to get all the RAM info

	ram = psutil.virtual_memory() # python psutil package that gathers information on memory

	ramOS_info = {} # RAM dictionary

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
		
		return ramOS_info # returns RAM dictionary
