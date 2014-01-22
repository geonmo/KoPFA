import FWCore.ParameterSet.Config as cms

CMGFinalLeptons = cms.EDProducer("CMGFinalLeptonProducer",
  MuMuLep1Label =  cms.untracked.InputTag('ZMuMu','Lepton1'),
  MuMuLep2Label =  cms.untracked.InputTag('ZMuMu','Lepton2'),
  MuElLep1Label =  cms.untracked.InputTag('ZMuEl','Lepton1'),
  MuElLep2Label =  cms.untracked.InputTag('ZMuEl','Lepton2'),
  ElElLep1Label =  cms.untracked.InputTag('ZElEl','Lepton1'),
  ElElLep2Label =  cms.untracked.InputTag('ZElEl','Lepton2'),
  MuMuJPsiMuMuLep1Label =  cms.untracked.InputTag('MuMuJPsiMuMu','Lepton1'), #jkim
  MuMuJPsiMuMuLep2Label =  cms.untracked.InputTag('MuMuJPsiMuMu','Lepton2'), #jkim
  MuMuJPsiMuMuLep3Label =  cms.untracked.InputTag('MuMuJPsiMuMu','Lepton3'), #jkim
  MuMuJPsiMuMuLep4Label =  cms.untracked.InputTag('MuMuJPsiMuMu','Lepton4'), #jkim
  MuMuJPsiElElLep1Label =  cms.untracked.InputTag('MuMuJPsiElEl','Lepton1'), #jkim
  MuMuJPsiElElLep2Label =  cms.untracked.InputTag('MuMuJPsiElEl','Lepton2'), #jkim
  MuMuJPsiElElLep3Label =  cms.untracked.InputTag('MuMuJPsiElEl','Lepton3'), #jkim
  MuMuJPsiElElLep4Label =  cms.untracked.InputTag('MuMuJPsiElEl','Lepton4'), #jkim
  MuElJPsiMuMuLep1Label =  cms.untracked.InputTag('MuElJPsiMuMu','Lepton1'), #jkim
  MuElJPsiMuMuLep2Label =  cms.untracked.InputTag('MuElJPsiMuMu','Lepton2'), #jkim
  MuElJPsiMuMuLep3Label =  cms.untracked.InputTag('MuElJPsiMuMu','Lepton3'), #jkim
  MuElJPsiMuMuLep4Label =  cms.untracked.InputTag('MuElJPsiMuMu','Lepton4'), #jkim
  MuElJPsiElElLep1Label =  cms.untracked.InputTag('MuElJPsiElEl','Lepton1'), #jkim
  MuElJPsiElElLep2Label =  cms.untracked.InputTag('MuElJPsiElEl','Lepton2'), #jkim
  MuElJPsiElElLep3Label =  cms.untracked.InputTag('MuElJPsiElEl','Lepton3'), #jkim
  MuElJPsiElElLep4Label =  cms.untracked.InputTag('MuElJPsiElEl','Lepton4'), #jkim
  ElElJPsiMuMuLep1Label =  cms.untracked.InputTag('ElElJPsiMuMu','Lepton1'), #jkim
  ElElJPsiMuMuLep2Label =  cms.untracked.InputTag('ElElJPsiMuMu','Lepton2'), #jkim
  ElElJPsiMuMuLep3Label =  cms.untracked.InputTag('ElElJPsiMuMu','Lepton3'), #jkim
  ElElJPsiMuMuLep4Label =  cms.untracked.InputTag('ElElJPsiMuMu','Lepton4'), #jkim
  ElElJPsiElElLep1Label =  cms.untracked.InputTag('ElElJPsiElEl','Lepton1'), #jkim
  ElElJPsiElElLep2Label =  cms.untracked.InputTag('ElElJPsiElEl','Lepton2'), #jkim
  ElElJPsiElElLep3Label =  cms.untracked.InputTag('ElElJPsiElEl','Lepton3'), #jkim
  ElElJPsiElElLep4Label =  cms.untracked.InputTag('ElElJPsiElEl','Lepton4'), #jkim

)
