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
