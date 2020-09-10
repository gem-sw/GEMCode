#include "GEMCode/GEMValidation/interface/Analyzers/SimTrackAnalyzer.h"

SimTrackAnalyzer::SimTrackAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC)
{
}

void SimTrackAnalyzer::init()
{
}

void SimTrackAnalyzer::analyze(TreeManager& tree, const SimTrack& t, const SimVertex& v)
{
  // simtrack properties
  tree.simTrack().pt = t.momentum().pt();
  tree.simTrack().px = t.momentum().px();
  tree.simTrack().py = t.momentum().py();
  tree.simTrack().pz = t.momentum().pz();
  tree.simTrack().phi = t.momentum().phi();
  tree.simTrack().eta = t.momentum().eta();
  tree.simTrack().charge = t.charge();
  tree.simTrack().endcap = (tree.simTrack().eta > 0.) ? 1 : -1;
  tree.simTrack().pdgid = t.type();

  tree.simTrack().vx = v.position().x();
  tree.simTrack().vy = v.position().y();
  tree.simTrack().vz = v.position().z();

  // simtrack properties
  auto& treeSim = tree.simTrack();
  treeSim.sim_pt->push_back(t.momentum().pt());
  treeSim.sim_px->push_back(t.momentum().px());
  treeSim.sim_py->push_back(t.momentum().py());
  treeSim.sim_pz->push_back(t.momentum().pz());
  treeSim.sim_phi->push_back(t.momentum().phi());
  treeSim.sim_eta->push_back(t.momentum().eta());
  treeSim.sim_charge->push_back(t.charge());
  treeSim.sim_pdgid->push_back(t.type());
  treeSim.sim_vx->push_back(v.position().x());
  treeSim.sim_vy->push_back(v.position().y());
  treeSim.sim_vz->push_back(v.position().z());
}
