import network

def net_human(dict):
    print "in net_human()"
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
    



