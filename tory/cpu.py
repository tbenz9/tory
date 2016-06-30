#!/usr/bin/python

import psutil
from subprocess import call
import subprocess

def mch_cpu():
        proc = subprocess.Popen('lscpu', stdout=subprocess.PIPE)
        output = proc.stdout.read()
	outlist = output.split('\n')
	num_thrds = int(filter(str.isdigit, outlist[5]))
	model = outlist[0].split(' ')[-1]
	mod_name = outlist[12][23:]
	speed = outlist[14].split(' ')[-1]
	proc2 = subprocess.Popen(["dmidecode", "-s", "system-serial-number"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
	(out, err) = proc2.communicate()
        cpu_info = {"num_cpus":psutil.cpu_count() , "num_cors_per_cpu":psutil.cpu_count()/ psutil.cpu_count(logical=False), "num_threds_per_core":num_thrds, "cpu_model":model, "cpu_model_name":mod_name, "cpu_speed":speed, "serial_number":out}
	
	return cpu_info



