import psutil
import socket
import fcntl
import struct

#function that obtains the MAC Address 
def getHwAddr(ifname): 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15])) 
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]

def get_network_info():
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


