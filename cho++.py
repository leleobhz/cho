#!/usr/bin/env pyhton2.6

# The good, the bad and the ugly code style
# Here, a lot of copied code from another places. A good restart with py.
# Let begin with the ugly

from elementtree import ElementTree

config = ConfigParser.ConfigParser()
config.read("cho++.conf")


class chotab(dict)
	def __init__(self.filename)
		self.xmldata = ElementTree(file=config.get("main", "datafile"))
		self.xmlparsing(self.xmldata)

	def xmlparsing(self.xmldata)
		self.iterator = self.xmldata.getiterator()
