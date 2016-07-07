import sys
import os
import pprint

# Hack to get the CWD until we build a real python package
sys.path.append(os.getcwd().split('tory')[0]+"tory/tory/")

import util
from util import AliasedArgumentParser, AliasedSubParsersAction
import argparse
import inventory
import network
import cpu
import ram
import user
import json
<<<<<<< HEAD
import pack
=======
import human_read
import database
import simple
>>>>>>> cf53dbf28319ecd2856b8595cc7bd5ff3692e7b7

def parse_input():
    parser = AliasedArgumentParser(prog='PROG',
                                   usage="%(prog)s [OPTION] CMD...",
                                   prefix_chars="-")
    parser.register('action', 'parsers', AliasedSubParsersAction)

    # commands following tory keyword (e.g. 'tory disks ...')
    subparsers = parser.add_subparsers(title='commands',
                                       metavar='CMD',
                                       dest='command')
    # This is just a sample flag, it doesn't do anything yet.
    parser.add_argument('-m',
                        '--max-records',
                        action='store',
                        dest='max_records',
                        default=200,
                        help='Maximum number of records to show')
    # This is the json flag
    parser.add_argument('-j',
                        '--json',
                        action='store_true',
                        dest='j_flag',
                        help='convert to json')

    # This is the human readable flag
    parser.add_argument('-r',
                        '--read',
                        action='store_true',
                        dest='r_flag',
                        help='convert to human readable')

    # This is the database flag
    parser.add_argument('-d',
                        '--database',
                        action='store_true',
                        dest='d_flag',
                        help='send to database')

    # get disks
    sub_get_disks = subparsers.add_parser('disks',
                                            aliases=['disk'],
                                            help='Get info on disks')
    # get network
    sub_get_network = subparsers.add_parser('network',
                                              aliases=['net'],
                                              help='Get info on network')
    #get cpu
    sub_get_cpu = subparsers.add_parser('cpu', 
                                              aliases=['cpu'], 
                                              help='Get info on CPU')
    #get ramOS
    sub_get_ram = subparsers.add_parser('ram',
		    			      aliases=['ram'],
					      help='Get info on RAM')
    #get user
    sub_get_user = subparsers.add_parser('user',
                                              aliases=['users'],
                                              help='Get info on users')
<<<<<<< HEAD
    #get package list 
    sub_get_package= subparsers.add_parser('package',
                                              aliases=['pack', 'packages'],
                                              help='Get list of packages or search for one package')
    sub_get_package.add_argument('-p', '--pack', type=str, nargs='?',  action='store', dest='PACKAGE', help = 'Get list of packages or search for one package')
=======
    #get simple
    sub_get_simple = subparsers.add_parser('simple',
		    			      aliases=['simple'],
					      help='Get simple info')

>>>>>>> cf53dbf28319ecd2856b8595cc7bd5ff3692e7b7
    args = parser.parse_args()
    return args

def main():
    args = parse_input()
    if args.command == 'disks':
        if args.j_flag:
            pprint.pprint(json.dumps(inventory.get_disk_partitions(), sort_keys=True, separators=(',', ': ')))
        else: 
            pprint.pprint(inventory.get_disk_partitions())
    if args.command == 'network':
        if args.j_flag:
            pprint.pprint(json.dumps(network.get_network_info(), sort_keys=True, separators=(',', ': ')))
        elif args.r_flag:
            human_read.net_human(network.get_network_info())
        elif args.d_flag:
            database.add_network_to_database(network.get_network_info())
            database.get_network_from_database()
        else:
            pprint.pprint(network.get_network_info())
    if args.command == 'cpu':
        if args.j_flag:
            pprint.pprint(json.dumps(cpu.mch_cpu(), sort_keys=True, separators=(',', ': ')))
        elif args.r_flag:
            human_read.cpu_human(cpu.mch_cpu())
        else:
            pprint.pprint(cpu.mch_cpu())
    if args.command == 'ram':
        if args.j_flag:
            pprint.pprint(json.dumps(ram.get_ram_partitions(), sort_keys=True, separators=(',', ': ')))
        elif args.r_flag:
            human_read.ram_human(ram.get_ram_partitions())
        else:
	    pprint.pprint(ram.get_ram_partitions())
    if args.command == 'user':
        if args.j_flag:
            pprint.pprint(json.dumps(user.get_users(), sort_keys=True, separators=(',', ': ')))
        elif args.r_flag:
            human_read.users_human(user.get_users())
        else:
            pprint.pprint(user.get_users())
<<<<<<< HEAD
    if args.command == 'pack':
        str_name= ''
        if args.PACKAGE:
            str_name=args.PACKAGE
        pprint.pprint(pack.get_pack(str_name))

=======
    if srgs.command == 'simple':
	if args.j_flag:
	    pprint.pprint(json.dumps(simple.get_simple_info(), sort_keys=True, separators=(',', ': ')))
        elif args.r_flag:
            human_read.simple_human(simple.get_simple_info())					         else:
	    pprint.pprint(user.get_simple_info())
>>>>>>> cf53dbf28319ecd2856b8595cc7bd5ff3692e7b7

if __name__ == '__main__':
    main()
