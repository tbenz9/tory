#!/usr/bin/python

from subprocess import call
import subprocess

def get_pack(pack_name ):
        """:
        If no package name is given, this will list all packages.
        otherwise, it will show the package.
 
        :type pack_name: string
        :param pack_name: package name
        """
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

