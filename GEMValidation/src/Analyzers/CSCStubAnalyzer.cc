#include "GEMCode/GEMValidation/interface/Analyzers/CSCStubAnalyzer.h"
#include "GEMCode/GEMValidation/interface/Helpers.h"
#include "L1Trigger/CSCCommonTrigger/interface/CSCPatternLUT.h"

CSCStubAnalyzer::CSCStubAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC)
{
  minNHitsChamber_ = conf.getParameter<int>("minNHitsChamberCSCStub");

  const auto& cscCLCT = conf.getParameter<edm::ParameterSet>("cscCLCT");
  minBXCLCT_ = cscCLCT.getParameter<int>("minBX");
  maxBXCLCT_ = cscCLCT.getParameter<int>("maxBX");
  verboseCLCT_ = cscCLCT.getParameter<int>("verbose");

  const auto& cscALCT = conf.getParameter<edm::ParameterSet>("cscALCT");
  minBXALCT_ = cscALCT.getParameter<int>("minBX");
  maxBXALCT_ = cscALCT.getParameter<int>("maxBX");
  verboseALCT_ = cscALCT.getParameter<int>("verbose");

  const auto& cscLCT = conf.getParameter<edm::ParameterSet>("cscLCT");
  minBXLCT_ = cscLCT.getParameter<int>("minBX");
  maxBXLCT_ = cscLCT.getParameter<int>("maxBX");
  verboseLCT_ = cscLCT.getParameter<int>("verbose");

  const auto& cscMPLCT = conf.getParameter<edm::ParameterSet>("cscMPLCT");
  minBXMPLCT_ = cscMPLCT.getParameter<int>("minBX");
  maxBXMPLCT_ = cscMPLCT.getParameter<int>("maxBX");
  verboseMPLCT_ = cscMPLCT.getParameter<int>("verbose");

  clctToken_ = iC.consumes<CSCCLCTDigiCollection>(cscCLCT.getParameter<edm::InputTag>("inputTag"));
  alctToken_ = iC.consumes<CSCALCTDigiCollection>(cscALCT.getParameter<edm::InputTag>("inputTag"));
  lctToken_ = iC.consumes<CSCCorrelatedLCTDigiCollection>(cscLCT.getParameter<edm::InputTag>("inputTag"));
  mplctToken_ = iC.consumes<CSCCorrelatedLCTDigiCollection>(cscMPLCT.getParameter<edm::InputTag>("inputTag"));

  positionLUTFiles_ = conf.getParameter<std::vector<std::string>>("positionLUTFiles");
  positionFloatLUTFiles_ = conf.getParameter<std::vector<std::string>>("positionFloatLUTFiles");
  slopeLUTFiles_ = conf.getParameter<std::vector<std::string>>("slopeLUTFiles");
  slopeFloatLUTFiles_ = conf.getParameter<std::vector<std::string>>("slopeFloatLUTFiles");
  patternConversionLUTFiles_ = conf.getParameter<std::vector<std::string>>("patternConversionLUTFiles");

  for (int i = 0; i < 5; ++i) {
    lutpos_[i] = std::make_unique<CSCComparatorCodeLUT>(positionLUTFiles_[i]);
    lutposfloat_[i] = std::make_unique<CSCComparatorCodeLUT>(positionFloatLUTFiles_[i]);
    lutslope_[i] = std::make_unique<CSCComparatorCodeLUT>(slopeLUTFiles_[i]);
    lutslopefloat_[i] = std::make_unique<CSCComparatorCodeLUT>(slopeFloatLUTFiles_[i]);
    lutpatconv_[i] = std::make_unique<CSCComparatorCodeLUT>(patternConversionLUTFiles_[i]);
  }
}

void CSCStubAnalyzer::init(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  iSetup.get<MuonGeometryRecord>().get(csc_geom_);
  if (csc_geom_.isValid()) {
  cscGeometry_ = &*csc_geom_;
  } else {
    std::cout << "+++ Info: CSC geometry is unavailable. +++\n";
  }

  iSetup.get<MuonGeometryRecord>().get(gem_geom_);
  if (gem_geom_.isValid()) {
  gemGeometry_ = &*gem_geom_;
  } else {
    std::cout << "+++ Info: GEM geometry is unavailable. +++\n";
  }
}

void CSCStubAnalyzer::setMatcher(const CSCStubMatcher& match_sh)
{
  match_.reset(new CSCStubMatcher(match_sh));
}

void CSCStubAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup, const MatcherSuperManager& manager, my::TreeManager& tree)
{
  iSetup.get<MuonGeometryRecord>().get(csc_geom_);
  if (csc_geom_.isValid()) {
  cscGeometry_ = &*csc_geom_;
  } else {
    std::cout << "+++ Info: CSC geometry is unavailable. +++\n";
  }

  iSetup.get<MuonGeometryRecord>().get(gem_geom_);
  if (gem_geom_.isValid()) {
  gemGeometry_ = &*gem_geom_;
  } else {
    std::cout << "+++ Info: GEM geometry is unavailable. +++\n";
  }

  iEvent.getByToken(clctToken_, clctsH_);
  iEvent.getByToken(alctToken_, alctsH_);
  iEvent.getByToken(lctToken_, lctsH_);
  iEvent.getByToken(mplctToken_, mplctsH_);

  const CSCCLCTDigiCollection& clcts = *clctsH_.product();
  const CSCALCTDigiCollection& alcts = *alctsH_.product();
  const CSCCorrelatedLCTDigiCollection& lcts = *lctsH_.product();
  const CSCCorrelatedLCTDigiCollection& mplcts = *mplctsH_.product();

  auto& cscTree = tree.cscStub();

  // CSC ALCTs
  for (auto detUnitIt = alcts.begin(); detUnitIt != alcts.end(); detUnitIt++) {
    const CSCDetId& id = (*detUnitIt).first;
    const bool isodd = (id.chamber()%2 == 1);
    const auto& range = (*detUnitIt).second;
    for (auto digiIt = range.first; digiIt != range.second; digiIt++) {

      if (!(*digiIt).isValid())
        continue;

      // check that the BX for this stub wasn't too early or too late
      if (digiIt->getBX() < minBXALCT_ || digiIt->getBX() > maxBXALCT_)
        continue;

      int tpidfound = -1;
      // check if it was matched to a simtrack
      for (int tpid = 0; tpid < MAX_PARTICLES; tpid++) {
        const auto& lctMatch = manager.matcher(tpid)->cscStubs()->bestAlctInChamber(id.rawId());
        // check if the same
        if (*digiIt == lctMatch) {
          tpidfound =  tpid;
          break;
        }
      }

      cscTree.alct_bx->push_back(digiIt->getBX());
      cscTree.alct_wg->push_back(digiIt->getKeyWG());
      cscTree.alct_quality->push_back(digiIt->getQuality());
      cscTree.alct_isodd->push_back(isodd);
      cscTree.alct_region->push_back(id.zendcap());
      cscTree.alct_station->push_back(id.station());
      cscTree.alct_ring->push_back(id.ring());
      cscTree.alct_chamber->push_back(id.chamber());
      cscTree.alct_tpid->push_back(tpidfound);
    }
  }

  // CSC CLCTs
  for (auto detUnitIt = clcts.begin(); detUnitIt != clcts.end(); detUnitIt++) {
    const CSCDetId& id = (*detUnitIt).first;
    const bool isodd = (id.chamber()%2 == 1);
    const auto& range = (*detUnitIt).second;
    for (auto digiIt = range.first; digiIt != range.second; digiIt++) {

      if (!(*digiIt).isValid())
        continue;

      // check that the BX for this stub wasn't too early or too late
      if (digiIt->getBX() < minBXCLCT_ || digiIt->getBX() > maxBXCLCT_)
        continue;

      int tpidfound = -1;
      // check if it was matched to a simtrack
      for (int tpid = 0; tpid < MAX_PARTICLES; tpid++) {
        const auto& lctMatch = manager.matcher(tpid)->cscStubs()->bestClctInChamber(id.rawId());
        // check if the same
        if (*digiIt == lctMatch) {
          tpidfound =  tpid;
          break;
        }
      }

      cscTree.clct_bx->push_back(digiIt->getBX());
      cscTree.clct_quality->push_back(digiIt->getQuality());
      cscTree.clct_isodd->push_back(isodd);
      cscTree.clct_region->push_back(id.zendcap());
      cscTree.clct_station->push_back(id.station());
      cscTree.clct_ring->push_back(id.ring());
      cscTree.clct_chamber->push_back(id.chamber());
      cscTree.clct_tpid->push_back(tpidfound);
    }
  }

  // CSC LCTs
  for (auto detUnitIt = lcts.begin(); detUnitIt != lcts.end(); detUnitIt++) {
    const CSCDetId& id = (*detUnitIt).first;
    const bool isodd = (id.chamber()%2 == 1);
    const auto& range = (*detUnitIt).second;
    for (auto digiIt = range.first; digiIt != range.second; digiIt++) {

      if (!(*digiIt).isValid())
        continue;

      // check that the BX for this stub wasn't too early or too late
      if (digiIt->getBX() < minBXLCT_ || digiIt->getBX() > maxBXLCT_)
        continue;

      int tpidfound = -1;
      // check if it was matched to a simtrack
      for (int tpid = 0; tpid < MAX_PARTICLES; tpid++) {
        const auto& lctMatch = manager.matcher(tpid)->cscStubs()->bestLctInChamber(id.rawId());
        // check if the same
        if (*digiIt == lctMatch) {
          tpidfound =  tpid;
          break;
        }
      }

      cscTree.lct_bx->push_back(digiIt->getBX());
      cscTree.lct_quality->push_back(digiIt->getQuality());
      cscTree.lct_isodd->push_back(isodd);
      cscTree.lct_region->push_back(id.zendcap());
      cscTree.lct_station->push_back(id.station());
      cscTree.lct_ring->push_back(id.ring());
      cscTree.lct_chamber->push_back(id.chamber());
      cscTree.lct_tpid->push_back(tpidfound);
    }
  }

  // CSC MPLCTs
  for (auto detUnitIt = mplcts.begin(); detUnitIt != mplcts.end(); detUnitIt++) {
    const CSCDetId& id = (*detUnitIt).first;
    const bool isodd = (id.chamber()%2 == 1);
    const auto& range = (*detUnitIt).second;
    for (auto digiIt = range.first; digiIt != range.second; digiIt++) {

      if (!(*digiIt).isValid())
        continue;

      // check that the BX for this stub wasn't too early or too late
      if (digiIt->getBX() < minBXMPLCT_ || digiIt->getBX() > maxBXMPLCT_)
        continue;

      int tpidfound = -1;
      // check if it was matched to a simtrack
      for (int tpid = 0; tpid < MAX_PARTICLES; tpid++) {
        const auto& lctMatch = manager.matcher(tpid)->cscStubs()->bestLctInChamber(id.rawId());
        // check if the same
        if (*digiIt == lctMatch) {
          tpidfound =  tpid;
          break;
        }
      }

      cscTree.mplct_bx->push_back(digiIt->getBX());
      cscTree.mplct_quality->push_back(digiIt->getQuality());
      cscTree.mplct_isodd->push_back(isodd);
      cscTree.mplct_region->push_back(id.zendcap());
      cscTree.mplct_station->push_back(id.station());
      cscTree.mplct_ring->push_back(id.ring());
      cscTree.mplct_chamber->push_back(id.chamber());
      cscTree.mplct_tpid->push_back(tpidfound);
    }
  }
}

void CSCStubAnalyzer::analyze(TreeManager& tree)
{
  // CSC CLCTs
  for(const auto& d: match_->chamberIdsCLCT(0)) {
    CSCDetId id(d);

    const int st(gem::detIdToMEStation(id.station(),id.ring()));

    const bool odd(id.chamber()%2==1);
    const auto& clct = match_->bestClctInChamber(d);

    if (!clct.isValid()) continue;

    const float slope(clct.getFloatSlope());

    int deltaStrip = 0;
    if (id.station() == 1 and id.ring() == 4 and clct.getKeyStrip() > CSCConstants::MAX_HALF_STRIP_ME1B)
      deltaStrip = CSCConstants::MAX_NUM_STRIPS_ME1B;

    float fpos = -9;
    if (clct.getCompCode() != -1) {
      fpos = clct.getKeyStrip() + lutposfloat_[clct.getRun3Pattern()]->lookup(clct.getCompCode());
      std::cout << "fpos " << fpos / 2. << " "
                << tree.cscSimHit().strip_csc_sh_odd[st] + deltaStrip << " "
                << tree.cscSimHit().strip_csc_sh_even[st] + deltaStrip << std::endl;
    }

    auto fill = [clct, odd, slope, tree, deltaStrip, id, fpos](gem::CSCStubStruct& cscStubTree, int st) mutable {
      if (odd) {
        cscStubTree.has_clct_odd[st] = true;
        cscStubTree.quality_clct_odd[st] = clct.getQuality();
        cscStubTree.pattern_clct_odd[st] = clct.getPattern();
        cscStubTree.bx_clct_odd[st] = clct.getBX();
        cscStubTree.hs_clct_odd[st] = clct.getKeyStrip();
        cscStubTree.qs_clct_odd[st] = clct.getKeyStrip(4);
        cscStubTree.es_clct_odd[st] = clct.getKeyStrip(8);
        cscStubTree.slope_clct_odd[st] = slope / 2.;
        cscStubTree.ffhs_clct_odd[st] = fpos/2.;
        cscStubTree.fhs_clct_odd[st] = clct.getFractionalStrip(2);
        cscStubTree.fqs_clct_odd[st] = clct.getFractionalStrip(4);
        cscStubTree.fes_clct_odd[st] = clct.getFractionalStrip(8);
        // position deltas
        cscStubTree.delta_ffhs_clct_odd[st] = cscStubTree.ffhs_clct_odd[st] - deltaStrip - tree.cscSimHit().strip_csc_sh_odd[st];
        cscStubTree.delta_fhs_clct_odd[st] = cscStubTree.fhs_clct_odd[st] - deltaStrip - tree.cscSimHit().strip_csc_sh_odd[st];
        cscStubTree.delta_fqs_clct_odd[st] = cscStubTree.fqs_clct_odd[st] - deltaStrip - tree.cscSimHit().strip_csc_sh_odd[st];
        cscStubTree.delta_fes_clct_odd[st] = cscStubTree.fes_clct_odd[st] - deltaStrip - tree.cscSimHit().strip_csc_sh_odd[st];
        // bending deltas
        cscStubTree.dslope_clct_odd[st] = cscStubTree.slope_clct_odd[st] - tree.cscSimHit().bend_csc_sh_odd[st];
        std::cout << "CSCStubAnalyzer " << id << " " << clct << " " << cscStubTree.slope_clct_odd[st] << " " << tree.cscSimHit().bend_csc_sh_odd[st] << " " <<  cscStubTree.dslope_clct_odd[st] << " " << fpos << std::endl;
      }
      else {
        cscStubTree.has_clct_even[st] = true;
        cscStubTree.quality_clct_even[st] = clct.getQuality();
        cscStubTree.pattern_clct_even[st] = clct.getPattern();
        cscStubTree.bx_clct_even[st] = clct.getBX();
        cscStubTree.hs_clct_even[st] = clct.getKeyStrip();
        cscStubTree.qs_clct_even[st] = clct.getKeyStrip(4);
        cscStubTree.es_clct_even[st] = clct.getKeyStrip(8);
        cscStubTree.slope_clct_even[st] = slope / 2.;
        cscStubTree.ffhs_clct_even[st] = fpos / 2.;
        cscStubTree.fhs_clct_even[st] = clct.getFractionalStrip(2);
        cscStubTree.fqs_clct_even[st] = clct.getFractionalStrip(4);
        cscStubTree.fes_clct_even[st] = clct.getFractionalStrip(8);
        // position deltas
        cscStubTree.delta_ffhs_clct_even[st] = cscStubTree.ffhs_clct_even[st] - deltaStrip - tree.cscSimHit().strip_csc_sh_even[st];
        cscStubTree.delta_fhs_clct_even[st] = cscStubTree.fhs_clct_even[st] - deltaStrip - tree.cscSimHit().strip_csc_sh_even[st];
        cscStubTree.delta_fqs_clct_even[st] = cscStubTree.fqs_clct_even[st] - deltaStrip - tree.cscSimHit().strip_csc_sh_even[st];
        cscStubTree.delta_fes_clct_even[st] = cscStubTree.fes_clct_even[st] - deltaStrip - tree.cscSimHit().strip_csc_sh_even[st];
        // bending deltas
        cscStubTree.dslope_clct_even[st] = cscStubTree.slope_clct_even[st] - tree.cscSimHit().bend_csc_sh_even[st];
        std::cout << "CSCStubAnalyzer " << id << " " << clct << " " << cscStubTree.slope_clct_even[st] << " " << tree.cscSimHit().bend_csc_sh_even[st] << " " <<  cscStubTree.dslope_clct_even[st] << " " << fpos << std::endl;
      }
    };

    fill(tree.cscStub(), st);
    // case ME11
    if (st==1 or st==2) {
      fill(tree.cscStub(), 0);
    }
  }

  // CSC ALCTs
  for(const auto& d: match_->chamberIdsALCT(0)) {
    CSCDetId id(d);
    const int st(gem::detIdToMEStation(id.station(),id.ring()));

    const bool odd(id.chamber()%2==1);
    const auto& alct = match_->bestAlctInChamber(d);

    if (!alct.isValid()) continue;

    auto fill = [alct, odd](gem::CSCStubStruct& cscStubTree, int st) mutable {
      if (odd) {
        cscStubTree.has_alct_odd[st] = true;
        cscStubTree.wg_alct_odd[st] = alct.getKeyWG();
        cscStubTree.quality_alct_odd[st] = alct.getQuality();
        cscStubTree.bx_alct_odd[st] = alct.getBX();
      }
      else {
        cscStubTree.has_alct_even[st] = true;
        cscStubTree.wg_alct_even[st] = alct.getKeyWG();
        cscStubTree.quality_alct_even[st] = alct.getQuality();
        cscStubTree.bx_alct_even[st] = alct.getBX();
      }
    };

    fill(tree.cscStub(), st);
    // case ME11
    if (st==1 or st==2){
      fill(tree.cscStub(), 0);
    }
  }

  // CSC LCTs
  for(const auto& d: match_->chamberIdsLCT(0)) {
    CSCDetId id(d);
    const int st(gem::detIdToMEStation(id.station(),id.ring()));
    const int gemstation(id.station());

    const auto& lct = match_->bestLctInChamber(d);

    if (!lct.isValid()) continue;

    const GlobalPoint& gp = match_->getGlobalPosition(d, lct);

    const bool odd(id.chamber()%2==1);

    auto fill = [lct, gp, odd](gem::CSCStubStruct& cscStubTree, int st) mutable {
      if (odd) {
        cscStubTree.has_lct_odd[st] = true;
        cscStubTree.bend_lct_odd[st] = lct.getPattern();
        cscStubTree.phi_lct_odd[st] = gp.phi();
        cscStubTree.eta_lct_odd[st] = gp.eta();
        cscStubTree.perp_lct_odd[st] = gp.perp();
        cscStubTree.bx_lct_odd[st] = lct.getBX();
        cscStubTree.hs_lct_odd[st] = lct.getStrip();
        cscStubTree.qs_lct_odd[st] = lct.getStrip(4);
        cscStubTree.es_lct_odd[st] = lct.getStrip(8);
        cscStubTree.wg_lct_odd[st] = lct.getKeyWG();
        cscStubTree.quality_lct_odd[st] = lct.getQuality();
      }
      else {
        cscStubTree.has_lct_even[st] = true;
        cscStubTree.bend_lct_even[st] = lct.getPattern();
        cscStubTree.phi_lct_even[st] = gp.phi();
        cscStubTree.eta_lct_even[st] = gp.eta();
        cscStubTree.perp_lct_even[st] = gp.perp();
        cscStubTree.bx_lct_even[st] = lct.getBX();
        cscStubTree.hs_lct_even[st] = lct.getStrip();
        cscStubTree.qs_lct_odd[st] = lct.getStrip(4);
        cscStubTree.es_lct_odd[st] = lct.getStrip(8);
        cscStubTree.wg_lct_even[st] = lct.getKeyWG();
        cscStubTree.quality_lct_even[st] = lct.getQuality();
      }
    };

    fill(tree.cscStub(), st);
    // case ME11
    if (st==1 or st==2){
      fill(tree.cscStub(), 0);
    }

    // only for ME1/1 and ME2/1
    if (st==1 or st==2 or st==5) continue;

    // require at least one GEM pad present...
    if (! (tree.gemStub().has_gem_pad_even[gemstation] or
           tree.gemStub().has_gem_pad_odd[gemstation] ) ) continue;

    if (odd) {
      tree.gemStub().dphi_lct_pad1_odd[gemstation]
        = reco::deltaPhi(float(tree.gemStub().phi_pad1_odd[st]),
                         float(tree.cscStub().phi_lct_odd[gemstation]));
      tree.gemStub().dphi_lct_pad2_odd[gemstation]
        = reco::deltaPhi(float(tree.gemStub().phi_pad2_odd[st]),
                         float(tree.cscStub().phi_lct_odd[gemstation]));
    } else {
      tree.gemStub().dphi_lct_pad1_even[gemstation]
        = reco::deltaPhi(float(tree.gemStub().phi_pad1_even[st]),
                         float(tree.cscStub().phi_lct_even[gemstation]));
      tree.gemStub().dphi_lct_pad2_even[gemstation]
        = reco::deltaPhi(float(tree.gemStub().phi_pad2_even[st]),
                         float(tree.cscStub().phi_lct_even[gemstation]));
    }

    // require at least one GEM pad present...
    if (! (tree.gemStub().has_gem_copad_even[gemstation] or
           tree.gemStub().has_gem_copad_odd[gemstation] ) ) continue;

    if (odd) {
      tree.gemStub().dphi_lct_copad_odd[gemstation]
        = reco::deltaPhi(float(tree.gemStub().phi_copad_odd[st]),
                         float(tree.cscStub().phi_lct_odd[gemstation]));
    } else {
      tree.gemStub().dphi_lct_copad_even[gemstation]
        = reco::deltaPhi(float(tree.gemStub().phi_copad_even[st]),
                         float(tree.cscStub().phi_lct_even[gemstation]));
    }
  }
}

float CSCStubAnalyzer::getSlope(const CSCCLCTDigi& lct) const {
  // std::cout << "halfstrip " << lct.getFractionalStrip(2) << " run-3 pattern " << lct.getRun3Pattern() << " slope " << lct.getSlope() << " run-3 slope " << lct.getFloatSlope(5) << std::endl;
  // for (const auto& p : lct.getHits()) {
  //   for (auto q : p) {
  //     std::cout << "\t" << q/2. << std::endl;
  //   }
  // }

  return lct.getFloatSlope();
}

std::pair<GEMDigi, GlobalPoint>
CSCStubAnalyzer::bestGEMDigi(const GEMDetId& gemId,
                             const GEMDigiContainer& gem_digis,
                             const GlobalPoint& csc_gp) const
{
  GlobalPoint gp;
  GEMDigi best_digi;
  auto emptyValue = make_pair(best_digi, gp);

  // no valid GEM digis
  if (gem_digis.empty()) return emptyValue;

  // invalid CSC stub
  if (std::abs(csc_gp.z()) < 0.001) return emptyValue;

  float bestDR2 = 999.;
  for (const auto& d: gem_digis) {
    const LocalPoint& lp = gemGeometry_->etaPartition(gemId)->centreOfStrip(d.strip());
    const GlobalPoint& gem_gp = gemGeometry_->idToDet(gemId)->surface().toGlobal(lp);

    // in deltaR calculation, give x20 larger weight to deltaPhi to make them comparable
    // but with slight bias towards dphi:
    float dphi = 20. * reco::deltaPhi(float(csc_gp.phi()), float(gem_gp.phi()));
    float deta = csc_gp.eta() - gem_gp.eta();
    float dR2 = dphi*dphi + deta*deta;
    // current gp is closer in phi then the previous
    if (dR2 < bestDR2) {
      gp = gem_gp;
      best_digi = d;
      bestDR2 = dR2;
    }
  }
  return emptyValue;
}


std::pair<GEMPadDigi, GlobalPoint>
CSCStubAnalyzer::bestGEMPadDigi(const GEMDetId& gemId,
                                const GEMPadDigiContainer& gem_digis,
                                const GlobalPoint& csc_gp) const
{
  GlobalPoint gp;
  GEMPadDigi best_digi;
  auto emptyValue = make_pair(best_digi, gp);

  // no valid GEM digis
  if (gem_digis.empty()) return emptyValue;

  // invalid CSC stub
  if (std::abs(csc_gp.z()) < 0.001) return emptyValue;

  float bestDR2 = 999.;
  for (const auto& d: gem_digis) {
    const LocalPoint& lp = gemGeometry_->etaPartition(gemId)->centreOfPad(d.pad());
    const GlobalPoint& gem_gp = gemGeometry_->idToDet(gemId)->surface().toGlobal(lp);

    // in deltaR calculation, give x20 larger weight to deltaPhi to make them comparable
    // but with slight bias towards dphi:
    float dphi = 20. * reco::deltaPhi(float(csc_gp.phi()), float(gem_gp.phi()));
    float deta = csc_gp.eta() - gem_gp.eta();
    float dR2 = dphi*dphi + deta*deta;
    // current gp is closer in phi then the previous
    if (dR2 < bestDR2) {
      gp = gem_gp;
      best_digi = d;
      bestDR2 = dR2;
    }
  }
  return emptyValue;
}


std::pair<GEMCoPadDigi, GlobalPoint>
CSCStubAnalyzer::bestGEMCoPadDigi(const GEMDetId& gemId,
                                  const GEMCoPadDigiContainer& gem_digis,
                                  const GlobalPoint& csc_gp) const
{
  GlobalPoint gp;
  GEMCoPadDigi best_digi;
  auto emptyValue = make_pair(best_digi, gp);

  // no valid GEM digis
  if (gem_digis.empty()) return emptyValue;

  // invalid CSC stub
  if (std::abs(csc_gp.z()) < 0.001) return emptyValue;

  float bestDR2 = 999.;
  for (const auto& d: gem_digis) {
    const LocalPoint& lp = gemGeometry_->etaPartition(gemId)->centreOfPad(d.pad(1));
    const GlobalPoint& gem_gp = gemGeometry_->idToDet(gemId)->surface().toGlobal(lp);

    // in deltaR calculation, give x20 larger weight to deltaPhi to make them comparable
    // but with slight bias towards dphi:
    float dphi = 20. * reco::deltaPhi(float(csc_gp.phi()), float(gem_gp.phi()));
    float deta = csc_gp.eta() - gem_gp.eta();
    float dR2 = dphi*dphi + deta*deta;
    // current gp is closer in phi then the previous
    if (dR2 < bestDR2) {
      gp = gem_gp;
      best_digi = d;
      bestDR2 = dR2;
    }
  }
  return emptyValue;
}
