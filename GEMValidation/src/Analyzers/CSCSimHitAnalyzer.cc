#include "GEMCode/GEMValidation/interface/Analyzers/CSCSimHitAnalyzer.h"

using namespace std;

CSCSimHitAnalyzer::CSCSimHitAnalyzer(const CSCSimHitMatcher& match_sh)
{
  match_.reset(new CSCSimHitMatcher(match_sh));
}

void CSCSimHitAnalyzer::init(const edm::ParameterSet& conf)
{
  minNHitsChamber_ = conf.getParameter<int>("minNHitsChamberCSCSimHit");
}

void CSCSimHitAnalyzer::analyze(std::vector<gem::MyTrack>& track, std::vector<int> stations_to_use_)
{
  const auto& csc_simhits(match_->chamberIds(0));

  for(const auto& d: match_->chamberIds(0)) {

    CSCDetId id(d);

    const int st(gem::detIdToMEStation(id.station(),id.ring()));

    // ignore station if need be
    if (std::find(stations_to_use_.begin(), stations_to_use_.end(), st) == stations_to_use_.end()) continue;

    const int stt( std::find(stations_to_use_.begin(), stations_to_use_.end(), st) - stations_to_use_.begin());

    // calculate hit layers
    int nlayers(match_->nLayersWithHitsInChamber(d));

    // case ME11
    if (id.station()==1 and (id.ring()==4 or id.ring()==1)){
      // get the detId of the pairing subchamber
      int other_ring(id.ring()==4 ? 1 : 4);
      CSCDetId co_id(id.endcap(), id.station(), other_ring, id.chamber());
      // check if co_id occurs in the list
      // add the hit layers

      const auto& rawId(co_id.rawId());
      if (csc_simhits.find(rawId) != csc_simhits.end()) {
        nlayers = nlayers+match_->nLayersWithHitsInChamber(rawId);
      }
    }

    // layer requirement (typically 4)
    if (nlayers < minNHitsChamber_) continue;

    match_->LocalBendingInChamber(d);

    const bool odd(id.chamber()%2==1);
    const auto& simhits = match_->hitsInDetId(id);
    const GlobalPoint& keygp(match_->simHitsMeanPosition(simhits));

    if (odd) {
      track[stt].chamber_sh_odd = id.chamber();
      track[stt].nlayers_csc_sh_odd = nlayers;
      track[stt].has_csc_sh_odd = true;
      track[stt].eta_cscsh_odd = keygp.eta();
      track[stt].phi_cscsh_odd = keygp.phi();
      track[stt].perp_cscsh_odd = keygp.perp();
    }
    else {
      track[stt].chamber_sh_even = id.chamber();
      track[stt].nlayers_csc_sh_even = nlayers;
      track[stt].has_csc_sh_even = true;
      track[stt].eta_cscsh_even = keygp.eta();
      track[stt].phi_cscsh_even = keygp.phi();
      track[stt].perp_cscsh_even = keygp.perp();
    }

    // case ME11
    if (st==2 or st==3){
      if (odd) {
        track[1].chamber_sh_odd = id.chamber();
        track[1].nlayers_csc_sh_odd = nlayers;
        track[1].has_csc_sh_odd = true;
        track[1].eta_cscsh_odd = keygp.eta();
        track[1].phi_cscsh_odd = keygp.phi();
        track[1].perp_cscsh_odd = keygp.perp();
      }
      else {
        track[1].chamber_sh_even = id.chamber();
        track[1].nlayers_csc_sh_even = nlayers;
        track[1].has_csc_sh_even = true;
        track[1].eta_cscsh_even = keygp.eta();
        track[1].phi_cscsh_even = keygp.phi();
        track[1].perp_cscsh_even = keygp.perp();
      }
    }
  }
}