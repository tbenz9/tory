import network
import cpu

#make network human readable, dict is a dictionary from the output of get_network_info()
def net_human(dict):
    for name in dict:
        print "name: " + name
        print "\t MAC address: " + dict[name]["mac_address"]
        print "\t IP address : " + dict[name]["ip_address"]
        print "\t Speed: " + str(dict[name]["speed"]) + "GB"
        if (dict[name]["link"] == True):
            print "\t Link: Up"
        else:
            print "\t Link: Up"
        print ""
    
#cpu info in human readable, dict is a dictionary from the output of mch_cpu()

def cpu_human(dict):
    print "in cpu_human()"
    print "Number of CPUs: " + str(dict["num_cpus"])
    print "Cores per CPU: " + str(dict["num_cors_per_cpu"])
    print "Threads per Core: " + str(dict["num_threds_per_core"])
    print "CPU model: " + dict["cpu_model"]
    print "CPU Model Name: " + dict["cpu_model_name"]
    print "CPU Speed: " + dict["cpu_speed"]
    print "CPU Serial Number: " + dict["serial_number"]

#disk info in  human readable, dict is a dictionary from the output of get_disj_partitions()
def ram_human(dict):
    print "Total RAM: " + str(dict["total_ram"])
    print "Free RAM: " + str(dict["free_ram"])
    print "Swap Space: " + str(dict["swap_space"])
    print "OS Version: " + dict["os_version"]
    print "Kernel Version: " + dict["kernel_version"]
    print "Hostname: " + dict["hostname"]


