# -*- coding: utf-8 -*-
# Copyright © 2011 Carl Chenet <chaica@ohmytux.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#Parse the configurations
'''Parse the configurations'''

import sys
from configparser import ConfigParser
from configparser import ParsingError, NoSectionError, NoOptionError
import os

class Configurations:
    '''Retrieve the different configurations'''

    def __init__(self, __confpath):
        '''The constructor of the Configurations class.

        __confpath -- the path to the directory with the configuration files

        '''
        self.__configs = {}
        self.__parse_configurations(__confpath)

    def __parse_configurations(self, __confpath):
        '''Parse the different configurations'''
        __confs = [__file for __file in os.listdir(__confpath) 
            if __file.endswith('.conf')]
        for __conf in __confs:
            __currentconf = {}
            try:
                __config = ConfigParser()
                with open(os.path.join(
                    '/'.join([__confpath, __conf])), 'r') as __file:
                    __config.read_file(__file)
                # Common information for the backups
                ### The type of the backups
                __currentconf['type'] = __config.get('main', 'type')
                # Common information for the archives
                ### The archive path
                __confsettings = [{'main': 'path'},
                ### The list of the expected files in the archive
                {'main': 'files_list'}
                ]
                for __element in __confsettings:
                    __key, __value = __element.popitem()
                    if __config.has_option(__key, __value):
                        __currentconf[__value] = __config.get(
                                                    __key, __value)
                    else:
                        __currentconf[__value] = __config.set(
                                                    __key, __value, '')
                # Checking the information
                ### Check the paths in the configuration
                __pathnames = ("__currentconf['path']")
                for __pathname in __pathnames:
                    __path = getattr(self, __pathname, None)
                    if __path:
                        __bckpath = os.path.abspath(__path)
                        if not os.path.exists(__bckpath):
                            print('{} does not exist.'.format(__bckpath))
                            sys.exit(1)
                self.__configs[__config.get('main', 'name')] = __currentconf
            except (ParsingError, NoSectionError, NoOptionError) as __err:
                print(__err)
                sys.exit(1)

    @property
    def configs(self):
        '''Return the different configurations parameters'''
        return self.__configs