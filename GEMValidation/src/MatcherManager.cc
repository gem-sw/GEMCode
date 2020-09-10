#include "GEMCode/GEMValidation/interface/MatcherManager.h"

MatcherManager::MatcherManager(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC) {
  genParticles_.reset(new GenParticleMatcher(conf, std::move(iC)));
  l1Muons_.reset(new L1MuMatcher(conf, std::move(iC)));
  l1Tracks_.reset(new L1TrackMatcher(conf, std::move(iC)));
  me0_rechits_.reset(new ME0RecHitMatcher(conf, std::move(iC)));
  // gem_rechits_.reset(new GEMRecHitMatcher(conf, std::move(iC)));

  const auto& simVertex = conf.getParameter<edm::ParameterSet>("simVertex");
  simVertexInput_ = iC.consumes<edm::SimVertexContainer>(simVertex.getParameter<edm::InputTag>("inputTag"));

  const auto& simTrack = conf.getParameter<edm::ParameterSet>("simTrack");
  simTrackInput_ = iC.consumes<edm::SimTrackContainer>(simTrack.getParameter<edm::InputTag>("inputTag"));
  simTrackMinPt_ = simTrack.getParameter<double>("minPt");
  simTrackMinEta_ = simTrack.getParameter<double>("minEta");
  simTrackMaxEta_ = simTrack.getParameter<double>("maxEta");
}

void MatcherManager::init(const edm::Event& e, const edm::EventSetup& eventSetup) {
  genParticles_->init(e, eventSetup);
  l1Muons_->init(e, eventSetup);
  l1Tracks_->init(e, eventSetup);
  me0_rechits_->init(e, eventSetup);
  // gem_rechits_->init(e, eventSetup);
}

void MatcherManager::match(const edm::Event& ev, const edm::EventSetup& eventSetup) {
  edm::Handle<edm::SimTrackContainer> sim_tracks;
  ev.getByToken(simTrackInput_, sim_tracks);
  const edm::SimTrackContainer& sim_track = *sim_tracks.product();

  edm::Handle<edm::SimVertexContainer> sim_vertices;
  ev.getByToken(simVertexInput_, sim_vertices);
  const edm::SimVertexContainer& sim_vert = *sim_vertices.product();

  if (verbose_) {
    std::cout << "Total number of SimTrack in this event: " << sim_track.size() << std::endl;
  }

  edm::SimTrackContainer sim_track_selected;
  for (const auto& t : sim_track) {
    if (!isSimTrackGood(t))
      continue;
    sim_track_selected.push_back(t);
  }

  int trk_no = 0;
  for (const auto& t : sim_track_selected) {
    if (verbose_) {
      std::cout << "Processing selected SimTrack " << trk_no + 1 << std::endl;
      std::cout << "pT = " << t.momentum().pt()
                << "GeV, eta = " << t.momentum().eta()
                << ", phi = " << t.momentum().phi()
                << ", Q = " << t.charge()
                << ", PDGiD =  " << t.type() << std::endl;
    }
    // now do the matching with all other objects
    match(t, sim_vert[t.vertIndex()]);

    trk_no++;
  }
}

/// do the matching
void MatcherManager::match(const SimTrack& t, const SimVertex& v) {
  genParticles_->match(t, v);
  l1Muons_->match(t, v);
  l1Tracks_->match(t, v);
  me0_rechits_->match(t, v);
  // gem_rechits_->match(t, v);
}

bool MatcherManager::isSimTrackGood(const SimTrack& t) {
  // SimTrack selection
  if (t.noVertex())
    return false;
  if (t.noGenpart())
    return false;
  // only muons
  if (std::abs(t.type()) != 13)
    return false;
  // pt selection
  if (t.momentum().pt() < simTrackMinPt_)
    return false;
  // eta selection
  const float eta(std::abs(t.momentum().eta()));
  if (eta > simTrackMaxEta_ || eta < simTrackMinEta_)
    return false;
  return true;
}
