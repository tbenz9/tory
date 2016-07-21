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
		print "Error: OS Version not found" # if file is not found

def get_ram_partitions(): # defined function to get all the RAM info
	
	try: # tries and ensures that psutil is found and installed
		ram = psutil.virtual_memory() # python psutil package that gathers information on memory
	except: # if psutil is not found, returns error
		print "Error: Please make sure your have psutil installed, psutil information not found"
	
	ramOS_info = {} # RAM dictionary

    	for x in ram:
		
		try:	
			total_ram = ram[0]
		except:
			total_ram = "Error: Total RAM not found"
	
		try:
			free_ram = ram[1]
		except:
			free_ram = "Error: Free RAM not found"
	
		try:
			swap_space = psutil.swap_memory()[2]
		except:
			swap_space = "Error: Swap Space not found"
	
		try:
			kernel_version = os.uname()[2]
		except:
			kernel_version = "Error: Kernel Version not found"
	
		try:
			hostname = os.uname()[1]
		except:
			hostname = "Error: Hostname not found"

		ramOS_info = {"total_ram": total_ram,
			      "free_ram": free_ram, 
			      "swap_space": swap_space, 
			      "os_version": get_os_vers(),
			      "kernel_version": kernel_version,
			      "hostname": hostname}
		
		return ramOS_info # returns RAM dictionary
