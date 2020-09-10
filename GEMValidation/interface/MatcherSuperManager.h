#ifndef GEMCode_GEMValidation_MatcherSuperManager_h
#define GEMCode_GEMValidation_MatcherSuperManager_h

#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "GEMCode/GEMValidation/interface/MatcherManager.h"

// container class with managers

class MatcherSuperManager
{
public:
  MatcherSuperManager(edm::ParameterSet const& iPS, edm::ConsumesCollector&& iC);

  ~MatcherSuperManager() {}

  /// do the matching
  void match(const edm::Event& e, const edm::EventSetup& eventSetup);

  bool isSimTrackGood(const SimTrack& t);

  // accessors
  std::vector<std::shared_ptr<MatcherManager> > matchers() const { return matchers_; }

private:
  // one manager per Sim-level particle we're fully analyzing
  std::vector<std::shared_ptr<MatcherManager> > matchers_;

  edm::EDGetTokenT<edm::SimVertexContainer> simVertexInput_;
  edm::EDGetTokenT<edm::SimTrackContainer> simTrackInput_;

  int verboseSimTrack_;
  double simTrackMinPt_;
  double simTrackMinEta_;
  double simTrackMaxEta_;
  int verbose_;
};

#endif
