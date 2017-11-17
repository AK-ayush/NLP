#!/usr/bin/python3
# libraries used
import os,sys
if __name__ == '__main__':
	flist = ['xan','xaq','xar','xas']
	
	for fname in flist:
		ret = False
		while ret == False:
			os.system("python3 ak.py split_tr/"+str(fname));
			if os.path.isfile("split_tr/"+str(fname)+".json"):
				ret = True;
		print ("done--> "+str(fname))

			

