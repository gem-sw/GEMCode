#include "GEMCode/GEMValidation/interface/Analyzers/GEMDigiAnalyzer.h"

GEMDigiAnalyzer::GEMDigiAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC)
{
  minNHitsChamber_ = conf.getParameter<int>("minNHitsChamberGEMDigi");

  const auto& gemDigi = conf.getParameterSet("gemStripDigi");
  minBXDigi_ = gemDigi.getParameter<int>("minBX");
  maxBXDigi_ = gemDigi.getParameter<int>("maxBX");
  verboseDigi_ = gemDigi.getParameter<int>("verbose");

  gemDigiToken_ = iC.consumes<GEMDigiCollection>(gemDigi.getParameter<edm::InputTag>("inputTag"));
}

void GEMDigiAnalyzer::setMatcher(const GEMDigiMatcher& match_sh)
{
  match_.reset(new GEMDigiMatcher(match_sh));
}

void GEMDigiAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup, const MatcherSuperManager& manager, my::TreeManager& tree)
{
  iEvent.getByToken(gemDigiToken_, gemDigisH_);

  iSetup.get<MuonGeometryRecord>().get(gem_geom_);
  if (gem_geom_.isValid()) {
  gemGeometry_ = &*gem_geom_;
  } else {
    std::cout << "+++ Info: GEM geometry is unavailable. +++\n";
  }

  // get the digi collections
  const GEMDigiCollection& gemDigis = *gemDigisH_.product();

  auto& gemTree = tree.gemDigi();

  for (auto detUnitIt = gemDigis.begin(); detUnitIt != gemDigis.end(); ++detUnitIt) {
    const GEMDetId& id = (*detUnitIt).first;
    const bool isodd = (id.chamber()%2 == 1);

    // Loop over the digis of this DetUnit
    const auto& range = (*detUnitIt).second;
    for (auto digiIt = range.first; digiIt != range.second; ++digiIt) {

      if (!digiIt->isValid())
        continue;

      int tpidfound = -1;
      for (int tpid = 0; tpid < MAX_PARTICLES; tpid++) {
        const auto& gemMatches = manager.matcher(tpid)->gemDigis()->digisInDetId(id.rawId());
        for (const auto& gemMatch : gemMatches) {
          // check if the same
          if (*digiIt == gemMatch) {
            tpidfound =  tpid;
          }
        }
      }

      gemTree.gem_digi_bx->push_back(digiIt->bx());
      gemTree.gem_digi_strip->push_back(digiIt->strip());
      gemTree.gem_digi_isodd->push_back(isodd);
      gemTree.gem_digi_region->push_back(id.region());
      gemTree.gem_digi_station->push_back(id.station());
      gemTree.gem_digi_chamber->push_back(id.chamber());
      gemTree.gem_digi_layer->push_back(id.layer());
      gemTree.gem_digi_roll->push_back(id.roll());
      gemTree.gem_digi_tpid->push_back(tpidfound);
    }
  }
}

void GEMDigiAnalyzer::analyze(TreeManager& tree)
{
  for(const auto& d: match_->chamberIdsDigi()) {
    GEMDetId id(d);
    GEMDetId scid(id.superChamberId());

    const int st = id.station();
    const bool odd(id.chamber()%2==1);

    const int median_strip(median(match_->digisInChamber(d)));
    if (match_->digisInChamber(d).size() >= 1) {
      if (odd) {
        tree.gemDigi().has_gem_dg_odd[st] = true;
        tree.gemDigi().strip_gem_dg_odd[st] = median_strip;
      }
      else {
        tree.gemDigi().has_gem_dg_even[st] = true;
        tree.gemDigi().strip_gem_dg_even[st] = median_strip;
      }
    }

    if (match_->nLayersWithDigisInSuperChamber(scid.rawId()) == 2) {
      if (odd) tree.gemDigi().has_gem_dg2_odd[st] = true;
      else     tree.gemDigi().has_gem_dg2_even[st] = true;
    }
  }
}

int GEMDigiAnalyzer::median(const GEMDigiContainer& digis) const
{
  size_t sz = digis.size();
  vector<int> strips(sz);
  std::transform(digis.begin(), digis.end(),
                 strips.begin(), [](const GEMDigi& d) {return d.strip();} );
  std::sort(strips.begin(), strips.end());
  if ( sz % 2 == 0 ) {
    return (strips[sz/2 - 1] + strips[sz/2])/2;
  }
  else {
    return strips[sz/2];
  }
}

GlobalPoint
GEMDigiAnalyzer::meanPosition(const GEMDetId& id,
                              const GEMDigiContainer& digis) const
{
  GlobalPoint point_zero;
  if (digis.empty()) return point_zero; // point "zero"

  float sumx, sumy, sumz;
  sumx = sumy = sumz = 0.f;
  size_t n = 0;
  for (auto& d: digis){
    const GlobalPoint& gp = match_->getGlobalPointDigi(id, d);
    if (gp == point_zero) continue;

    sumx += gp.x();
    sumy += gp.y();
    sumz += gp.z();
    ++n;
  }
  if (n == 0) return GlobalPoint();
  return GlobalPoint(sumx/n, sumy/n, sumz/n);
}
