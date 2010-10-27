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


import ConfigParser
import sqlite3
from elementtree.ElementTree import parse

config = ConfigParser.ConfigParser()
config.read("cho++.conf")

# Force read-only operations within XML file
chofile=open(config.get("main", "xmlfile"), "r")
conn = sqlite3.connect(config.get("main", "dbfile"))

cursor = conn.cursor()

except 
cursor.execute('CREATE TABLE alimentos (idx INTEGER PRIMARY KEY, alimento TEXT, cho')

# XML party #

xmldata = parse()



# EOF
conn.commit()
