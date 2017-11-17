#!/usr/bin/python
import json
import os,sys
import codecs

f= "result.json"
with codecs.open(f, 'r',encoding='utf-8', errors='ignore') as infile:
	file_data = json.load(infile)
	print len(file_data['articles'])
	for art in file_data['articles']:
		#print art['pmid']
		if art['pmid']==26535433:
			print art['pmid']
			print art['abstractText']	
