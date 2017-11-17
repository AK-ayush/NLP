import os,sys


f1= sys.argv[1]
f2= sys.argv[2]
l1 =[]
l2 =[]
with open(f1, 'r') as f_1:
	# print f_1.readlines()
	for num in f_1.readlines():
		l1.append(num)
# l1 = sorted(l1)

with open(f2, 'r') as f_2:
	# print f_2.readlines()
	for num in f_2.readlines():
		l2.append(num)
# l2 = sorted(l2)
#out = open('left_pmid','w');
ct=0
for i in l2:
	if i not in l1:
		#out.write(i) 
		ct+=1

print ct
#out.close()
