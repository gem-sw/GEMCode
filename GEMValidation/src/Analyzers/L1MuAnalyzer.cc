#include "GEMCode/GEMValidation/interface/Analyzers/L1MuAnalyzer.h"

L1MuAnalyzer::L1MuAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC)
{
  const auto& emtfTrack = conf.getParameter<edm::ParameterSet>("emtfTrack");
  minBXEMTFTrack_ = emtfTrack.getParameter<int>("minBX");
  maxBXEMTFTrack_ = emtfTrack.getParameter<int>("maxBX");
  verboseEMTFTrack_ = emtfTrack.getParameter<int>("verbose");
  runEMTFTrack_ = emtfTrack.getParameter<bool>("run");

  const auto& emtfCand = conf.getParameter<edm::ParameterSet>("emtfCand");
  minBXRegMuCand_ = emtfCand.getParameter<int>("minBX");
  maxBXRegMuCand_ = emtfCand.getParameter<int>("maxBX");
  verboseRegMuCand_ = emtfCand.getParameter<int>("verbose");
  runRegMuCand_ = emtfCand.getParameter<bool>("run");

  const auto& muon = conf.getParameter<edm::ParameterSet>("muon");
  minBXGMT_ = muon.getParameter<int>("minBX");
  maxBXGMT_ = muon.getParameter<int>("maxBX");
  verboseGMT_ = muon.getParameter<int>("verbose");
  runGMT_ = muon.getParameter<bool>("run");

  emtfTrackToken_ = iC.consumes<l1t::EMTFTrackCollection>(emtfTrack.getParameter<edm::InputTag>("inputTag"));
  emtfCandToken_ = iC.consumes<l1t::RegionalMuonCandBxCollection>(emtfCand.getParameter<edm::InputTag>("inputTag"));
  muonToken_ = iC.consumes<l1t::MuonBxCollection>(muon.getParameter<edm::InputTag>("inputTag"));
}

void L1MuAnalyzer::setMatcher(const L1MuMatcher& match_sh)
{
  match_.reset(new L1MuMatcher(match_sh));
}

void L1MuAnalyzer::analyze(const edm::Event& ev, const edm::EventSetup& es, const MatcherSuperManager& manager, TreeManager& tree) {}

void L1MuAnalyzer::analyze(TreeManager& tree)
{
  const auto& emtfTrack = match_->emtfTrack();
  const auto& muon = match_->muon();

  if (emtfTrack != nullptr) {
    tree.l1mu().has_emtfTrack = 1;
    tree.l1mu().emtf_pt = emtfTrack->pt();
    tree.l1mu().emtf_eta = emtfTrack->eta();
    tree.l1mu().emtf_phi = emtfTrack->phi();

    tree.l1mu().hasME1 = emtfTrack->hasStub(1);
    tree.l1mu().hasME2 = emtfTrack->hasStub(2);
    tree.l1mu().hasME3 = emtfTrack->hasStub(3);
    tree.l1mu().hasME4 = emtfTrack->hasStub(4);
    tree.l1mu().nstubs = emtfTrack->nStubs();
    tree.l1mu().deltaR = emtfTrack->dR();
    tree.l1mu().chargesign = emtfTrack->charge();
  }

  if (muon != nullptr) {
    tree.l1mu().has_gmtCand = 1;
    tree.l1mu().bestdRGmtCand = muon->dR();
    tree.l1mu().L1Mu_pt = muon->pt();
    tree.l1mu().L1Mu_eta = muon->eta();
    tree.l1mu().L1Mu_phi = muon->phi();
    tree.l1mu().L1Mu_charge = muon->charge();
    tree.l1mu().L1Mu_bx = muon->bx();
    tree.l1mu().L1Mu_quality = muon->quality();
  }
}
