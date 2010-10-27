#!/usr/bin/env pyhton2.6

# Copyright (C) 2010  Leonardo Silva Amaral

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# The good, the bad and the ugly code style
# Here, a lot of copied code from another places. A good restart with py.
# Let begin with the ugly

import ConfigParser
from PyDbLite import Base
from elementtree.ElementTree import parse

config = ConfigParser.ConfigParser()
config.read("cho++.conf")

# Force read-only operations within database
chofile=open(config.get("main", "datafile"), "r")

class chotab(dict):
	def __init__():
		self.xmldata = parse(chofile)
		self.xmlparsing(self.xmldata)

	def xmlparsing(xmldata):
		iterator = xmldata.getiterator()
		# Initial parsing here. Just to pass by headers
		
