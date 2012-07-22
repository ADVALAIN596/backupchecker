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

# Analyze the type of the backup to produce the list
'''Analyze the type of the backup to produce the list'''

import logging
import os.path

from brebis.generatelist.generatelistforbzip2 import GenerateListForBzip2
from brebis.generatelist.generatelistforlzma import GenerateListForLzma
from brebis.generatelist.generatelistforgzip import GenerateListForGzip
from brebis.generatelist.generatelistfortar import GenerateListForTar
from brebis.generatelist.generatelistfortree import GenerateListForTree
from brebis.generatelist.generatelistforzip import GenerateListForZip

class ListType(object):
    '''The ListType class'''

    def __init__(self, __arcpaths):
        '''The constructor for the ListType class.
        '''
        self.__main(__arcpaths)

    def __main(self, __arcpaths):
        '''Main for ListType class'''
        for __arcpath in __arcpaths:
            # generate a list of files for a tree
            if os.path.isdir(__arcpath):
                __bck = GenerateListForTree(__arcpath)
            # generate a list of files for a tar.gz/bz2 archive
            elif __arcpath.lower().endswith('.tar') or\
                    __arcpath.lower().endswith('.tar.gz') or\
                    __arcpath.lower().endswith('.tar.bz2') or\
                    __arcpath.lower().endswith('.tgz') or\
                    __arcpath.lower().endswith('.tbz2'):
                __bck = GenerateListForTar(__arcpath)
            # generate a list of files for a gzip archive
            elif __arcpath.lower().endswith('.gz'):
                __bck = GenerateListForGzip(__arcpath)
            # generate a list of files for a bzip2 archive
            elif __arcpath.lower().endswith('.bz2'):
                __bck = GenerateListForBzip2(__arcpath)
            # generate a list of files for a lzma archive
            elif __arcpath.lower().endswith('.xz'):
                __bck = GenerateListForLzma(__arcpath)
            # generate a list of files for a zip archive
            elif __arcpath.lower().endswith('.zip'):
                __bck = GenerateListForZip(__arcpath)
            # A MESSAGE RESUMING OPERATION FOR GENERATING THE LIST OF FILES IS MISSING HERE

