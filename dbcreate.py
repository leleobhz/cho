#!/usr/bin/env pyhton2.6

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
