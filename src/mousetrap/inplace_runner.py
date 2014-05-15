#!/usr/bin/python

# MouseTrap
#
# Copyright 2009 Flavio Percoco Premoli
#
# This file is part of mouseTrap.
#
# MouseTrap is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License v2 as published
# by the Free Software Foundation.
#
# mouseTrap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with mouseTrap.  If not, see <http://www.gnu.org/licenses/>.

# This script performs some clean up and will run mousetrap.  It will also
# rerun mousetrap if it detects that mousetrap died an unnatural death.
# IMPORTANT: Parts of this script have been taken from the Orcas launch script. Thanks!!

#__id__        = "$Id$"
#__version__   = "$Revision$"
#__date__      = "$Date$"
#__copyright__ = "Copyright (c) 2008 Flavio Percoco Premoli"
#__license__   = "GPLv2"

import sys
import os.path

def add_parent_directory_to_path():
    absolute_path_to_parent_directory = os.path.abspath(os.path.dirname(__file__) + '/..')
    sys.path.append(absolute_path_to_parent_directory)

def run_mousetrap():
    from mousetrap.controller import Controller
    Controller().start()

add_parent_directory_to_path()
run_mousetrap()
