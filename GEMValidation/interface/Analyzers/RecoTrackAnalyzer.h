#ifndef GEMCode_GEMValidation_RecoTrackAnalyzer_h
#define GEMCode_GEMValidation_RecoTrackAnalyzer_h

#include "GEMCode/GEMValidation/interface/Helpers.h"
#include "GEMCode/GEMValidation/interface/MatchManager.h"
#include "GEMCode/GEMValidation/interface/TreeManager.h"

class RecoTrackAnalyzer
{
public:

  // constructor
  RecoTrackAnalyzer(const RecoTrackMatcher& match_sh);

  // destructor
  ~RecoTrackAnalyzer() {}

  void init(const edm::ParameterSet& conf);

  // initialize the event
  void analyze(TreeManager& tree);

 private:

  std::unique_ptr<RecoTrackMatcher> match_;
};

#endif
