#include "KoPFA/CMGAnalyzer/interface/CMGFinalLeptonProducer.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Common/interface/Ptr.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"

// #include "TauAnalysis/CandidateTools/interface/FetchCollection.h"
using namespace std;

CMGFinalLeptonProducer::CMGFinalLeptonProducer(const edm::ParameterSet& cfg)
{
  MuMuLep1Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuMuLep1Label");
  MuMuLep2Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuMuLep2Label");
  MuElLep1Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuElLep1Label");
  MuElLep2Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuElLep2Label");
  ElElLep1Label_ = cfg.getUntrackedParameter<edm::InputTag>("ElElLep1Label");
  ElElLep2Label_ = cfg.getUntrackedParameter<edm::InputTag>("ElElLep2Label");

  MuMuJPsiMuMuLep1Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuMuJPsiMuMuLep1Label");
  MuMuJPsiMuMuLep2Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuMuJPsiMuMuLep2Label");
  MuMuJPsiMuMuLep3Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuMuJPsiMuMuLep3Label");
  MuMuJPsiMuMuLep4Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuMuJPsiMuMuLep4Label");
  MuMuJPsiElElLep1Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuMuJPsiElElLep1Label");
  MuMuJPsiElElLep2Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuMuJPsiElElLep2Label");
  MuMuJPsiElElLep3Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuMuJPsiElElLep3Label");
  MuMuJPsiElElLep4Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuMuJPsiElElLep4Label");
  MuElJPsiMuMuLep1Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuElJPsiMuMuLep1Label");
  MuElJPsiMuMuLep2Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuElJPsiMuMuLep2Label");
  MuElJPsiMuMuLep3Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuElJPsiMuMuLep3Label");
  MuElJPsiMuMuLep4Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuElJPsiMuMuLep4Label");
  MuElJPsiElElLep1Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuElJPsiElElLep1Label");
  MuElJPsiElElLep2Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuElJPsiElElLep2Label");
  MuElJPsiElElLep3Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuElJPsiElElLep3Label");
  MuElJPsiElElLep4Label_ = cfg.getUntrackedParameter<edm::InputTag>("MuElJPsiElElLep4Label");
  ElElJPsiMuMuLep1Label_ = cfg.getUntrackedParameter<edm::InputTag>("ElElJPsiMuMuLep1Label");
  ElElJPsiMuMuLep2Label_ = cfg.getUntrackedParameter<edm::InputTag>("ElElJPsiMuMuLep2Label");
  ElElJPsiMuMuLep3Label_ = cfg.getUntrackedParameter<edm::InputTag>("ElElJPsiMuMuLep3Label");
  ElElJPsiMuMuLep4Label_ = cfg.getUntrackedParameter<edm::InputTag>("ElElJPsiMuMuLep4Label");
  ElElJPsiElElLep1Label_ = cfg.getUntrackedParameter<edm::InputTag>("ElElJPsiElElLep1Label");
  ElElJPsiElElLep2Label_ = cfg.getUntrackedParameter<edm::InputTag>("ElElJPsiElElLep2Label");
  ElElJPsiElElLep3Label_ = cfg.getUntrackedParameter<edm::InputTag>("ElElJPsiElElLep3Label");
  ElElJPsiElElLep4Label_ = cfg.getUntrackedParameter<edm::InputTag>("ElElJPsiElElLep4Label");

  produces<std::vector<cmg::Muon> >("Muons");
  produces<std::vector<cmg::Electron> >("Electrons");

}

CMGFinalLeptonProducer::~CMGFinalLeptonProducer()
{

}

void CMGFinalLeptonProducer::produce(edm::Event& iEvent, const edm::EventSetup& es)
{
  using namespace reco;

  std::auto_ptr<std::vector<cmg::Muon> > muons(new std::vector<cmg::Muon>());
  std::auto_ptr<std::vector<cmg::Electron> > electrons(new std::vector<cmg::Electron>());

  iEvent.getByLabel(MuMuLep1Label_, mmlep1_);
  iEvent.getByLabel(MuMuLep2Label_, mmlep2_);
  iEvent.getByLabel(MuElLep1Label_, melep1_);
  iEvent.getByLabel(MuElLep2Label_, melep2_);
  iEvent.getByLabel(ElElLep1Label_, eelep1_);
  iEvent.getByLabel(ElElLep2Label_, eelep2_);

  iEvent.getByLabel(MuMuJPsiMuMuLep1Label_, mm2mlep1_);
  iEvent.getByLabel(MuMuJPsiMuMuLep2Label_, mm2mlep2_);
  iEvent.getByLabel(MuMuJPsiMuMuLep3Label_, mm2mlep3_);
  iEvent.getByLabel(MuMuJPsiMuMuLep4Label_, mm2mlep4_);
  iEvent.getByLabel(MuMuJPsiElElLep1Label_, mm2elep1_);
  iEvent.getByLabel(MuMuJPsiElElLep2Label_, mm2elep2_);
  iEvent.getByLabel(MuMuJPsiElElLep3Label_, mm2elep3_);
  iEvent.getByLabel(MuMuJPsiElElLep4Label_, mm2elep4_);
  iEvent.getByLabel(MuElJPsiMuMuLep1Label_, me2mlep1_);
  iEvent.getByLabel(MuElJPsiMuMuLep2Label_, me2mlep2_);
  iEvent.getByLabel(MuElJPsiMuMuLep3Label_, me2mlep3_);
  iEvent.getByLabel(MuElJPsiMuMuLep4Label_, me2mlep4_);
  iEvent.getByLabel(MuElJPsiElElLep1Label_, me2elep1_);
  iEvent.getByLabel(MuElJPsiElElLep2Label_, me2elep2_);
  iEvent.getByLabel(MuElJPsiElElLep3Label_, me2elep3_);
  iEvent.getByLabel(MuElJPsiElElLep4Label_, me2elep4_);
  iEvent.getByLabel(ElElJPsiMuMuLep1Label_, ee2mlep1_);
  iEvent.getByLabel(ElElJPsiMuMuLep2Label_, ee2mlep2_);
  iEvent.getByLabel(ElElJPsiMuMuLep3Label_, ee2mlep3_);
  iEvent.getByLabel(ElElJPsiMuMuLep4Label_, ee2mlep4_);
  iEvent.getByLabel(ElElJPsiElElLep1Label_, ee2elep1_);
  iEvent.getByLabel(ElElJPsiElElLep2Label_, ee2elep2_);
  iEvent.getByLabel(ElElJPsiElElLep3Label_, ee2elep3_);
  iEvent.getByLabel(ElElJPsiElElLep4Label_, ee2elep4_);

  if( mmlep1_.isValid() && mmlep2_.isValid()  ) {
    if( mmlep1_->size() > 0 && mmlep2_->size() > 0 ){
     muons->push_back((*mmlep1_)[0]);
     muons->push_back((*mmlep2_)[0]);
    }
  }

  if( melep1_.isValid() && melep2_.isValid()  ) {
    if( melep1_->size() > 0 && melep2_->size() > 0 ){
     muons->push_back((*melep1_)[0]);
     electrons->push_back((*melep2_)[0]);
    }
  }

  if( eelep1_.isValid() && eelep2_.isValid()  ) {
    if( eelep1_->size() > 0 && eelep2_->size() > 0 ){
     electrons->push_back((*eelep1_)[0]);
     electrons->push_back((*eelep2_)[0]);
    }
  }

  if( mm2mlep1_.isValid() && mm2mlep2_.isValid() &&  mm2mlep3_.isValid() && mm2mlep4_.isValid() ) {
    if( mm2mlep1_->size() > 0 && mm2mlep2_->size() > 0 && mm2mlep3_->size() > 0 && mm2mlep4_->size() > 0){
     muons->push_back((*mm2mlep1_)[0]);
     muons->push_back((*mm2mlep2_)[0]);
    }
  }

  if( mm2elep1_.isValid() && mm2elep2_.isValid() &&  mm2elep3_.isValid() && mm2elep4_.isValid() ) {
    if( mm2elep1_->size() > 0 && mm2elep2_->size() > 0 && mm2elep3_->size() > 0 && mm2elep4_->size() > 0){
     muons->push_back((*mm2elep1_)[0]);
     muons->push_back((*mm2elep2_)[0]);
    }
  }

  if( me2mlep1_.isValid() && me2mlep2_.isValid() && me2mlep3_.isValid() && me2mlep4_.isValid() ) {
    if( me2mlep1_->size() > 0 && me2mlep2_->size() > 0 && me2mlep3_->size() > 0 && me2mlep4_->size() > 0 ){
     muons->push_back((*me2mlep1_)[0]);
     electrons->push_back((*me2mlep2_)[0]);
    }
  }

  if( me2elep1_.isValid() && me2elep2_.isValid() && me2elep3_.isValid() && me2elep4_.isValid() ) {
    if( me2elep1_->size() > 0 && me2elep2_->size() > 0 && me2elep3_->size() > 0 && me2elep4_->size() > 0 ){
     muons->push_back((*me2elep1_)[0]);
     electrons->push_back((*me2elep2_)[0]);
    }
  }

  if( ee2mlep1_.isValid() && ee2mlep2_.isValid() && ee2mlep3_.isValid() && ee2mlep4_.isValid() ) {
    if( ee2mlep1_->size() > 0 && ee2mlep2_->size() > 0 && ee2mlep3_->size() > 0 && ee2mlep4_->size() > 0){
     electrons->push_back((*ee2mlep1_)[0]);
     electrons->push_back((*ee2mlep2_)[0]);
    }
  }

  if( ee2elep1_.isValid() && ee2elep2_.isValid() && ee2elep3_.isValid() && ee2elep4_.isValid() ) {
    if( ee2elep1_->size() > 0 && ee2elep2_->size() > 0 && ee2elep3_->size() > 0 && ee2elep4_->size() > 0){
     electrons->push_back((*ee2elep1_)[0]);
     electrons->push_back((*ee2elep2_)[0]);
    }
  }

  iEvent.put(muons,"Muons");
  iEvent.put(electrons,"Electrons");
 
}

void 
CMGFinalLeptonProducer::beginJob(){
}


void
CMGFinalLeptonProducer::endJob() {
}


#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(CMGFinalLeptonProducer);



