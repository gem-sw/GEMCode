#include "GEMCode/GEMValidation/interface/AnalyzerManager.h"

AnalyzerManager::AnalyzerManager(const MatchManager& manager)
{
  cscsh_.reset(new CSCSimHitAnalyzer(*manager.cscSimHits()));
  gemsh_.reset(new GEMSimHitAnalyzer(*manager.gemSimHits()));
  gemdg_.reset(new GEMDigiAnalyzer(*manager.gemDigis()));
  cscdg_.reset(new CSCDigiAnalyzer(*manager.cscDigis()));
  cscstub_.reset(new CSCStubAnalyzer(*manager.cscStubs()));
  l1mu_.reset(new L1MuAnalyzer(*manager.l1Muons()));
}

void AnalyzerManager::init(const edm::ParameterSet& conf)
{
  cscsh_->init(conf);
  gemsh_->init(conf);
  cscdg_->init(conf);
  gemdg_->init(conf);
  cscstub_->init(conf);
  l1mu_->init(conf);
}

void
AnalyzerManager::analyze(std::vector<gem::MyTrack>& track, std::vector<int> stations)
{
  cscsh_->analyze(track, stations);
  gemsh_->analyze(track, stations);
  cscdg_->analyze(track, stations);
  gemdg_->analyze(track, stations);
  cscstub_->analyze(track, stations);
  l1mu_->analyze(track);
}
