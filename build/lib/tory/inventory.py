#!/usr/bin/python

import psutil
import pprint

p = psutil.disk_partitions()
disk_info = {}

def get_disk_partitions():
    count = 0
    for i in p:
        disk_info[p[count][0]] = {'name': p[count][0],
                                  'mount': p[count][1],
                                  'type': p[count][2],
                                  'total': psutil.disk_usage(p[count][count])[0],
                                  'used': psutil.disk_usage(p[count][count])[1]}
        count += 1
    return disk_info

#pprint.pprint(get_disk_partitions())
