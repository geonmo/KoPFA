#!/usr/bin/env python
import os,sys
filename = sys.argv[1]
file = open(filename,'r')
num = []
for line in file.readlines() :
	value = ( int(line.split('/')[-1].split('_')[1]) ) 
	if ( len(num) > 0 and num[-1] ==  value ) :
	  print value
	else : 
	  num.append(value)
#num.sort()
#print num

