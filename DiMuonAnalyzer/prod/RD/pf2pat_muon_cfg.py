import FWCore.ParameterSet.Config as cms

process = cms.Process("PAT")

## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")

## Options and Output Report
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

## Source
process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring(
'/store/data/Run2010A/Mu/RECO/Jul6thReReco_v1/0054/FCC806C9-7D89-DF11-8666-0022649F01AA.root')
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('START36_V4::All')
process.load("Configuration.StandardSequences.MagneticField_cff")

## Output Module Configuration (expects a path 'p')
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('patTuple_muon.root'),
                               # save only events passing the full path
                               SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               # save PAT Layer 1 output; you need a '*' to
                               # unpack the list of commands 'patEventContent'
                               outputCommands = cms.untracked.vstring('drop *')
                               )

## Standard PAT Configuration File
process.load("PhysicsTools.PatAlgos.patSequences_cff")
process.load("PhysicsTools.PFCandProducer.PF2PAT_cff")

#PF2PAT
process.load("PhysicsTools.PatAlgos.patSequences_cff")
from PhysicsTools.PatAlgos.tools.pfTools import *
postfix = "PFlow"
usePF2PAT(process,runPF2PAT=True, jetAlgo='AK5', runOnMC=False, postfix=postfix)
removeMCMatching(process, ['All'] )

process.primaryVertexFilter = cms.EDFilter("VertexSelector",
   src = cms.InputTag("offlinePrimaryVertices"),
   cut = cms.string("!isFake && ndof > 4 && abs(z) <= 15 && position.Rho <= 2"), # tracksSize() > 3 for the older cut
   filter = cms.bool(True),   # otherwise it won't filter the events, just produce an empty vertex collection.
)

process.noscraping = cms.EDFilter("FilterOutScraping",
   applyfilter = cms.untracked.bool(True),
   debugOn = cms.untracked.bool(False),
   numtrack = cms.untracked.uint32(10),
   thresh = cms.untracked.double(0.25)
)

#PATMUON Selector
#Here we define the muon selectors
process.acceptedMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("selectedPatMuons"),
    cut =cms.string("pt > 15 && abs(eta) < 2.4")
)

process.patMuonFilter = cms.EDFilter("CandViewCountFilter",
  src = cms.InputTag('acceptedMuons'),
  minNumber = cms.uint32(1)
)
   
##################################################################
process.load("KoPFA.CommonTools.countingSequences_cfi")

process.outpath = cms.EndPath(process.saveHistosInRunInfo*process.out)

process.p = cms.Path(
                 process.primaryVertexFilter*
                 process.noscraping*
                 process.startupSequence*
                 process.patDefaultSequence*
                 getattr(process,"patPF2PATSequence"+postfix)*
                 process.acceptedMuons*
                 process.patMuonFilter*
                 process.finalSequence
    )

from PhysicsTools.PatAlgos.patEventContent_cff import *
process.out.outputCommands += patTriggerEventContent
process.out.outputCommands += patExtraAodEventContent
process.out.outputCommands += patEventContentNoCleaning

process.out.outputCommands.extend(cms.untracked.vstring(
                                                    'keep *_MEtoEDMConverter_*_*',
                                                    'keep *_particleFlow_*_*',
                                                ))

process.MessageLogger.cerr.FwkReport.reportEvery = 100
