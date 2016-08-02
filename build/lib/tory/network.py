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
    addresses = psutil.net_if_addrs()
    stats = psutil.net_if_stats()
    
    dict = {}
    for name in addresses:
        mac_address = getHwAddr(name)
        ip_address = addresses[name][0][1]
        speed = stats[name][2] / 1000.0
        link = stats[name][0]
        dict[name] =  {"mac_address": mac_address, "ip_address": ip_address, \
                       "speed": speed, "link": link}
    return dict



