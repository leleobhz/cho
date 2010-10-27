#!/bin/bash

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
