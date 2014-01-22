#include "DataFormats/Common/interface/Wrapper.h"
#include "KoPFA/CMGDataFormats/interface/CMGTTbarCandidate.h"
#include "KoPFA/CMGDataFormats/interface/CMGTTbarJPsiCandidate.h"

#include <vector>

namespace {
  struct KoPFA_CMGAnalyzer {

    vallot::CMGTTbarCandidate dummyCMGTTbarCandidate;
    edm::Wrapper<vallot::CMGTTbarCandidate> dummyCMGTTbarCandidateWrapper;
    std::vector<vallot::CMGTTbarCandidate> dummyCMGTTbarCandidateCollection;
    edm::Wrapper<std::vector<vallot::CMGTTbarCandidate> > dummyCMGTTbarCandidateCollectionWrapper;
    edm::Ptr<vallot::CMGTTbarCandidate> dummyCMGTTbarCandidatePtr;

    vallot::CMGTTbarJPsiCandidate dummyCMGTTbarJPsiCandidate;
    edm::Wrapper<vallot::CMGTTbarJPsiCandidate> dummyCMGTTbarJPsiCandidateWrapper;
    std::vector<vallot::CMGTTbarJPsiCandidate> dummyCMGTTbarJPsiCandidateCollection;
    edm::Wrapper<std::vector<vallot::CMGTTbarJPsiCandidate> > dummyCMGTTbarJPsiCandidateCollectionWrapper;
    edm::Ptr<vallot::CMGTTbarJPsiCandidate> dummyCMGTTbarJPsiCandidatePtr;

  };

}
