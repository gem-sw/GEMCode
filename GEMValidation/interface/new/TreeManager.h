#ifndef GEMCode_GEMValidation_MY_TreeManager_h
#define GEMCode_GEMValidation_MY_TreeManager_h

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "GEMCode/GEMValidation/interface/NewStructs/GenParticleStruct.h"
#include "GEMCode/GEMValidation/interface/NewStructs/SimTrackStruct.h"
#include "GEMCode/GEMValidation/interface/NewStructs/GEMSimHitStruct.h"
#include "GEMCode/GEMValidation/interface/NewStructs/GEMDigiStruct.h"
#include "GEMCode/GEMValidation/interface/NewStructs/GEMStubStruct.h"
#include "GEMCode/GEMValidation/interface/NewStructs/CSCSimHitStruct.h"
#include "GEMCode/GEMValidation/interface/NewStructs/CSCDigiStruct.h"
#include "GEMCode/GEMValidation/interface/NewStructs/CSCStubStruct.h"
#include "GEMCode/GEMValidation/interface/NewStructs/RPCSimHitStruct.h"
#include "GEMCode/GEMValidation/interface/NewStructs/RPCDigiStruct.h"
#include "GEMCode/GEMValidation/interface/NewStructs/RPCRecHitStruct.h"
#include "GEMCode/GEMValidation/interface/NewStructs/L1MuStruct.h"
#include "GEMCode/GEMValidation/interface/NewStructs/L1TrackStruct.h"
#include "GEMCode/GEMValidation/interface/NewStructs/RecoTrackStruct.h"

#include "TTree.h"
#include <vector>
#include <string>

namespace my {

class TreeManager
{
 public:
  TreeManager() { book(); }

  ~TreeManager() {}

  void book();

  void init();

  void fill();

  my::GenParticleStruct& genParticle() { return genParticleSt_; }
  my::SimTrackStruct& simTrack() { return simTrackSt_; }
  my::GEMSimHitStruct& gemSimHit() { return gemSimHitSt_; }
  my::GEMDigiStruct& gemDigi() { return gemDigiSt_; }
  my::GEMStubStruct& gemStub() { return gemStubSt_; }
  my::CSCSimHitStruct& cscSimHit() { return cscSimHitSt_; }
  my::CSCDigiStruct& cscDigi() { return cscDigiSt_; }
  my::CSCStubStruct& cscStub() { return cscStubSt_; }
  my::RPCSimHitStruct& rpcSimHit() { return rpcSimHitSt_; }
  my::RPCDigiStruct& rpcDigi() { return rpcDigiSt_; }
  my::RPCRecHitStruct& rpcRecHit() { return rpcRecHitSt_; }
  my::L1MuStruct& l1mu() { return l1MuSt_; }
  my::L1TrackStruct& l1track() { return l1TrackSt_; }
  my::RecoTrackStruct& recoTrack() { return recoTrackSt_; }

 private:

  my::GenParticleStruct genParticleSt_;
  my::SimTrackStruct simTrackSt_;
  my::GEMSimHitStruct gemSimHitSt_;
  my::GEMDigiStruct gemDigiSt_;
  my::GEMStubStruct gemStubSt_;
  my::CSCSimHitStruct cscSimHitSt_;
  my::CSCDigiStruct cscDigiSt_;
  my::CSCStubStruct cscStubSt_;
  my::RPCSimHitStruct rpcSimHitSt_;
  my::RPCDigiStruct rpcDigiSt_;
  my::RPCRecHitStruct rpcRecHitSt_;
  my::L1MuStruct l1MuSt_;
  my::L1TrackStruct l1TrackSt_;
  my::RecoTrackStruct recoTrackSt_;

  // new stuff
  TTree* flatTree_;
};

};

#endif
