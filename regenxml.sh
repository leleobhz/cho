#!/bin/bash

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


pagestart=20
pageend=114

rm -f taco_versao2.xml

while [[ $pagestart -lt $(($pageend+1)) ]]
do
	pdftohtml -xml -f $pagestart -l $pagestart -stdout taco_versao2.pdf >> taco_versao2.xml || (echo "Oh oh, no donut for you..." ; exit 1)
	pagestart=$(($pagestart+2))
	echo -ne "\rProgresso: $(($pagestart * 100 / $(($pageend+1)) ))%"
done
echo
