import network
import cpu

#make network human readable
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
    
# name cpu infor human readable
def cpu_human(dict):
    print "in cpu_human()"
    print "Number of CPUs: " + str(dict["num_cpus"])
    print "Cores per CPU: " + str(dict["num_cors_per_cpu"])
    print "Threads per Core: " + str(dict["num_threds_per_core"])
    print "CPU model: " + dict["cpu_model"]
    print "CPU Model Name: " + dict["cpu_model_name"]
    print "CPU Speed: " + dict["cpu_speed"]
    print "CPU Serial Number: " + dict["serial_number"]



