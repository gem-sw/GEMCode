#include "GEMCode/GEMValidation/interface/MatcherSuperManager.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

MatcherSuperManager::MatcherSuperManager(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC)
{
  verbose_ = conf.getParameter<int>("verbose") + 1;

  const auto& simVertex = conf.getParameter<edm::ParameterSet>("simVertex");
  simVertexInput_ = iC.consumes<edm::SimVertexContainer>(simVertex.getParameter<edm::InputTag>("inputTag"));

  const auto& simTrack = conf.getParameter<edm::ParameterSet>("simTrack");
  simTrackInput_ = iC.consumes<edm::SimTrackContainer>(simTrack.getParameter<edm::InputTag>("inputTag"));
  simTrackMinPt_ = simTrack.getParameter<double>("minPt");
  simTrackMinEta_ = simTrack.getParameter<double>("minEta");
  simTrackMaxEta_ = simTrack.getParameter<double>("maxEta");

  matchers_.clear();

  for (unsigned i = 0; i<100; i++) {
    // make a new matcher (1 particle to many objects)
    std::shared_ptr<MatcherManager> newMatcher(new MatcherManager(conf, std::move(iC)));

    // add the matcher to the list
    matchers_.push_back(newMatcher);
  }
}

void MatcherSuperManager::match(const edm::Event& ev, const edm::EventSetup& eventSetup) {

  edm::Handle<edm::SimTrackContainer> sim_tracks;
  ev.getByToken(simTrackInput_, sim_tracks);
  const edm::SimTrackContainer& sim_track = *sim_tracks.product();

  edm::Handle<edm::SimVertexContainer> sim_vertices;
  ev.getByToken(simVertexInput_, sim_vertices);
  const edm::SimVertexContainer& sim_vert = *sim_vertices.product();

  if (verbose_) {
    std::cout << "Total number of SimTrack in this event: "
              << sim_track.size() << std::endl;
  }


  edm::SimTrackContainer sim_track_selected;
  for (const auto& t : sim_track) {
    if (!isSimTrackGood(t))
      continue;
    sim_track_selected.push_back(t);
  }

  int trk_no = 0;
  for (const auto& t : sim_track_selected) {

    // only process the first 100 muons
    if (trk_no >= 100) break;

    if (verbose_) {
      std::cout << "Processing selected SimTrack " << trk_no + 1 << std::endl;
      std::cout << "pT = " << t.momentum().pt()
                << "GeV, eta = " << t.momentum().eta()
                << ", phi = " << t.momentum().phi()
                << ", Q = " << t.charge()
                << ", PDGiD =  " << t.type() << std::endl;
    }

    // initialize the matchers!
    matchers_[trk_no]->init(ev, eventSetup);

    // now do the matching with all other objects
    matchers_[trk_no]->match(t, sim_vert[t.vertIndex()]);

    trk_no++;
  }
}

bool MatcherSuperManager::isSimTrackGood(const SimTrack& t) {
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
