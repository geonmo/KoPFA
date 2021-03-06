import FWCore.ParameterSet.Config as cms

from KoPFA.CommonTools.countingSequences_cfi import *
from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector
myJetId = pfJetIDSelector.clone()

from KoPFA.TopAnalyzer.triggerFilterByRun_cfi import *
from KoPFA.CMGAnalyzer.topHLTfilter_cff import *
from KoPFA.CommonTools.EventWeightProducer_cfi import *
from KoPFA.CMGAnalyzer.JetEnergyScale_cfi import *
from KoPFA.CMGAnalyzer.ElectronFilter_cfi import *
from KoPFA.CMGAnalyzer.MuonFilter_cfi import *
from KoPFA.TopAnalyzer.topDecayGenFilter_cfi import *

#scale up
#JetEnergyScale.doJecUnc = True
#JetEnergyScale.up = True
#scale down
#JetEnergyScale.doJecUnc = True
#JetEnergyScale.up = False 

VertexFilter = cms.EDFilter('VertexFilter',
    vertexLabel =  cms.InputTag('offlinePrimaryVertices'),
    min = cms.untracked.int32(1),
    max = cms.untracked.int32(999),
)

GenZmassFilter = cms.EDFilter('GenZmassFilter',
    genParticlesLabel = cms.InputTag('genParticles'),
    applyFilter = cms.untracked.bool( False ),
    decayMode = cms.untracked.vint32(11, 13, 15),
    min = cms.untracked.int32(0),
    max = cms.untracked.int32(999),
)

bTagSets = cms.untracked.VPSet(
#    cms.untracked.PSet(
#        algo = cms.untracked.string("trackCountingHighEffBJetTags"),
#        name = cms.untracked.string("TCHEL"),
#        cutValue = cms.untracked.double(1.7),
#        isCutMin = cms.untracked.bool(True),
#    ),
    cms.untracked.PSet(
        algo = cms.untracked.string("combinedSecondaryVertexBJetTags"),
        name = cms.untracked.string("CSVL"),
        cutValue = cms.untracked.double(0.244),
        isCutMin = cms.untracked.bool(True),
    ),
    cms.untracked.PSet(
        algo = cms.untracked.string("combinedSecondaryVertexBJetTags"),
        name = cms.untracked.string("CSVM"),
        cutValue = cms.untracked.double(0.679),
        isCutMin = cms.untracked.bool(True),
    ),
    cms.untracked.PSet(
        algo = cms.untracked.string("combinedSecondaryVertexBJetTags"),
        name = cms.untracked.string("CSVT"),
        cutValue = cms.untracked.double(0.898),
        isCutMin = cms.untracked.bool(True),
    ),
#    cms.untracked.PSet(
#        algo = cms.untracked.string("simpleSecondaryVertexHighEffBJetTags"),
#        name = cms.untracked.string("SSVHEM"),
#        cutValue = cms.untracked.double(1.74),
#        isCutMin = cms.untracked.bool(True),
#    ),
)

ElEl = cms.EDFilter('CMGTopElElAnalyzer',
    genParticlesLabel = cms.InputTag('genParticlesPruned'),
    genJetsLabel = cms.InputTag('genJetSel'),
    muonLabel1 =  cms.InputTag('Electrons'),
    muonLabel2 =  cms.InputTag('Electrons'),
    dileptonLabel = cms.untracked.InputTag("ZElEl","DiLepton"),
    metLabel =  cms.InputTag('JetEnergyScale','MET'),
    jetLabel =  cms.InputTag('JetEnergyScale','Jets'),
    vertexLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
    puWeightLabel = cms.InputTag('PUweight','weight'),
    puUpWeightLabel = cms.InputTag('PUweight','weightplus'),
    puDwWeightLabel = cms.InputTag('PUweight','weightminus'),
    puNVertexLabel = cms.InputTag('PUweight','npileup'),
    useEventCounter = cms.bool( True ),
    filters = cms.untracked.vstring(
    ),
    relIso1 = cms.untracked.double(0.15),
    relIso2 = cms.untracked.double(0.15),
    fullLepEvt = cms.untracked.InputTag("kinSolutionTtFullLepEventElEl","ttbars"),
    #fullLepEvt2 = cms.untracked.InputTag("maosSolutionTtFullLepEventElEl","ttbars"),
    nstep    = cms.untracked.uint32(0), ## 0 : ZMass > 0 | 1 : Iso  |  2 : PairSign | 3 : ZMass veto |  4 : MET |  5 : nJet >= 4 |  6 : nbjets30_CSVT >= 2
    bTagSets = bTagSets,
    histograms = cms.untracked.bool( False),
)

MuMu = cms.EDFilter('CMGTopMuMuAnalyzer',
    genParticlesLabel = cms.InputTag('genParticlesPruned'),
    genJetsLabel = cms.InputTag('genJetSel'),
    muonLabel1 =  cms.InputTag('Muons'),
    muonLabel2 =  cms.InputTag('Muons'),
    dileptonLabel = cms.untracked.InputTag("ZMuMu","DiLepton"),
    metLabel =  cms.InputTag('JetEnergyScale','MET'),
    jetLabel =  cms.InputTag('JetEnergyScale','Jets'),
    vertexLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
    puWeightLabel = cms.InputTag('PUweight','weight'),
    puUpWeightLabel = cms.InputTag('PUweight','weightplus'),
    puDwWeightLabel = cms.InputTag('PUweight','weightminus'),
    puNVertexLabel = cms.InputTag('PUweight','npileup'),
    useEventCounter = cms.bool( True ),
    filters = cms.untracked.vstring(
    ),
    #for jet cleaning overlapping with isolated epton within 0.4
    relIso1 = cms.untracked.double(0.15),
    relIso2 = cms.untracked.double(0.15),
    fullLepEvt = cms.untracked.InputTag("kinSolutionTtFullLepEventMuMu","ttbars"),
    #fullLepEvt2 = cms.untracked.InputTag("maosSolutionTtFullLepEventMuMu","ttbars"),
    nstep    = cms.untracked.uint32(0), ## 0 : ZMass > 0 | 1 : Iso  |  2 : PairSign | 3 : ZMass veto |  4 : MET |  5 : nJet >= 4 |  6 : nbjets30_CSVT >= 2
    bTagSets = bTagSets,
    histograms = cms.untracked.bool( False),
)

MuEl = cms.EDFilter('CMGTopMuElAnalyzer',
    genParticlesLabel = cms.InputTag('genParticles'),
    genJetsLabel = cms.InputTag('genJetSel'),
    muonLabel1 =  cms.InputTag('Muons'),
    muonLabel2 =  cms.InputTag('Electrons'),
    dileptonLabel = cms.untracked.InputTag("ZMuEl","DiLepton"),
    metLabel =  cms.InputTag('JetEnergyScale','MET'),
    jetLabel =  cms.InputTag('JetEnergyScale','Jets'),
    vertexLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
    puWeightLabel = cms.InputTag('PUweight','weight'),
    puUpWeightLabel = cms.InputTag('PUweight','weightplus'),
    puDwWeightLabel = cms.InputTag('PUweight','weightminus'),
    puNVertexLabel = cms.InputTag('PUweight','npileup'),
    useEventCounter = cms.bool( True ),
    filters = cms.untracked.vstring(
    ),
    #for jet cleaning overlapping with isolated epton within 0.4
    relIso1 = cms.untracked.double(0.15),
    relIso2 = cms.untracked.double(0.15),
    fullLepEvt = cms.untracked.InputTag("kinSolutionTtFullLepEventMuEl","ttbars"),
    #fullLepEvt2 = cms.untracked.InputTag("maosSolutionTtFullLepEventMuEl","ttbars"),
    nstep    = cms.untracked.uint32(0), ## 0 : ZMass > 0 | 1 : Iso  |  2 : PairSign | 3 : ZMass veto |  4 : MET |  5 : nJet >= 4 |  6 : nbjets30_CSVT >= 2
    bTagSets = bTagSets,
    histograms = cms.untracked.bool( False),
)

###jkim

MuMu2Mu = cms.EDFilter('CMGTopMuMu2MuAnalyzer',
    genParticlesLabel = cms.InputTag('genParticlesPruned'),
    genJetsLabel = cms.InputTag('genJetSel'),
    muonLabel1 =  cms.InputTag('Muons'),
    muonLabel2 =  cms.InputTag('Muons'),
    muonLabel3 =  cms.InputTag('Muons'),
    muonLabel4 =  cms.InputTag('Muons'),
    dileptonLabel = cms.untracked.InputTag("MuMuJPsiMuMu","DiLepton"),
    jpsiLabel = cms.untracked.InputTag("MuMuJPsiMuMu","JPsi"),
    ssjpsiLabel = cms.untracked.InputTag("MuMuJPsiMuMu","ssJPsi"),
    lepJPsiLabel1 = cms.untracked.InputTag("MuMuJPsiMuMu","LepJPsi1"),
    lepJPsiLabel2 = cms.untracked.InputTag("MuMuJPsiMuMu","LepJPsi2"),
    metLabel =  cms.InputTag('JetEnergyScale','MET'),
    jetLabel =  cms.InputTag('JetEnergyScale','Jets'),
    vertexLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
    puWeightLabel = cms.InputTag('PUweight','weight'),
    puUpWeightLabel = cms.InputTag('PUweight','weightplus'),
    puDwWeightLabel = cms.InputTag('PUweight','weightminus'),
    puNVertexLabel = cms.InputTag('PUweight','npileup'),
    useEventCounter = cms.bool( True ),
    filters = cms.untracked.vstring(
    ),
    #for jet cleaning overlapping with isolated epton within 0.4
    relIso1 = cms.untracked.double(0.15),
    relIso2 = cms.untracked.double(0.15),
    #fullLepEvt = cms.untracked.InputTag("kinSolutionTtFullLepEventMuMu","ttbars"),
    #fullLepEvt2 = cms.untracked.InputTag("maosSolutionTtFullLepEventMuMu","ttbars"),
    nstep    = cms.untracked.uint32(0), ## 0 : ZMass > 0 | 1 : Iso  |  2 : PairSign | 3 : ZMass veto |  4 : MET |  5 : nJet >= 4 |  6 : nbjets30_CSVT >= 2
    bTagSets = bTagSets,
    histograms = cms.untracked.bool( False),
)

MuMu2El = cms.EDFilter('CMGTopMuMu2ElAnalyzer',
    genParticlesLabel = cms.InputTag('genParticlesPruned'),
    genJetsLabel = cms.InputTag('genJetSel'),
    muonLabel1 =  cms.InputTag('Muons'),
    muonLabel2 =  cms.InputTag('Muons'),
    muonLabel3 =  cms.InputTag('Electrons'),
    muonLabel4 =  cms.InputTag('Electrons'),
    dileptonLabel = cms.untracked.InputTag("MuMuJPsiElEl","DiLepton"),
    jpsiLabel = cms.untracked.InputTag("MuMuJPsiElEl","JPsi"),
    ssjpsiLabel = cms.untracked.InputTag("MuMuJPsiElEl","ssJPsi"),
    lepJPsiLabel1 = cms.untracked.InputTag("MuMuJPsiElEl","LepJPsi1"),
    lepJPsiLabel2 = cms.untracked.InputTag("MuMuJPsiElEl","LepJPsi2"),
    metLabel =  cms.InputTag('JetEnergyScale','MET'),
    jetLabel =  cms.InputTag('JetEnergyScale','Jets'),
    vertexLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
    puWeightLabel = cms.InputTag('PUweight','weight'),
    puUpWeightLabel = cms.InputTag('PUweight','weightplus'),
    puDwWeightLabel = cms.InputTag('PUweight','weightminus'),
    puNVertexLabel = cms.InputTag('PUweight','npileup'),
    useEventCounter = cms.bool( True ),
    filters = cms.untracked.vstring(
    ),
    #for jet cleaning overlapping with isolated epton within 0.4
    relIso1 = cms.untracked.double(0.15),
    relIso2 = cms.untracked.double(0.15),
    #fullLepEvt = cms.untracked.InputTag("kinSolutionTtFullLepEventMuMu","ttbars"),
    #fullLepEvt2 = cms.untracked.InputTag("maosSolutionTtFullLepEventMuMu","ttbars"),
    nstep    = cms.untracked.uint32(0), ## 0 : ZMass > 0 | 1 : Iso  |  2 : PairSign | 3 : ZMass veto |  4 : MET |  5 : nJet >= 4 |  6 : nbjets30_CSVT >= 2
    bTagSets = bTagSets,
    histograms = cms.untracked.bool( False),
)

MuEl2Mu = cms.EDFilter('CMGTopMuEl2MuAnalyzer',
    genParticlesLabel = cms.InputTag('genParticles'),
    genJetsLabel = cms.InputTag('genJetSel'),
    muonLabel1 =  cms.InputTag('Muons'),
    muonLabel2 =  cms.InputTag('Electrons'),
    muonLabel3 =  cms.InputTag('Muons'),
    muonLabel4 =  cms.InputTag('Muons'),
    dileptonLabel = cms.untracked.InputTag("MuElJPsiMuMu","DiLepton"),
    jpsiLabel = cms.untracked.InputTag("MuElJPsiMuMu","JPsi"),
    ssjpsiLabel = cms.untracked.InputTag("MuElJPsiMuMu","ssJPsi"),
    lepJPsiLabel1 = cms.untracked.InputTag("MuElJPsiMuMu","LepJPsi1"),
    lepJPsiLabel2 = cms.untracked.InputTag("MuElJPsiMuMu","LepJPsi2"),
    metLabel =  cms.InputTag('JetEnergyScale','MET'),
    jetLabel =  cms.InputTag('JetEnergyScale','Jets'),
    vertexLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
    puWeightLabel = cms.InputTag('PUweight','weight'),
    puUpWeightLabel = cms.InputTag('PUweight','weightplus'),
    puDwWeightLabel = cms.InputTag('PUweight','weightminus'),
    puNVertexLabel = cms.InputTag('PUweight','npileup'),
    useEventCounter = cms.bool( True ),
    filters = cms.untracked.vstring(
    ),
    #for jet cleaning overlapping with isolated epton within 0.4
    relIso1 = cms.untracked.double(0.15),
    relIso2 = cms.untracked.double(0.15),
    #fullLepEvt = cms.untracked.InputTag("kinSolutionTtFullLepEventMuEl","ttbars"),
    #fullLepEvt2 = cms.untracked.InputTag("maosSolutionTtFullLepEventMuEl","ttbars"),
    nstep    = cms.untracked.uint32(0), ## 0 : ZMass > 0 | 1 : Iso  |  2 : PairSign | 3 : ZMass veto |  4 : MET |  5 : nJet >= 4 |  6 : nbjets30_CSVT >= 2
    bTagSets = bTagSets,
    histograms = cms.untracked.bool( False),
)

MuEl2El = cms.EDFilter('CMGTopMuEl2ElAnalyzer',
    genParticlesLabel = cms.InputTag('genParticles'),
    genJetsLabel = cms.InputTag('genJetSel'),
    muonLabel1 =  cms.InputTag('Muons'),
    muonLabel2 =  cms.InputTag('Electrons'),
    muonLabel3 =  cms.InputTag('Electrons'),
    muonLabel4 =  cms.InputTag('Electrons'),
    dileptonLabel = cms.untracked.InputTag("MuElJPsiElEl","DiLepton"),
    jpsiLabel = cms.untracked.InputTag("MuElJPsiElEl","JPsi"),
    ssjpsiLabel = cms.untracked.InputTag("MuElJPsiElEl","ssJPsi"),
    lepJPsiLabel1 = cms.untracked.InputTag("MuElJPsiElEl","LepJPsi1"),
    lepJPsiLabel2 = cms.untracked.InputTag("MuElJPsiElEl","LepJPsi2"),
    metLabel =  cms.InputTag('JetEnergyScale','MET'),
    jetLabel =  cms.InputTag('JetEnergyScale','Jets'),
    vertexLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
    puWeightLabel = cms.InputTag('PUweight','weight'),
    puUpWeightLabel = cms.InputTag('PUweight','weightplus'),
    puDwWeightLabel = cms.InputTag('PUweight','weightminus'),
    puNVertexLabel = cms.InputTag('PUweight','npileup'),
    useEventCounter = cms.bool( True ),
    filters = cms.untracked.vstring(
    ),
    #for jet cleaning overlapping with isolated epton within 0.4
    relIso1 = cms.untracked.double(0.15),
    relIso2 = cms.untracked.double(0.15),
    #fullLepEvt = cms.untracked.InputTag("kinSolutionTtFullLepEventMuEl","ttbars"),
    #fullLepEvt2 = cms.untracked.InputTag("maosSolutionTtFullLepEventMuEl","ttbars"),
    nstep    = cms.untracked.uint32(0), ## 0 : ZMass > 0 | 1 : Iso  |  2 : PairSign | 3 : ZMass veto |  4 : MET |  5 : nJet >= 4 |  6 : nbjets30_CSVT >= 2
    bTagSets = bTagSets,
    histograms = cms.untracked.bool( False),
)

ElEl2Mu = cms.EDFilter('CMGTopElEl2MuAnalyzer',
    genParticlesLabel = cms.InputTag('genParticlesPruned'),
    genJetsLabel = cms.InputTag('genJetSel'),
    muonLabel1 =  cms.InputTag('Electrons'),
    muonLabel2 =  cms.InputTag('Electrons'),
    muonLabel3 =  cms.InputTag('Muons'),
    muonLabel4 =  cms.InputTag('Muons'),
    dileptonLabel = cms.untracked.InputTag("ElElJPsiMuMu","DiLepton"),
    jpsiLabel = cms.untracked.InputTag("ElElJPsiMuMu","JPsi"),
    ssjpsiLabel = cms.untracked.InputTag("ElElJPsiMuMu","ssJPsi"),
    lepJPsiLabel1 = cms.untracked.InputTag("ElElJPsiMuMu","LepJPsi1"),
    lepJPsiLabel2 = cms.untracked.InputTag("ElElJPsiMuMu","LepJPsi2"),
    metLabel =  cms.InputTag('JetEnergyScale','MET'),
    jetLabel =  cms.InputTag('JetEnergyScale','Jets'),
    vertexLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
    puWeightLabel = cms.InputTag('PUweight','weight'),
    puUpWeightLabel = cms.InputTag('PUweight','weightplus'),
    puDwWeightLabel = cms.InputTag('PUweight','weightminus'),
    puNVertexLabel = cms.InputTag('PUweight','npileup'),
    useEventCounter = cms.bool( True ),
    filters = cms.untracked.vstring(
    ),
    relIso1 = cms.untracked.double(0.15),
    relIso2 = cms.untracked.double(0.15),
    #fullLepEvt = cms.untracked.InputTag("kinSolutionTtFullLepEventElEl","ttbars"),
    #fullLepEvt2 = cms.untracked.InputTag("maosSolutionTtFullLepEventElEl","ttbars"),
    nstep    = cms.untracked.uint32(0), ## 0 : ZMass > 0 | 1 : Iso  |  2 : PairSign | 3 : ZMass veto |  4 : MET |  5 : nJet >= 4 |  6 : nbjets30_CSVT >= 2
    bTagSets = bTagSets,
    histograms = cms.untracked.bool( False),
)

ElEl2El = cms.EDFilter('CMGTopElEl2ElAnalyzer',
    genParticlesLabel = cms.InputTag('genParticlesPruned'),
    genJetsLabel = cms.InputTag('genJetSel'),
    muonLabel1 =  cms.InputTag('Electrons'),
    muonLabel2 =  cms.InputTag('Electrons'),
    muonLabel3 =  cms.InputTag('Electrons'),
    muonLabel4 =  cms.InputTag('Electrons'),
    dileptonLabel = cms.untracked.InputTag("ElElJPsiElEl","DiLepton"),
    jpsiLabel = cms.untracked.InputTag("ElElJPsiElEl","JPsi"),
    ssjpsiLabel = cms.untracked.InputTag("ElElJPsiElEl","ssJPsi"),
    lepJPsiLabel1 = cms.untracked.InputTag("ElElJPsiElEl","LepJPsi1"),
    lepJPsiLabel2 = cms.untracked.InputTag("ElElJPsiElEl","LepJPsi2"),
    metLabel =  cms.InputTag('JetEnergyScale','MET'),
    jetLabel =  cms.InputTag('JetEnergyScale','Jets'),
    vertexLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
    puWeightLabel = cms.InputTag('PUweight','weight'),
    puUpWeightLabel = cms.InputTag('PUweight','weightplus'),
    puDwWeightLabel = cms.InputTag('PUweight','weightminus'),
    puNVertexLabel = cms.InputTag('PUweight','npileup'),
    useEventCounter = cms.bool( True ),
    filters = cms.untracked.vstring(
    ),
    relIso1 = cms.untracked.double(0.15),
    relIso2 = cms.untracked.double(0.15),
    #fullLepEvt = cms.untracked.InputTag("kinSolutionTtFullLepEventElEl","ttbars"),
    #fullLepEvt2 = cms.untracked.InputTag("maosSolutionTtFullLepEventElEl","ttbars"),
    nstep    = cms.untracked.uint32(0), ## 0 : ZMass > 0 | 1 : Iso  |  2 : PairSign | 3 : ZMass veto |  4 : MET |  5 : nJet >= 4 |  6 : nbjets30_CSVT >= 2
    bTagSets = bTagSets,
    histograms = cms.untracked.bool( False),
)

removeDuplicate = cms.EDFilter("RemoveDuplicate",
    applyFilter = cms.untracked.bool( True )
)

nEventsPatHLT = cms.EDProducer("EventCountProducer")
nEventsDuplicate = cms.EDProducer("EventCountProducer")
nEventsTopFilter = cms.EDProducer("EventCountProducer")

## std sequence to produce the ttFullLepEvent
from TopQuarkAnalysis.TopEventProducers.sequences.ttFullLepEvtBuilder_cff import *
