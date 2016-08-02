#!/usr/bin/python

import psutil
import pprint

def get_simple_info():
	
	simple_info = {}
	
	cpu_count = psutil.cpu_count()
	ram = psutil.virtual_memory()

	for x in simple:
		num_cpu = cpu_count
		total_ram = ram[0]
		
		simple_info = {"CPU:" num_cpu
			      RAM: total_ram}
		
		return simple_info
