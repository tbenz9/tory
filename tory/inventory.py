#!/usr/bin/python

import psutil
import pprint
import os
import os.path
import subprocess
from subprocess import call
import fcntl
import struct
import socket
import pwd
import grp


p = psutil.disk_partitions()
disk_info = {}

def get_disks():
    count = 0
    for i in p:
        disk_info[p[count][0]] = {'name': p[count][0],
                                  'mount': p[count][1],
                                  'type': p[count][2],
                                  'total': psutil.disk_usage(p[count][count])[0],
                                  'used': psutil.disk_usage(p[count][count])[1]}
        count += 1
    return disk_info


"""This function will gather cpu information. Needs root permission
   Parameters: none
   return: dictionary"""

def get_cpu():
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
                cpu_info = {"num_cpus":psutil.cpu_count() , "num_cors_per_cpu":psutil.cpu_count()/ psutil.cpu_count(logical=False), "num_threds_per_core":num_thrds, "cpu_model":model, "cpu_model_name":mod_name, "cpu_speed":speed, "serial_number":out}

            elif (uid != 0 ):

                cpu_info = {"num_cpus":psutil.cpu_count() , "num_cors_per_cpu":psutil.cpu_count()/ psutil.cpu_count(logical=False), "num_threds_per_core":num_thrds, "cpu_model":model, "cpu_model_name":mod_name, "cpu_speed":speed, "serial_number":"Need Root!"}

            return cpu_info


#function that obtains the MAC Address 
def getHwAddr(ifname): 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15])) 
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]

def get_network():
    try:
        addresses = psutil.net_if_addrs()
        stats = psutil.net_if_stats()
    except: 
        print "psutil information not found."   #if no psutil found return error
        return "error"
    
    dict = {}
    for name in addresses:                      #for each individual value, say no ___ if not found
        try:
            mac_address = getHwAddr(name)
        except:
            mac_address = "No mac_address found"

        try:
            ip_address = addresses[name][0][1]
        except:
            ip_address = "no ip_address found"        

        try:
            speed = stats[name][2] / 1000.0
        except:
            speed = "no speed found"        

        try:
            link = stats[name][0]
        except:
            link = False        

        dict[name] =  {"mac_address": mac_address, "ip_address": ip_address, \
                        "speed": speed, "link": link}
    return dict



def get_os_vers(): # defined function to return OS Version from command
     
	if os.path.exists("/etc/redhat-release"): # error checking, checking to see if OS version is found within file
		f = open("/etc/redhat-release", "r")
        	return f.readline().strip("\n").strip(" ")
	else:
		print "Error: OS Version not found" # if file is not found

def get_ram(): # defined function to get all the RAM info
	
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

def get_pack(pack_name=''):
        # If no argument is given I will list all packages
        if (len(pack_name) == 0) :
            proc = subprocess.Popen(['rpm', '-qa'], stdout=subprocess.PIPE, stdin = subprocess.PIPE)
            (out, err)= proc.communicate()
            pack_list = out.split('\n')
            pack_count = 0
            for package in pack_list:
                if len(package) >= 1 :
                    pack_count = pack_count + 1
            print ("We hav " + str(pack_count)+ " packages")
            return pack_list
        # This will search for the package givin in argument
        elif (len(pack_name) > 0):
            proc = subprocess.Popen(['rpm', '-qa', pack_name], stdout=subprocess.PIPE, stdin = subprocess.PIPE)
            (out, err)=proc.communicate()
            if (len(out) == 0):
                return "This package is not available! \n"
            else:
                return out


def get_user():
    dict = {}
    #find current users and add to the the dictionary
    try:    
        users = psutil.users()

        names = []
        for user in users:
            names.append(user[0])
        dict['current_users'] = names
    except:
        print "Current Users not found"

    #find all users
    try:    
        all_users = []
        for p in pwd.getpwall():
            all_users.append(p[0])
        dict['all_users'] = all_users
    except:
        print "All Users not found"


    #make a dict of the groups of all the users
    try:
        groups = {}
        for p in pwd.getpwall():
            groups[p[0]] = grp.getgrgid(p[3])[0] 
        dict['groups'] = groups
    except:
        print "Groups not found"

    return dict


def get_simple():

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

