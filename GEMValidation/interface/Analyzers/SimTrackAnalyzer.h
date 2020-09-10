#ifndef GEMCode_GEMValidation_SimTrackAnalyzer_h
#define GEMCode_GEMValidation_SimTrackAnalyzer_h

#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"
#include "GEMCode/GEMValidation/interface/Helpers.h"
#include "GEMCode/GEMValidation/interface/TreeManager.h"

class SimTrackAnalyzer
{
public:

  // constructor
  SimTrackAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC);

  // destructor
  ~SimTrackAnalyzer() {}

  void init();

  // initialize the event
  void analyze(TreeManager& tree, const SimTrack& t, const SimVertex& v);
};

#endif
