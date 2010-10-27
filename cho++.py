#!/usr/bin/env pyhton2.6

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
		
