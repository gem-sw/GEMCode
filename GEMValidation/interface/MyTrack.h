#ifndef GEMCode_GEMValidation_MyTrack
#define GEMCode_GEMValidation_MyTrack

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

static const int NumOfTrees = 13;

namespace gem {

  struct MyTrack :
    gem::SimTrackStruct,
    gem::SimHitStruct,
    gem::DigiStruct,
    gem::StubStruct,
    gem::L1MuStruct,
    gem::RecoTrackStruct {

    // initialize to default values
    void init() {
    };

    TTree* book(TTree* t) {

      return t;
    }
  };
}  // namespace

#endif
