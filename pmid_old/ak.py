#!/usr/bin/python
# libraries used
import os,sys
import time
import re
import urllib
import json
from time import sleep
#from proxy import urllib2
import requests
from bs4 import BeautifulSoup
# import mechanize
# from urlparse import urlsplit,urlparse
# from multiprocessing import Pool
from multiprocessing import Process, Lock,Pool
# print "done"
new_data={}
# new_list = []
fname = str(sys.argv[1])
with open(fname,'r') as inp:
	pmids = [x.strip() for x in inp.readlines()]

proxies = { "http": "http://username:password@host:port/", "https": "http://username:password@host:port/", }
# print pmids
# for pmid in pmids:
def get_data(pmid):
	global proxies
	url = "https://www.ncbi.nlm.nih.gov/pubmed/?term="+str(pmid)
	# print (url)
	data={}
	abtract=""
	r= requests.get(url,proxies=proxies)
	# page = urllib.request.urlopen(url)
	# html_doc = page.read()
	html_doc = r.text
	soup = BeautifulSoup(html_doc,"html5lib")
	for anchor in soup.find_all('abstracttext'):
		label = anchor.get('label')
		if label!=None:
			abtract = label+":"+anchor.text
		else:
			abtract=anchor.text
			# print abtract
	mesh_terms=[]
	for link in soup.find_all('a'):
		alterm = link.get('alterm')
		alsec = link.get('alsec')
		if alterm !=None and alsec!=None and alsec=='mesh':
			mesh_terms.append( alterm)

	data['abstractText']=abtract
	data['pmid']=pmid
	data['meshMajor']=mesh_terms
	del(mesh_terms)
	return data
	# new_list.append(data);
	# del(data)
	# break;
if __name__ == '__main__':
		#new_list=[get_data(pmid) for pmid in pmids] 
		with Pool(12)as p:
			new_list = (p.map(get_data,pmids))
		sleep(10)

new_data['articles']=new_list
with open(str(fname+".json"),'w')as fp:
	json.dump(new_data,fp)
