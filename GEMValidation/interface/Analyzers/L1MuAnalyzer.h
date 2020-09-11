#ifndef GEMCode_GEMValidation_L1MuAnalyzer_h
#define GEMCode_GEMValidation_L1MuAnalyzer_h

#include "GEMCode/GEMValidation/interface/Helpers.h"
#include "GEMCode/GEMValidation/interface/MatcherSuperManager.h"
#include "GEMCode/GEMValidation/interface/TreeManager.h"

class L1MuAnalyzer
{
public:

  // constructor
  L1MuAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC);

  // destructor
  ~L1MuAnalyzer() {}

  void setMatcher(const L1MuMatcher& match_sh);

  // initialize the event
  void analyze(const edm::Event& ev, const edm::EventSetup& es, const MatcherSuperManager& manager, my::TreeManager& tree);
  void analyze(TreeManager& tree);

 private:

  edm::EDGetTokenT<l1t::EMTFTrackCollection> emtfTrackToken_;
  edm::EDGetTokenT<l1t::RegionalMuonCandBxCollection> emtfCandToken_;
  edm::EDGetTokenT<l1t::MuonBxCollection> muonToken_;

  edm::Handle<l1t::EMTFTrackCollection> emtfTrackHandle_;
  edm::Handle<l1t::RegionalMuonCandBxCollection> emtfCandHandle_;
  edm::Handle<l1t::MuonBxCollection> muonHandle_;

  std::shared_ptr<CSCStubMatcher> cscStubMatcher_;

  int minBXEMTFTrack_, maxBXEMTFTrack_;
  int verboseEMTFTrack_;
  bool runEMTFTrack_;

  int minBXRegMuCand_, maxBXRegMuCand_;
  int verboseRegMuCand_;
  bool runRegMuCand_;

  int minBXGMT_, maxBXGMT_;
  int verboseGMT_;
  bool runGMT_;

  std::unique_ptr<L1MuMatcher> match_;
};

#endif
