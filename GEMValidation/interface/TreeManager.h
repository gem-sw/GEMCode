#ifndef GEMCode_GEMValidation_TreeManager_h
#define GEMCode_GEMValidation_TreeManager_h

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "GEMCode/GEMValidation/interface/Structs/SimTrackStruct.h"
#include "GEMCode/GEMValidation/interface/Structs/SimHitStruct.h"
#include "GEMCode/GEMValidation/interface/Structs/L1MuStruct.h"
#include "GEMCode/GEMValidation/interface/Structs/RecoTrackStruct.h"
#include "GEMCode/GEMValidation/interface/Structs/DigiStruct.h"
#include "GEMCode/GEMValidation/interface/Structs/StubStruct.h"

#include "TTree.h"
#include <vector>
#include <string>

class TreeManager
{
 public:
  TreeManager(const SimTrackMatchManager&);

  ~TreeManager() {}

  /// initialize
  void init() {
    gem::SimTrackStruct::init();
    gem::SimHitStruct::init();
    gem::DigiStruct::init();
    gem::StubStruct::init();
    gem::L1MuStruct::init();
    gem::RecoTrackStruct::init();
  }

  void book() {
    t = gem::SimTrackStruct::book(t);
    t = gem::SimHitStruct::book(t);
    t = gem::DigiStruct::book(t);
    t = gem::StubStruct::book(t);
    t = gem::L1MuStruct::book(t);
    t = gem::RecoTrackStruct::book(t);
  }

  // analyzers
  gem::SimTrackStruct sh_;
  gem::SimHitStruct gemsh_;
  gem::DigiStruct cscdg_;
  gem::StubStruct gemdg_;
  gem::L1MuStruct cscstub_;
  gem::RecoTrackStruct l1mu_;
};

#endif
