#!/usr/bin/python

import psutil
import pprint
import network
import cpu
import os
import socket
from network import get_network_info
from cpu import mch_cpu
from human_read import find_units

def get_simple_info():

	simple_info = {}
	
	try:
		cpu_count = psutil.cpu_count()
		ram = psutil.virtual_memory()
		disk = psutil.disk_usage('/')
	except:
		print "Error: Please make sure you have psutil installed, psutil info not found"
		
	network = socket.gethostbyname(socket.gethostname())

	for x in network:
		try:
			num_cpu = cpu_count
		except:
			num_cpu = "Error: Number of CPUs could not be found"
		
		try:
			total_ram = ram[0]
		except:
			total_ram = "Error: Total RAM could not be found"
		
		try:
			ip_address = network
		except:
			ip_address = "Error: IP Address could not be found"
		
		try:
			total_disk = disk[0]
		except:
			total_disk = "Error: Total HDD could not be found"
		
		try:
			hostname = os.uname()[1]
		except:
			hostname = "Error: Hostname could not be found"

		simple_info = {"CPU": num_cpu,
			       "RAM": total_ram,
			       "IP Address": ip_address,
			       "Total HDD": total_disk,
			       "Hostname": hostname}

		return simple_info

