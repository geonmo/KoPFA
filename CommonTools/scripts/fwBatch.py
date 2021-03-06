#!/usr/bin/env python
# Colin
# additional layer, on top of cmsBatch.py

import os, sys,  imp, re, pprint, string
from optparse import OptionParser

import castortools

from addToDatasets import *

    


parser = OptionParser()
parser.usage = "fwBatch.py <sampleName>"
parser.add_option("-n", "--negate", action="store_true",
                  dest="negate",
                  help="do not proceed",
                  default=False)
parser.add_option("-c", "--castorBaseDir", 
                  dest="castorBaseDir",
                  help="Base castor directory. Subdirectories will be created automatically for each prod",
                  default="/castor/cern.ch/user/c/cbern/cmst3/SusyJetMET")
parser.add_option("-t", "--tier", 
                  dest="tier",
                  help="Tier: extension you can give to specify you are doing a new production",
                  default="")
parser.add_option("-N", "--numberOfInputFiles", 
                  dest="nInput",
                  help="number of input files per job",
                  default="1")
parser.add_option("-q", "--queue", 
                  dest="queue",
                  help="batch queue",
                  default="cmst3")


(options,args) = parser.parse_args()

if len(args)!=1:
    parser.print_help()
    sys.exit(1)

sampleName = args[0]


print 'starting prod for sample:', sampleName

# preparing castor dir -----------------

cdir = options.castorBaseDir 


# sampleAndTier = sampleName
#if options.tier != "":
#    sampleAndTier += "/" + options.tier

#print "sampleAndTier ",sampleAndTier
#outFile = cdir
#if options.tier!="":
#    outFile += sampleAndTier
#else:
#    outFile += sampleName
    
if options.tier != "":
    sampleName += "/" + options.tier

print "sampleName ",sampleName
outFile = cdir
outFile += sampleName
    
# creating castor dir
rfmkdir  = 'rfmkdir -p ' + outFile
print rfmkdir 
os.system( rfmkdir )
# outFile += '/PFAnalysis_%s.root' % ext

# prepare local output dir:
localOutputDir = './' + sampleName 
mkdir = 'mkdir -p ' + localOutputDir
print mkdir
os.system(mkdir)

cmsBatch = 'cmsBatch.py %s susyJetMET_cfg.py -r %s -b "bsub -q %s <  batchScript.sh" -o %s' % (options.nInput, outFile, options.queue, localOutputDir)

addToDatasets( sampleName )


print cmsBatch
