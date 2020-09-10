// CMSSW
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

// Private code
#include "GEMCode/GEMValidation/interface/MatcherManager.h"
#include "GEMCode/GEMValidation/interface/AnalyzerManager.h"
#include "GEMCode/GEMValidation/interface/TreeManager.h"

class MuonNtuplizer : public edm::one::EDAnalyzer<> {
public:
  explicit MuonNtuplizer(const edm::ParameterSet&);

  ~MuonNtuplizer() {}

  virtual void analyze(const edm::Event&, const edm::EventSetup&);

private:
  void analyze(const SimTrack& t, const SimVertex& v);

  std::unique_ptr<TreeManager> tree_;
  std::unique_ptr<MatcherManager> matcher_;
  std::unique_ptr<AnalyzerManager> analyzer_;
};

MuonNtuplizer::MuonNtuplizer(const edm::ParameterSet& ps)
{
  // book the trees
  tree_.reset(new TreeManager());
  tree_->book();

  // define new matchers
  matcher_.reset(new MatcherManager(ps, consumesCollector()));

  // define new analyzers
  analyzer_.reset(new AnalyzerManager(ps, consumesCollector()));
}

void MuonNtuplizer::analyze(const edm::Event& ev, const edm::EventSetup& es) {
  // reset all structs
  tree_->init();

  // set event and setup
  matcher_->init(ev, es);
  analyzer_->init(ev, es);

  // match the track
  matcher_->match(ev, es);

  // initialize the track analyzers
  analyzer_->setManager(*matcher_);
  analyzer_->setTree(*tree_);

  // analyze the track
  analyzer_->analyze(ev, es);

  // fill all trees
  tree_->fill();
}

DEFINE_FWK_MODULE(MuonNtuplizer);
