import network
import cpu

#make network human readable, dict is a dictionary from the output of get_network_info()
def net_human(dict):
    for name in dict:
        print "name: " + name
        print "\t MAC address: " + dict[name]["mac_address"]
        print "\t IP address : " + dict[name]["ip_address"]
        if (dict[name]["speed"] == 0):
            print "\t Speed: Unavailable"
        else:
            print "\t Speed: " + find_units((dict[name]["speed"] * (10 ** 9)))
        if (dict[name]["link"] == True):
            print "\t Link: Up"
        else:
            print "\t Link: Up"
        print ""
    
#cpu info in human readable, dict is a dictionary from the output of mch_cpu()

def cpu_human(dict):
    print "Number of CPUs: " + str(dict["num_cpus"])
    print "Cores per CPU: " + str(dict["num_cors_per_cpu"])
    print "Threads per Core: " + str(dict["num_threds_per_core"])
    print "CPU model: " + dict["cpu_model"]
    print "CPU Model Name: " + dict["cpu_model_name"]
    print "CPU Speed: " + dict["cpu_speed"]
    print "CPU Serial Number: " + dict["serial_number"]

#disk info in  human readable, dict is a dictionary from the output of get_disk_partitions()
def ram_human(dict):
    print "Total RAM: " + find_units(dict["total_ram"])
    print "Free RAM: " + find_units(dict["free_ram"])
    print "Swap Space: " + find_units(dict["swap_space"])
    print "OS Version: " + dict["os_version"]
    print "Kernel Version: " + dict["kernel_version"]
    print "Hostname: " + dict["hostname"]

#user info in human readable, dict is a dictionary from the output of get_users()
def users_human(dict):
    print "Current Users: ",
    print ', '.join(dict['current_users'])
    print "\nAll Users:"
    print '%-12s\t%-12s' % ('Name:', 'Group:')
    for name in dict['groups']:
        print '%-12s\t%-12s' % (name, dict['groups'][name])

def find_units(num):
    counter = 0
    while (num > 999):
        num = num / 1000.0
        counter = counter + 1
    num = round(num, 2)
    if counter == 0:
       return str(num) + 'B'
    elif counter == 1:
       return str(num) + 'KB'
    elif counter == 2:
       return str(num) + 'MB'
    elif counter == 3:
       return str(num) + 'GB'
    elif counter == 4:
       return str(num) + 'TB'
    elif counter == 5:
       return str(num) + 'PB'
    elif counter == 6:
       return str(num) + 'EB'
    else:
       return str(num)

