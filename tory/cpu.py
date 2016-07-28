#!/usr/bin/python

import os
import psutil
from subprocess import call
import subprocess


def mch_cpu():
            """
            This function will gather cpu information. 
            Needs root permission.
            Parameters: none
            return: dictionary
            """

            uid = os.getuid()
            proc = subprocess.Popen('lscpu', stdout=subprocess.PIPE)
            output = proc.stdout.read()
            outlist = output.split('\n')
            num_thrds = int(filter(str.isdigit, outlist[5]))
            model = outlist[0].split(' ')[-1]
            mod_name = outlist[12][23:]
            speed = outlist[14].split(' ')[-1]
            if (uid == 0):
                proc2 = subprocess.Popen(["dmidecode", "-s", "system-serial-number"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                (out, err) = proc2.communicate()
                cpu_info = {"num_cpus":psutil.cpu_count() , "num_cores_per_cpu":psutil.cpu_count()/ psutil.cpu_count(logical=False), "num_threads_per_core":num_thrds, "cpu_model":model, "cpu_model_name":mod_name, "cpu_speed":speed, "serial_number":out}

            elif (uid != 0 ):

                cpu_info = {"num_cpus":psutil.cpu_count() , "num_cores_per_cpu":psutil.cpu_count()/ psutil.cpu_count(logical=False), "num_threads_per_core":num_thrds, "cpu_model":model, "cpu_model_name":mod_name, "cpu_speed":speed, "serial_number":"Need Root!"}

            return cpu_info



