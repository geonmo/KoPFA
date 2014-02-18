#!/usr/bin/env python
import os,sys
if ( len( sys.argv ) <2 ) :
	print "Wrong"
	exit(-1)
input = open(sys.argv[1],'r')
output_filename = 'output_'+sys.argv[1]
output = open(output_filename,"w+")
cmd = "cat cmgtuple_madspin_cff.py > "+output_filename
os.system(cmd)
output.write( "source.fileNames.extend([\n")
lines = input.readlines()
for line in lines :
	if line is not lines[-1] : 
		output.write("\"root://cluster142.knu.ac.kr/"+line.strip()+'\",\n')
	else :
		output.write("\"root://cluster142.knu.ac.kr/"+line.strip()+'\"\n')
		
output.write("])\n")
