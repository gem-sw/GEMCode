#include "GEMCode/GEMValidation/interface/Analyzers/GEMSimHitAnalyzer.h"

GEMSimHitAnalyzer::GEMSimHitAnalyzer(const edm::ParameterSet& conf)
{
  minNHitsChamber_ = conf.getParameter<int>("minNHitsChamberGEMSimHit");
}

void GEMSimHitAnalyzer::init(const GEMSimHitMatcher& match_sh)
{
  match_.reset(new GEMSimHitMatcher(match_sh));
}

void GEMSimHitAnalyzer::analyze(TreeManager& tree)
{
  for(const auto& d: match_->superChamberIds()) {
    GEMDetId id(d);
    const int st = id.station();

    const bool odd(id.chamber()%2==1);

    auto& match = match_;

    auto& gemSimHit = tree.gemSimHit();

    auto fill = [gemSimHit, d, match, odd] (int st) mutable {

      if (match->hitsInSuperChamber(d).size() > 0) {
        if (odd) {
          gemSimHit.has_gem_sh_odd[st] = true;
        }
        else {
          gemSimHit.has_gem_sh_even[st] = true;
        }
        const float mean_strip(match->simHitsMeanStrip(match->hitsInSuperChamber(d)));
        if (odd) gemSimHit.strip_gemsh_odd[st] = mean_strip;
        else     gemSimHit.strip_gemsh_even[st] = mean_strip;
      }
      if (match->nLayersWithHitsInSuperChamber(d) >= 2) {
        if (odd) gemSimHit.has_gem_sh2_odd[st] = true;
        else     gemSimHit.has_gem_sh2_even[st] = true;
      }
      const auto& copad_superids (match->superChamberIdsCoincidences());
      if (copad_superids.find(d) != copad_superids.end()) {
        if (odd) gemSimHit.has_gemcopad_sh_odd[st] = true;
        else     gemSimHit.has_gemcopad_sh_even[st] = true;
      }
    };

    fill(st);
    if (st==2 or st==3) {
      fill(1);
    }
  }
}
