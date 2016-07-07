#!/usr/bin/python

from subprocess import call
import subprocess

def get_pack(pack_name):
        if (len(pack_name) == 0) :
            proc = subprocess.Popen(['rpm', '-qa'], stdout=subprocess.PIPE, stdin = subprocess.PIPE)
            (out, err)= proc.communicate()
            pack_list = out.split('\n')
            return pack_list
        elif (len(pack_name) > 0):
            proc = subprocess.Popen(['rpm', '-qa', pack_name], stdout=subprocess.PIPE, stdin = subprocess.PIPE)
            (out, err)=proc.communicate()
            if (len(out) == 0):
                return "This package is not available! \n"
            else: 
                return out

