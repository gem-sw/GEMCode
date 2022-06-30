#include "GEMCode/GEMValidation/interface/Analyzers/L1MuAnalyzer.h"

L1MuAnalyzer::L1MuAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC)
{
  const auto& emtfTrack = conf.getParameter<edm::ParameterSet>("emtfTrack");
  minBXEMTFTrack_ = emtfTrack.getParameter<int>("minBX");
  maxBXEMTFTrack_ = emtfTrack.getParameter<int>("maxBX");
  verboseEMTFTrack_ = emtfTrack.getParameter<int>("verbose");
  runEMTFTrack_ = emtfTrack.getParameter<bool>("run");

  const auto& emtfCand = conf.getParameter<edm::ParameterSet>("emtfCand");
  minBXEMTFCand_ = emtfCand.getParameter<int>("minBX");
  maxBXEMTFCand_ = emtfCand.getParameter<int>("maxBX");
  verboseEMTFCand_ = emtfCand.getParameter<int>("verbose");
  runEMTFCand_ = emtfCand.getParameter<bool>("run");

  const auto& omtfCand = conf.getParameter<edm::ParameterSet>("omtfCand");
  minBXOMTFCand_ = omtfCand.getParameter<int>("minBX");
  maxBXOMTFCand_ = omtfCand.getParameter<int>("maxBX");
  verboseOMTFCand_ = omtfCand.getParameter<int>("verbose");
  runOMTFCand_ = omtfCand.getParameter<bool>("run");

  const auto& bmtfCand = conf.getParameter<edm::ParameterSet>("bmtfCand");
  minBXBMTFCand_ = bmtfCand.getParameter<int>("minBX");
  maxBXBMTFCand_ = bmtfCand.getParameter<int>("maxBX");
  verboseBMTFCand_ = bmtfCand.getParameter<int>("verbose");
  runBMTFCand_ = bmtfCand.getParameter<bool>("run");

  const auto& muon = conf.getParameter<edm::ParameterSet>("muon");
  minBXGMT_ = muon.getParameter<int>("minBX");
  maxBXGMT_ = muon.getParameter<int>("maxBX");
  verboseGMT_ = muon.getParameter<int>("verbose");
  runGMT_ = muon.getParameter<bool>("run");

  const auto& emtfShower = conf.getParameter<edm::ParameterSet>("emtfShower");
  minBXEMTFShower_ = emtfShower.getParameter<int>("minBX");
  maxBXEMTFShower_ = emtfShower.getParameter<int>("maxBX");
  verboseEMTFShower_ = emtfShower.getParameter<int>("verbose");
  runEMTFShower_ = emtfShower.getParameter<bool>("run");

  const auto& muonShower = conf.getParameter<edm::ParameterSet>("muonShower");
  minBXGMT_ = muonShower.getParameter<int>("minBX");
  maxBXGMT_ = muonShower.getParameter<int>("maxBX");
  verboseShower_ = muonShower.getParameter<int>("verbose");
  runShower_ = muonShower.getParameter<bool>("run");

  if (runEMTFTrack_)
    emtfTrackToken_ = iC.consumes<l1t::EMTFTrackCollection>(emtfTrack.getParameter<edm::InputTag>("inputTag"));

  if (runEMTFCand_)
    emtfCandToken_ = iC.consumes<l1t::RegionalMuonCandBxCollection>(emtfCand.getParameter<edm::InputTag>("inputTag"));

  if (runGMT_)
    muonToken_ = iC.consumes<l1t::MuonBxCollection>(muon.getParameter<edm::InputTag>("inputTag"));

  if (runEMTFShower_)
    emtfShowerToken_ = iC.consumes<l1t::RegionalMuonShowerBxCollection>(emtfShower.getParameter<edm::InputTag>("inputTag"));

  if (runShower_)
    showerToken_ = iC.consumes<l1t::MuonShowerBxCollection>(muonShower.getParameter<edm::InputTag>("inputTag"));
}

void L1MuAnalyzer::setMatcher(const L1MuMatcher& match_sh)
{
  match_.reset(new L1MuMatcher(match_sh));
}

void L1MuAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup,
                           const MatcherSuperManager& manager, my::TreeManager& tree) {

  auto& trkTree = tree.l1mu();
  auto& simTree = tree.simTrack();
  const bool validTracks(simTree.sim_pt->size()>0);

  if (runEMTFTrack_) {
    iEvent.getByToken(emtfTrackToken_, emtfTrackHandle_);
    const l1t::EMTFTrackCollection& emtfTracks = *emtfTrackHandle_.product();
    if (verboseEMTFTrack_)
      std::cout << "Analyzing " << emtfTracks.size() << " EMTF tracks" << std::endl;

    int index = 0;
    for (const auto& trk : emtfTracks) {

      int bx = trk.BX();
      if ( bx < minBXEMTFTrack_ or bx > maxBXEMTFTrack_) continue;

      const gem::EMTFTrack& gemtrk(trk);

      if (verboseEMTFTrack_)
        std::cout << gemtrk << std::endl;

      int tpidfound = -1;
      // check if it was matched to a simtrack
      for (int tpid = 0; tpid < MAX_PARTICLES; tpid++) {

        // get the matcher
        const auto& matcher = manager.matcher(tpid);

        index++;

        const auto& trackMatch = matcher->l1Muons()->emtfTrack();
        if (trackMatch) {

          if (verboseEMTFTrack_)
            std::cout << "Candidate match " << *trackMatch
                      << std::endl;

          //check if the same
          if (gemtrk == *trackMatch) {
            tpidfound = tpid;
            if (verboseEMTFTrack_)
              std::cout << "...matched! With index " << tpidfound << std::endl;
            break;
          }
        }
      }
      trkTree.emtftrack_pt->push_back(gemtrk.pt());
      trkTree.emtftrack_eta->push_back(gemtrk.eta());
      trkTree.emtftrack_phi->push_back(gemtrk.phi());
      trkTree.emtftrack_charge->push_back(gemtrk.charge());
      trkTree.emtftrack_bx->push_back(gemtrk.bx());
      trkTree.emtftrack_tpid->push_back(tpidfound);

      if (tpidfound != -1 and validTracks) {
        ((*simTree.sim_id_emtf_track)[tpidfound]).push_back(index);
      }
    }

  }

  if (runEMTFCand_) {
    iEvent.getByToken(emtfCandToken_, emtfCandHandle_);
    const l1t::RegionalMuonCandBxCollection& emtfCands = *emtfCandHandle_.product();

    if (verboseEMTFCand_)
      std::cout << "Analyzing " << int(emtfCands.end(0) - emtfCands.begin(0)) << " EMTF cands" << std::endl;

    int index = 0;
    for (int bx = emtfCands.getFirstBX(); bx <= emtfCands.getLastBX(); bx++ ){
      if ( bx < minBXEMTFCand_ or bx > maxBXEMTFCand_) continue;
      for (auto emtfCand = emtfCands.begin(bx); emtfCand != emtfCands.end(bx); ++emtfCand ){

        const gem::EMTFCand& gemtrk(*emtfCand);

        if (verboseEMTFCand_)
          std::cout << gemtrk << std::endl;

        int tpidfound = -1;
        // check if it was matched to a simtrack
        for (int tpid = 0; tpid < MAX_PARTICLES; tpid++) {

          // get the matcher
          const auto& matcher = manager.matcher(tpid);

          const auto& trackMatch = matcher->l1Muons()->emtfCand();
          if (trackMatch) {

            if (verboseEMTFCand_)
              std::cout << "Candidate match " << *trackMatch
                        << std::endl;

            //check if the same
            if (gemtrk == *trackMatch) {
              tpidfound = tpid;
              if (verboseEMTFCand_)
                std::cout << "...matched! With index " << tpidfound << std::endl;
              break;
            }
          }
        }
        trkTree.emtfcand_pt->push_back(gemtrk.pt());
        trkTree.emtfcand_eta->push_back(gemtrk.eta());
        trkTree.emtfcand_phi->push_back(gemtrk.phi());
        trkTree.emtfcand_charge->push_back(gemtrk.charge());
        trkTree.emtfcand_bx->push_back(gemtrk.bx());
        trkTree.emtfcand_tpid->push_back(tpidfound);

        if (tpidfound != -1 and validTracks) {
          ((*simTree.sim_id_emtf_cand)[tpidfound]).push_back(index);
        }
      }
    }
  }

  if (runGMT_) {
    iEvent.getByToken(muonToken_, muonHandle_);
    const l1t::MuonBxCollection& gmtCands = *muonHandle_.product();

    if (verboseGMT_)
      std::cout << "Analyzing " << int(gmtCands.end(0) - gmtCands.begin(0)) << " GMT cands" << std::endl;

    int index = 0;
    for (int bx = gmtCands.getFirstBX(); bx <= gmtCands.getLastBX(); bx++ ){
      if ( bx < minBXGMT_ or bx > maxBXGMT_) continue;
      for (auto emtfCand = gmtCands.begin(bx); emtfCand != gmtCands.end(bx); ++emtfCand ){

        const gem::EMTFCand& gemtrk(*emtfCand);

        if (verboseGMT_)
          std::cout << gemtrk << std::endl;

        int tpidfound = -1;
        // check if it was matched to a simtrack
        for (int tpid = 0; tpid < MAX_PARTICLES; tpid++) {

          // get the matcher
          const auto& matcher = manager.matcher(tpid);

          const auto& trackMatch = matcher->l1Muons()->muon();
          if (trackMatch) {

            if (verboseGMT_)
              std::cout << "Candidate match " << *trackMatch
                        << std::endl;

            //check if the same
            if (gemtrk == *trackMatch) {
              tpidfound = tpid;
              if (verboseGMT_)
                std::cout << "...matched! With index " << tpidfound << std::endl;
              break;
            }
          }
        }
        trkTree.l1mu_pt->push_back(gemtrk.pt());
        trkTree.l1mu_eta->push_back(gemtrk.eta());
        trkTree.l1mu_phi->push_back(gemtrk.phi());
        trkTree.l1mu_charge->push_back(gemtrk.charge());
        trkTree.l1mu_bx->push_back(gemtrk.bx());
        trkTree.l1mu_tpid->push_back(tpidfound);

        if (tpidfound != -1 and validTracks) {
          ((*simTree.sim_id_l1mu)[tpidfound]).push_back(index);
        }
      }
    }
  }

  if (runEMTFShower_) {
    iEvent.getByToken(emtfShowerToken_, emtfShowerHandle_);
    const l1t::RegionalMuonShowerBxCollection& emtfShowers = *emtfShowerHandle_.product();

    if (verboseEMTFShower_)
      std::cout << "Analyzing " << int(emtfShowers.end(0) - emtfShowers.begin(0)) << " EMTF showers" << std::endl;

    for (int bx = emtfShowers.getFirstBX(); bx <= emtfShowers.getLastBX(); bx++ ){
      if ( bx < minBXEMTFShower_ or bx > maxBXEMTFShower_) continue;
      for (auto emtfShower = emtfShowers.begin(bx); emtfShower != emtfShowers.end(bx); ++emtfShower ){

        trkTree.emtfshower_bx->push_back(0);
        //trkTree.emtfshower_region->push_back(emtfShower->endcap());
        //trkTree.emtfshower_sector->push_back(emtfShower->sector());
        trkTree.emtfshower_isOneNominalInTime->push_back(emtfShower->isOneNominalInTime());
        trkTree.emtfshower_isTwoLooseInTime->push_back(emtfShower->isTwoLooseInTime());
        trkTree.emtfshower_isOneNominalOutOfTime->push_back(emtfShower->isOneNominalOutOfTime());
        trkTree.emtfshower_isTwoLooseOutOfTime->push_back(emtfShower->isTwoLooseOutOfTime());
        if (verboseEMTFShower_)
          std::cout << "\tShower data: "
                    << " TwoLooseOOT: " << emtfShower->isTwoLooseOutOfTime()
                    << " TwoLooseIT: " << emtfShower->isTwoLooseInTime()
                    << " OneNominalOOT: " << emtfShower->isOneNominalOutOfTime()
                    << " OneNominalIT: " << emtfShower->isOneNominalInTime()
                    << std::endl;
      }
    }

  }

  if (runShower_) {
    iEvent.getByToken(showerToken_, showerHandle_);
    const l1t::MuonShowerBxCollection& gmtShowers = *showerHandle_.product();

    if (verboseShower_)
      std::cout << "Analyzing " << int(gmtShowers.end(0) - gmtShowers.begin(0)) << " GMT shower" << std::endl;

    for (int bx = gmtShowers.getFirstBX(); bx <= gmtShowers.getLastBX(); bx++ ){
      if ( bx < minBXGMT_ or bx > maxBXGMT_) continue;
      for (auto gmtShower = gmtShowers.begin(bx); gmtShower != gmtShowers.end(bx); ++gmtShower ){

        trkTree.l1mushower_bx->push_back(0);
        trkTree.l1mushower_isOneNominalInTime->push_back(gmtShower->isOneNominalInTime());
        trkTree.l1mushower_isTwoLooseInTime->push_back(gmtShower->isTwoLooseInTime());
        trkTree.l1mushower_isOneNominalOutOfTime->push_back(gmtShower->isOneNominalOutOfTime());
        trkTree.l1mushower_isTwoLooseOutOfTime->push_back(gmtShower->isTwoLooseOutOfTime());
        if (verboseShower_)
          std::cout << "\tShower data: "
                    << " TwoLooseOOT: " << gmtShower->isTwoLooseOutOfTime()
                    << " TwoLooseIT: " << gmtShower->isTwoLooseInTime()
                    << " OneNominalOOT: " << gmtShower->isOneNominalOutOfTime()
                    << " OneNominalIT: " << gmtShower->isOneNominalInTime()
                    << std::endl;
      }
    }
  }
}

  void L1MuAnalyzer::analyze(TreeManager& tree)
  {
  const auto& emtfTrack = match_->emtfTrack();
  const auto& muon = match_->muon();

  if (emtfTrack != nullptr) {
    unsigned int nMatchingStubs = 0;
    bool stubMatched[4] = {false, false, false, false};
    const auto& cscStubMatcher_ = match_->cscStubMatcher();
    for (const auto& stub : *emtfTrack->emtfHits()){
      if (not stub.Is_CSC()) continue;
      const CSCCorrelatedLCTDigi& csc_stub = stub.CreateCSCCorrelatedLCTDigi();
      const CSCDetId& csc_id1 = stub.CSC_DetId();
      const CSCDetId& csc_id = CSCDetId(csc_id1.endcap(), csc_id1.station(), csc_id1.ring()==4 ? 1 : csc_id1.ring(), 
       csc_id1.chamber(), 0);
      int stub_halfstrip = csc_id1.ring() == 4 ? csc_stub.getStrip()+128 : csc_stub.getStrip();
      //if (csc_id1.ring() == 4) std::cout <<"EMTFhit in ring4 " << csc_id1 <<" "<< csc_stub << std::endl;
      for (const auto& sim_stub: cscStubMatcher_->lctsInChamber(csc_id.rawId())){
        bool matched = sim_stub.isValid() == csc_stub.isValid() && sim_stub.getQuality() == csc_stub.getQuality() 
        && sim_stub.getPattern() == csc_stub.getPattern() && sim_stub.getStrip() == stub_halfstrip 
        && sim_stub.getKeyWG() == csc_stub.getKeyWG() && sim_stub.getBend() == csc_stub.getBend() 
        && sim_stub.getBX() == csc_stub.getBX();
        if (matched) {
          if (not stubMatched[csc_id.station() - 1])
              nMatchingStubs++;
          stubMatched[csc_id.station() - 1] = true;
        }
        //else {
        //  std::cout <<"NOT matched in CSCid "<< csc_id <<" emtfhit "<< csc_stub <<" simstub "<< sim_stub << std::endl;
        //}
      }
      const auto& lct = cscStubMatcher_->bestLctInChamber(csc_id);
      switch (csc_id.station()){
        case 1:
          tree.l1mu().emtfhit_st1_ring = csc_id.ring();
          tree.l1mu().emtfhit_st1_pattern = csc_stub.getPattern();
          tree.l1mu().emtfhit_st1_wire = csc_stub.getKeyWG();
          tree.l1mu().emtfhit_st1_halfstrip = stub_halfstrip;
        if (lct.isValid()){
          tree.l1mu().cscstub_st1_found = true;
          tree.l1mu().cscstub_st1_ring = csc_id.ring();
          tree.l1mu().cscstub_st1_pattern = lct.getPattern();
          tree.l1mu().cscstub_st1_wire = lct.getKeyWG();
          tree.l1mu().cscstub_st1_halfstrip = lct.getStrip();
        }
        break;
        case 2:
          tree.l1mu().emtfhit_st2_ring = csc_id.ring();
          tree.l1mu().emtfhit_st2_pattern = csc_stub.getPattern();
          tree.l1mu().emtfhit_st2_wire =  csc_stub.getKeyWG();
          tree.l1mu().emtfhit_st2_halfstrip =  csc_stub.getStrip();
        if (lct.isValid()){
          tree.l1mu().cscstub_st2_found = true;
          tree.l1mu().cscstub_st2_ring = csc_id.ring();
          tree.l1mu().cscstub_st2_pattern = lct.getPattern();
          tree.l1mu().cscstub_st2_wire = lct.getKeyWG();
          tree.l1mu().cscstub_st2_halfstrip = lct.getStrip();
        }
        break;
        case 3:
          tree.l1mu().emtfhit_st3_ring = csc_id.ring();
          tree.l1mu().emtfhit_st3_pattern =  csc_stub.getPattern();
          tree.l1mu().emtfhit_st3_wire =  csc_stub.getKeyWG();
          tree.l1mu().emtfhit_st3_halfstrip =  csc_stub.getStrip();
        if (lct.isValid()){
          tree.l1mu().cscstub_st3_found = true;
          tree.l1mu().cscstub_st3_ring = csc_id.ring();
          tree.l1mu().cscstub_st3_pattern = lct.getPattern();
          tree.l1mu().cscstub_st3_wire = lct.getKeyWG();
          tree.l1mu().cscstub_st3_halfstrip = lct.getStrip();
        }
        break;
        case 4:
          tree.l1mu().emtfhit_st4_ring = csc_id.ring();
          tree.l1mu().emtfhit_st4_pattern =  csc_stub.getPattern();
          tree.l1mu().emtfhit_st4_wire =  csc_stub.getKeyWG();
          tree.l1mu().emtfhit_st4_halfstrip =  csc_stub.getStrip();
        if (lct.isValid()){
          tree.l1mu().cscstub_st4_found = true;
          tree.l1mu().cscstub_st4_ring = csc_id.ring();
          tree.l1mu().cscstub_st4_pattern = lct.getPattern();
          tree.l1mu().cscstub_st4_wire = lct.getKeyWG();
          tree.l1mu().cscstub_st4_halfstrip = lct.getStrip();
        }
        break;
        default: std::cout<<"Error!! station from CSC id is > 4 "<<csc_id << std::endl; 
      }
    }
    tree.l1mu().cscstub_st1_matched = stubMatched[0];
    tree.l1mu().cscstub_st2_matched = stubMatched[1];
    tree.l1mu().cscstub_st3_matched = stubMatched[2];
    tree.l1mu().cscstub_st4_matched = stubMatched[3];
    tree.l1mu().nstubs_matched_TF   = nMatchingStubs;
    tree.l1mu().allstubs_matched_TF = nMatchingStubs == emtfTrack->nStubs();
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
    tree.l1mu().quality = emtfTrack->quality();
    tree.l1mu().deltaphi12 = emtfTrack->deltaphi(0); 
    tree.l1mu().deltaphi13 = emtfTrack->deltaphi(1); 
    tree.l1mu().deltaphi14 = emtfTrack->deltaphi(2); 
    tree.l1mu().deltaphi23 = emtfTrack->deltaphi(3); 
    tree.l1mu().deltaphi24 = emtfTrack->deltaphi(4); 
    tree.l1mu().deltaphi34 = emtfTrack->deltaphi(5); 
    tree.l1mu().deltatheta12 = emtfTrack->deltatheta(0); 
    tree.l1mu().deltatheta13 = emtfTrack->deltatheta(1); 
    tree.l1mu().deltatheta14 = emtfTrack->deltatheta(2); 
    tree.l1mu().deltatheta23 = emtfTrack->deltatheta(3); 
    tree.l1mu().deltatheta24 = emtfTrack->deltatheta(4); 
    tree.l1mu().deltatheta34 = emtfTrack->deltatheta(5); 
    tree.l1mu().lctslope1 = emtfTrack->lctslope(0); 
    tree.l1mu().lctslope2 = emtfTrack->lctslope(1); 
    tree.l1mu().lctslope3 = emtfTrack->lctslope(2); 
    tree.l1mu().lctslope4 = emtfTrack->lctslope(3); 
    tree.l1mu().lctpattern1 = emtfTrack->lctpattern(0); 
    tree.l1mu().lctpattern2 = emtfTrack->lctpattern(1); 
    tree.l1mu().lctpattern3 = emtfTrack->lctpattern(2); 
    tree.l1mu().lctpattern4 = emtfTrack->lctpattern(3); 
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
