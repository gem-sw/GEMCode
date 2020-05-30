#ifndef GEMCode_GEMValidation_TreeManager_h
#define GEMCode_GEMValidation_TreeManager_h

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "GEMCode/GEMValidation/interface/Structs/SimTrackStruct.h"
#include "GEMCode/GEMValidation/interface/Structs/CSCSimHitStruct.h"
#include "GEMCode/GEMValidation/interface/Structs/GEMSimHitStruct.h"
#include "GEMCode/GEMValidation/interface/Structs/L1MuStruct.h"
#include "GEMCode/GEMValidation/interface/Structs/RecoTrackStruct.h"
#include "GEMCode/GEMValidation/interface/Structs/CSCDigiStruct.h"
#include "GEMCode/GEMValidation/interface/Structs/GEMDigiStruct.h"
#include "GEMCode/GEMValidation/interface/Structs/CSCStubStruct.h"

#include "TTree.h"
#include <vector>
#include <string>

class TreeManager
{
 public:
  TreeManager(const SimTrackMatchManager&);

  ~TreeManager() {}

  void book() {
    edm::Service<TFileService> fs;
    simTrackTree_ = fs->make<TTree>("SimTrack","SimTrack");
    gemSimHitTree_ = fs->make<TTree>("GEMSimHit","GEMSimHit");
    cscSimHitTree_ = fs->make<TTree>("GEMSimHit","GEMSimHit");
    gemDigiTree_ = fs->make<TTree>("GEMDigi","GEMDigi");
    cscDigiTree_ = fs->make<TTree>("CSCDigi","CSCDigi");
    cscStubTree_ = fs->make<TTree>("CSCStub","CSCStub");
    l1MuTree_ = fs->make<TTree>("L1Mu","L1Mu");
    recoTrackTree_ = fs->make<TTree>("RecoTrack","RecoTrack");

    simTrackSt_.book(simTrackTree_);
    gemSimHitSt_.book(gemSimHitTree_);
    cscSimHitSt_.book(cscSimHitTree_);
    gemDigiSt_.book(gemDigiTree_);
    cscDigiSt_.book(cscDigiTree_);
    cscStubSt_.book(cscStubTree_);
    l1MuSt_.book(l1MuTree_);
    recoTrackSt_.book(recoTrackTree_);
  }

  /// initialize
  void init() {
    simTrackSt_.init();
    gemSimHitSt_.init();
    cscSimHitSt_.init();
    gemDigiSt_.init();
    cscDigiSt_.init();
    cscStubSt_.init();
    l1MuSt_.init(l);
    recoTrackSt_.init();
  }

  void fill() {
    simTrackTree_->Fill();
    gemSimHitTree_->Fill();
    cscSimHitTree_->Fill();
    gemDigiTree_->Fill();
    cscDigiTree_->Fill();
    cscStubTree_->Fill();
    l1MuTree_->Fill();
    recoTrackTree_->Fill();
  }

  TTree* simTrackTree_;
  TTree* gemSimHitTree_;
  TTree* cscSimHitTree_;
  TTree* gemDigiTree_;
  TTree* cscDigiTree_;
  TTree* cscStubTree_;
  TTree* l1MuTree_;
  TTree* recoTrackTree_;

  gem::SimTrackStruct simTrackSt_;
  gem::GEMSimHitStruct gemSimHitSt_;
  gem::CSCSimHitStruct cscSimHitSt_;
  gem::GEMDigiStruct gemDigiSt_;
  gem::CSCDigiStruct cscDigiSt_;
  gem::CSCStubStruct cscStubSt_;
  gem::L1MuStruct l1MuSt_;
  gem::RecoTrackStruct recoTrackSt_;
};

#endif
