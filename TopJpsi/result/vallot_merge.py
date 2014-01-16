#!/usr/bin/env python

import os,sys

if len(sys.argv) != 2 :
	sys.stderr.write( "Argument is wrong!\n")
	sys.stderr.write( "Usage : ./vallot_merge.py <'Out' directory>\n")
	sys.stderr.write( "Example : ./vallot_merge.py ../../CMGAnalyzer/prod/Out/\n")
	sys.exit(-1)
dir = sys.argv[1]
list_dir=[]
for list in  os.listdir(dir):
	if os.path.isdir(dir+list) :
		list_dir.append(os.path.normpath(os.getcwd()+'/'+dir+list))	
for sample_fullpath in list_dir :
	sample_name = sample_fullpath.split('/')[-1]
	vallot_dir = sample_fullpath+'/Res'
	cmd = "hadd vallot_"+sample_name+".root "+vallot_dir+'/*.root'
	print cmd
	os.system(cmd)

