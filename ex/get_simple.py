#!/usr/bin/python

import psutil
import pprint
import network
import os

def get_simple_info():
	
	simple_info = {}
	
	cpu_count = psutil.cpu_count()
	ram = psutil.virtual_memory()
	network = psutil.net_if_addrs()
	disk = psutil.disk_usage('/')

	for x in simple:
		num_cpu = cpu_count
		total_ram = ram[0]
		ip_address = get_network_info(addresses[0][1])
		ip_address = get_network_info("ip_address")
		ip_address = network[0][1]
		total_disk = disk[0]
		hostname = os.uname()[1]

		simple_info = {"CPU": num_cpu,
			       "RAM": total_ram,
			       "IP Address": ip_address,
			       "Total HDD": total_disk,
			       "Hostname": hostname}

		return simple_info

pprint.pprint(get_simple_info())
