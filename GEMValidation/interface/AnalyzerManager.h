#ifndef GEMCode_GEMValidation_AnalyzerManager_h
#define GEMCode_GEMValidation_AnalyzerManager_h

#include "GEMCode/GEMValidation/interface/MatchManager.h"
#include "GEMCode/GEMValidation/interface/TreeManager.h"
#include "GEMCode/GEMValidation/interface/Analyzers/CSCSimHitAnalyzer.h"
#include "GEMCode/GEMValidation/interface/Analyzers/GEMSimHitAnalyzer.h"
#include "GEMCode/GEMValidation/interface/Analyzers/GEMDigiAnalyzer.h"
#include "GEMCode/GEMValidation/interface/Analyzers/CSCDigiAnalyzer.h"
#include "GEMCode/GEMValidation/interface/Analyzers/CSCStubAnalyzer.h"
#include "GEMCode/GEMValidation/interface/Analyzers/L1MuAnalyzer.h"

class AnalyzerManager
{
 public:
  AnalyzerManager(const edm::ParameterSet& conf);

  ~AnalyzerManager() {}

  /// initialize
  void init(const MatchManager&);

  /// do the matching
  void analyze(TreeManager& tree, const SimTrack& t);

 private:

  // analyzers
  std::unique_ptr<SimTrackAnalyzer> simt_;
  std::unique_ptr<CSCSimHitAnalyzer> cscsh_;
  std::unique_ptr<GEMSimHitAnalyzer> gemsh_;
  std::unique_ptr<CSCDigiAnalyzer> cscdg_;
  std::unique_ptr<GEMDigiAnalyzer> gemdg_;
  std::unique_ptr<CSCStubAnalyzer> cscstub_;
  std::unique_ptr<L1MuAnalyzer> l1mu_;
};

#endif
