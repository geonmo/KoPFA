#ifndef KoPFA_CommonTools_CMGFinalLeptonProducer_h
#define KoPFA_CommonTools_CMGFinalLeptonProducer_h

// store the position of the Z combinaison the closest to the Z mass

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "KoPFA/CommonTools/interface/MuonIDSelector.h"
//#include "PFAnalyses/CommonTools/interface/PatMuonSelector.h"
//#include "PFAnalyses/CommonTools/interface/PatLeptonSelector.h"
#include "KoPFA/CommonTools/interface/LeptonIsoSelector.h"
#include "KoPFA/DataFormats/interface/Lepton.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/RecoCandidate/interface/IsoDepositDirection.h"
#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/RecoCandidate/interface/IsoDepositVetos.h"
#include "DataFormats/PatCandidates/interface/Isolation.h"
#include "AnalysisDataFormats/CMGTools/interface/Electron.h"
#include "AnalysisDataFormats/CMGTools/interface/Muon.h"

#include "TFile.h"
#include "TTree.h"
#include "TH1.h"

class CMGFinalLeptonProducer : public edm::EDProducer
{
 public:

  explicit CMGFinalLeptonProducer(const edm::ParameterSet&);
  ~CMGFinalLeptonProducer();

  void beginJob();
  void produce(edm::Event&, const edm::EventSetup&);
  void endJob();

 private:

  edm::InputTag MuMuLep1Label_;
  edm::InputTag MuMuLep2Label_;
  edm::InputTag MuElLep1Label_;
  edm::InputTag MuElLep2Label_;
  edm::InputTag ElElLep1Label_;
  edm::InputTag ElElLep2Label_;

  edm::InputTag MuMuJPsiMuMuLep1Label_;
  edm::InputTag MuMuJPsiMuMuLep2Label_;
  edm::InputTag MuMuJPsiMuMuLep3Label_;
  edm::InputTag MuMuJPsiMuMuLep4Label_;

  edm::InputTag MuMuJPsiElElLep1Label_;
  edm::InputTag MuMuJPsiElElLep2Label_;
  edm::InputTag MuMuJPsiElElLep3Label_;
  edm::InputTag MuMuJPsiElElLep4Label_;

  edm::InputTag MuElJPsiMuMuLep1Label_;
  edm::InputTag MuElJPsiMuMuLep2Label_;
  edm::InputTag MuElJPsiMuMuLep3Label_;
  edm::InputTag MuElJPsiMuMuLep4Label_;

  edm::InputTag MuElJPsiElElLep1Label_;
  edm::InputTag MuElJPsiElElLep2Label_;
  edm::InputTag MuElJPsiElElLep3Label_;
  edm::InputTag MuElJPsiElElLep4Label_;

  edm::InputTag ElElJPsiMuMuLep1Label_;
  edm::InputTag ElElJPsiMuMuLep2Label_;
  edm::InputTag ElElJPsiMuMuLep3Label_;
  edm::InputTag ElElJPsiMuMuLep4Label_;

  edm::InputTag ElElJPsiElElLep1Label_;
  edm::InputTag ElElJPsiElElLep2Label_;
  edm::InputTag ElElJPsiElElLep3Label_;
  edm::InputTag ElElJPsiElElLep4Label_;
 
  edm::Handle<vector<cmg::Muon> > mmlep1_;
  edm::Handle<vector<cmg::Muon> > mmlep2_;
  edm::Handle<vector<cmg::Muon> > melep1_;
  edm::Handle<vector<cmg::Electron> > eelep1_;
  edm::Handle<vector<cmg::Electron> > eelep2_;
  edm::Handle<vector<cmg::Electron> > melep2_;

  edm::Handle<vector<cmg::Muon> > mm2mlep1_;
  edm::Handle<vector<cmg::Muon> > mm2mlep2_;
  edm::Handle<vector<cmg::Muon> > mm2mlep3_;
  edm::Handle<vector<cmg::Muon> > mm2mlep4_;

  edm::Handle<vector<cmg::Muon> > mm2elep1_;
  edm::Handle<vector<cmg::Muon> > mm2elep2_;
  edm::Handle<vector<cmg::Electron> > mm2elep3_;
  edm::Handle<vector<cmg::Electron> > mm2elep4_;

  edm::Handle<vector<cmg::Muon> > me2mlep1_;
  edm::Handle<vector<cmg::Electron> > me2mlep2_;
  edm::Handle<vector<cmg::Muon> > me2mlep3_;
  edm::Handle<vector<cmg::Muon> > me2mlep4_;

  edm::Handle<vector<cmg::Muon> > me2elep1_;
  edm::Handle<vector<cmg::Electron> > me2elep2_;
  edm::Handle<vector<cmg::Electron> > me2elep3_;
  edm::Handle<vector<cmg::Electron> > me2elep4_;

  edm::Handle<vector<cmg::Electron> > ee2mlep1_;
  edm::Handle<vector<cmg::Electron> > ee2mlep2_;
  edm::Handle<vector<cmg::Muon> > ee2mlep3_;
  edm::Handle<vector<cmg::Muon> > ee2mlep4_;

  edm::Handle<vector<cmg::Electron> > ee2elep1_;
  edm::Handle<vector<cmg::Electron> > ee2elep2_;
  edm::Handle<vector<cmg::Electron> > ee2elep3_;
  edm::Handle<vector<cmg::Electron> > ee2elep4_;

};


#endif

