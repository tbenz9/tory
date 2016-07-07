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
import pack

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
    #get package list 
    sub_get_package= subparsers.add_parser('package',
                                              aliases=['pack', 'packages'],
                                              help='Get list of packages or search for one package')
    sub_get_package.add_argument('-p', '--pack', type=str, nargs='?',  action='store', dest='PACKAGE', help = 'Get list of packages or search for one package')
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
        else:
            pprint.pprint(network.get_network_info())
    if args.command == 'cpu':
        if args.j_flag:
            pprint.pprint(json.dumps(cpu.mch_cpu(), sort_keys=True, separators=(',', ': ')))
        else:
            pprint.pprint(cpu.mch_cpu())
    if args.command == 'ram':
        if args.j_flag:
            pprint.pprint(json.dumps(ram.get_ram_partitions(), sort_keys=True, separators=(',', ': ')))
        else:
	    pprint.pprint(ram.get_ram_partitions())
    if args.command == 'user':
        if args.j_flag:
            pprint.pprint(json.dumps(user.get_users(), sort_keys=True, separators=(',', ': ')))
        else:
            pprint.pprint(user.get_users())
    if args.command == 'pack':
        str_name= ''
        if args.PACKAGE:
            str_name=args.PACKAGE
        pprint.pprint(pack.get_pack(str_name))


if __name__ == '__main__':
    main()
