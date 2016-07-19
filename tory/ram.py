#!/usr/bin/python

import psutil
import pprint
import os
import os.path
from human_read import find_units

def get_os_vers(): # defined function to return OS Version from command
     
	if os.path.exists("/etc/redhat-release"): # error checking, checking to see if OS version is found within file
		f = open("/etc/redhat-release", "r")
        	return f.readline().strip("\n").strip(" ")
	else:
		print "There is no such file" # if file is not found

def get_ram_partitions(): # defined function to get all the RAM info
	
	try: # tries and ensures that psutil is found and installed
		ram = psutil.virtual_memory() # python psutil package that gathers information on memory
	except: # if psutil is not found, returns error
		print "Please make sure your have psutil installed, psutil information not found"
	
	ramOS_info = {} # RAM dictionary

	for x in ram:
		total_ram = ram[0]
		free_ram = ram[1]
		swap_space = psutil.swap_memory()[2]
		kernel_version = os.uname()[2]
		hostname = os.uname()[1]

		ramOS_info = {"total_ram": total_ram,
			      "free_ram": free_ram, 
			      "swap_space": swap_space, 
			      "os_version": get_os_vers(),
			      "kernel_version": kernel_version,
			      "hostname": hostname}
		
		return ramOS_info # returns RAM dictionary
