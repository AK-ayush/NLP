#!/usr/bin/python
import json
import os,sys
import codecs

head = []
head_d = {}
#file_list= str(sys.argv[1])
#print (file_list)

for f in os.listdir('.'):
    if 'json' in f:
    	print f
    	with codecs.open(f, 'r',encoding='utf-8', errors='ignore') as infile:
    		file_data = json.load(infile)
	        head += file_data['articles']
		head_d['articles']=head
with open("result.json", "w") as outfile:
	json.dump(head_d, outfile)
