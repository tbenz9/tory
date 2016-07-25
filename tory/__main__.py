import sys
import os
import pprint

import util
from util import AliasedArgumentParser, AliasedSubParsersAction
import argparse
import inventory
import json
import database

# Hack to get the CWD until we build a real python package
sys.path.append(os.getcwd().split('tory')[0]+"tory/tory/")


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
    # This is the show database flag
    parser.add_argument('-s',
                        '--show_database',
                        action='store_true',
                        dest='s_flag',
                        help='show contents in database')

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
    #get simple
    sub_get_simple = subparsers.add_parser('simple',
		    			      aliases=['simple'],
					      help='Get info on simple')
    #get package list 
    sub_get_package= subparsers.add_parser('package',
                                              aliases=['pack', 'packages'],
                                              help='Get list of packages or search for one package')
    sub_get_package.add_argument('-p', '--pack', type=str, nargs='?',  action='store', dest='PACKAGE', help = 'Get list of packages or search for one package')

    args = parser.parse_args()
    return args

def main():
    args = parse_input() 

    output = getattr(inventory, 'get_'+args.command)()
   
    if args.j_flag:
        pprint.pprint(json.dumps(output, sort_keys=True, separators=(',', ': ')))
    else:
        util.print_nicely(output)

#        elif args.d_flag:
#            database.add_ram_to_database(ram.get_ram_partitions())
#        elif args.s_flag:
#            database.get_from_database("ram")


if __name__ == '__main__':
    main()
