#include "GEMCode/GEMValidation/interface/AnalyzerManager.h"

AnalyzerManager::AnalyzerManager(const edm::ParameterSet& conf)
{
  simt_.reset(new SimTrackAnalyzer(conf));
  cscsh_.reset(new CSCSimHitAnalyzer(conf));
  gemsh_.reset(new GEMSimHitAnalyzer(conf));
  gemdg_.reset(new GEMDigiAnalyzer(conf));
  cscdg_.reset(new CSCDigiAnalyzer(conf));
  cscstub_.reset(new CSCStubAnalyzer(conf));
  l1mu_.reset(new L1MuAnalyzer(conf));
  // l1track_.reset(new L1TrackAnalyzer(conf));
  // recotrack_.reset(new RecoTrackAnalyzer(conf));
}

void AnalyzerManager::init(const MatchManager& manager)
{
  cscsh_->init(*manager.cscSimHits());
  gemsh_->init(*manager.gemSimHits());
  cscdg_->init(*manager.cscDigis());
  gemdg_->init(*manager.gemDigis());
  cscstub_->init(*manager.cscStubs());
  l1mu_->init(*manager.l1Muons());;
  // l1track_->init(*manager.l1Tracks());;
  // recotrack_->init(*manager.recoTracks());;
}

void
AnalyzerManager::analyze(TreeManager& tree, const SimTrack& t)
{
  simt_->analyze(tree, t);
  cscsh_->analyze(tree);
  gemsh_->analyze(tree);
  cscdg_->analyze(tree);
  gemdg_->analyze(tree);
  cscstub_->analyze(tree);
  l1mu_->analyze(tree);
}
