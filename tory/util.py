import argparse
import ConfigParser
import getopt
import math
import os
import sys
from collections import OrderedDict
from ConfigParser import (
    NoSectionError,
    DuplicateSectionError,
    NoOptionError,
    MissingSectionHeaderError,
    ParsingError
)

ALIASES = {}

def print_nicely(obj):
    if type(obj) == dict:
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print k
                print_nicely(v)
            else:
                print '%s : %s' % (k, v)
    elif type(obj) == list:
        for v in obj:
            if hasattr(v, '__iter__'):
                print_nicely(v)
            else:
                print v
    else:
        print obj

#converts from bytes to largest unit, returns a string of #units
def find_units(num):
    counter = 0
    while (num > 999):
        num = num / 1000.0
        counter = counter + 1
    num = round(num, 2)
    if counter == 0:
       return str(num) + 'B'
    elif counter == 1:
       return str(num) + 'KB'
    elif counter == 2:
       return str(num) + 'MB'
    elif counter == 3:
       return str(num) + 'GB'
    elif counter == 4:
       return str(num) + 'TB'
    elif counter == 5:
       return str(num) + 'PB'
    elif counter == 6:
       return str(num) + 'EB'
    else:
       return str(num)

# class to allow for aliases for argparse positional arguments
#### code credit to https://gist.github.com/sampsyo/471779 ####
class AliasedSubParsersAction(argparse._SubParsersAction):
    
    class _AliasedPseudoAction(argparse.Action):
        def __init__(self, name, aliases, help):
            dest = name
            # uncomment for aliases to show up in help
            #if aliases:
            #    dest += ' (%s)' % ','.join(aliases)
            sup = super(AliasedSubParsersAction._AliasedPseudoAction, self)
            sup.__init__(option_strings=[], dest=dest, help=help) 

    def add_parser(self, name, **kwargs):
        if 'aliases' in kwargs:
            aliases = kwargs['aliases']
            del kwargs['aliases']
        else:
            aliases = []

        parser = super(AliasedSubParsersAction, self).add_parser(name, **kwargs)

        # Make the aliases work.
        for alias in aliases:
            self._name_parser_map[alias] = parser
            ALIASES[alias] = name

        # Make the help text reflect them, first removing old help entry.
        if 'help' in kwargs:
            help = kwargs.pop('help')
            self._choices_actions.pop()
            pseudo_action = self._AliasedPseudoAction(name, aliases, help)
            self._choices_actions.append(pseudo_action)

        return parser


class AliasedArgumentParser(argparse.ArgumentParser):

    def __init__(self, **kwargs):
        super(AliasedArgumentParser, self).__init__(**kwargs)
        self.register('action', 'parsers', AliasedSubParsersAction)
