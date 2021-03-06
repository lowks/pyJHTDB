###############################################################################
#
#    Copyright 2014 Johns Hopkins University
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   Contact: turbulence@pha.jhu.edu
#   Website: http://turbulence.pha.jhu.edu/
#
###############################################################################

"""
    Python tools and wrappers for the Johns Hopkins Turbulence Databases C library.
    Contact: turbulence@pha.jhu.edu
    Website: http://turbulence.pha.jhu.edu/
"""

import os
import os.path
import sys
import numpy as np
import h5py
import ctypes
import inspect
import platform

from pkg_resources import get_distribution, DistributionNotFound

try:
    _dist = get_distribution('pyJHTDB')
    # Normalize case for Windows systems
    dist_loc = os.path.normcase(_dist.location)
    here = os.path.normcase(__file__)
    if not here.startswith(os.path.join(dist_loc, 'pyJHTDB')):
        # not installed, but there is another version that *is*
        raise DistributionNotFound
except DistributionNotFound:
    __version__ = 'Please install this project with setup.py'
else:
    __version__ = _dist.version

auth_token = 'edu.jhu.pha.turbulence.testing-201302'

#__configuration_file__ = os.path.join(os.path.expanduser('~'), '/.config/pyJHTDB.cfg')
#__config__ = ConfigParser.ConfigParser()
#__config__.readfp(open(__configuration_file__))

homefolder = os.path.expanduser('~')
data_dir = '../data/'
if os.path.isfile(homefolder + '/JHTDB_user_token.txt'):
    tokenfile = open(homefolder + '/JHTDB_user_token.txt', 'r')
    auth_token = tokenfile.readline().split()[0]
    tokenfile.close()

from libJHTDB import *
from test import test_plain, test_misc, test_cutout

