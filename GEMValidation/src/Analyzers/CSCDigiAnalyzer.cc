#include "GEMCode/GEMValidation/interface/Analyzers/CSCDigiAnalyzer.h"

CSCDigiAnalyzer::CSCDigiAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC)
{
  minNHitsChamber_ = conf.getParameter<int>("minNHitsChamberCSCDigi");

  const auto& wireDigi = conf.getParameterSet("cscWireDigi");
  verboseWG_ = wireDigi.getParameter<int>("verbose");
  minBXWire_ = wireDigi.getParameter<int>("minBX");
  maxBXWire_ = wireDigi.getParameter<int>("maxBX");

  const auto& comparatorDigi = conf.getParameterSet("cscComparatorDigi");
  verboseComparator_ = comparatorDigi.getParameter<int>("verbose");
  minBXComparator_ = comparatorDigi.getParameter<int>("minBX");
  maxBXComparator_ = comparatorDigi.getParameter<int>("maxBX");

  const auto& stripDigi = conf.getParameterSet("cscStripDigi");
  verboseStrip_ = stripDigi.getParameter<int>("verbose");
  minBXStrip_ = stripDigi.getParameter<int>("minBX");
  maxBXStrip_ = stripDigi.getParameter<int>("maxBX");

  comparatorDigiInput_ =
      iC.consumes<CSCComparatorDigiCollection>(comparatorDigi.getParameter<edm::InputTag>("inputTag"));
  stripDigiInput_ = iC.consumes<CSCStripDigiCollection>(stripDigi.getParameter<edm::InputTag>("inputTag"));
  wireDigiInput_ = iC.consumes<CSCWireDigiCollection>(wireDigi.getParameter<edm::InputTag>("inputTag"));
}

void CSCDigiAnalyzer::setMatcher(const CSCDigiMatcher& match_sh)
{
  match_.reset(new CSCDigiMatcher(match_sh));
}

void CSCDigiAnalyzer::analyze(const edm::Event& ev, const edm::EventSetup& es, const MatcherSuperManager& manager, my::TreeManager& tree)
{
}

void CSCDigiAnalyzer::analyze(TreeManager& tree)
{
  // CSC strip digis
  for(const auto& d: match_->chamberIdsStrip(0)) {
    CSCDetId id(d);

    const int st(gem::detIdToMEStation(id.station(),id.ring()));

    const int nlayers(match_->nLayersWithStripInChamber(d));

    if (nlayers < minNHitsChamber_) continue;

    const bool odd(id.chamber()%2==1);

    if (odd) tree.cscDigi().has_csc_strips_odd[st] = true;
    else     tree.cscDigi().has_csc_strips_even[st] = true;

    if (odd) tree.cscDigi().nlayers_st_dg_odd[st] = nlayers;
    else     tree.cscDigi().nlayers_st_dg_even[st] = nlayers;

    // case ME11
    if (st==1 or st==2){
      if (odd) tree.cscDigi().has_csc_strips_odd[0] = true;
      else     tree.cscDigi().has_csc_strips_even[0] = true;

      if (odd) tree.cscDigi().nlayers_st_dg_odd[0] = nlayers;
      else     tree.cscDigi().nlayers_st_dg_even[0] = nlayers;
    }
  }

  // CSC wire digis
  for(const auto& d: match_->chamberIdsWire(0)) {
    CSCDetId id(d);
    const int st(gem::detIdToMEStation(id.station(),id.ring()));

    const int nlayers(match_->nLayersWithWireInChamber(d));
    if (nlayers < minNHitsChamber_) continue;

    const bool odd(id.chamber()%2==1);

    if (odd) tree.cscDigi().has_csc_wires_odd[st] = true;
    else tree.cscDigi().has_csc_wires_even[st] = true;

    if (odd) tree.cscDigi().nlayers_wg_dg_odd[st] = nlayers;
    else tree.cscDigi().nlayers_wg_dg_even[st] = nlayers;

    // case ME11
    if (st==1 or st==2){
      if (odd) tree.cscDigi().has_csc_wires_odd[0] = true;
      else tree.cscDigi().has_csc_wires_even[0] = true;

      if (odd) tree.cscDigi().nlayers_wg_dg_odd[0] = nlayers;
      else tree.cscDigi().nlayers_wg_dg_even[0] = nlayers;
    }
  }
}
