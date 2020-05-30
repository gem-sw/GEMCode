#ifndef GEMCode_GEMValidation_GEMDigiStruct
#define GEMCode_GEMValidation_GEMDigiStruct

#include "TTree.h"
#include <string>

namespace gem {

  struct GEMDigiStruct {

    bool has_gem_dg_even;
    bool has_gem_dg2_even;

    bool has_gem_dg_odd;
    bool has_gem_dg2_odd;

    Int_t strip_gemdg_odd;
    Int_t strip_gemdg_even;

    int bx_dg_odd;
    int bx_dg_even;

    void init() {
      for (unsigned i = 0 ; i < nStations; i++) {
        has_gem_dg_even[i] = 0;
        has_gem_dg2_even[i] = 0;

        has_gem_dg_odd[i] = 0;
        has_gem_dg2_odd[i] = 0;

        strip_gemdg_odd[i] = -9;
        strip_gemdg_even[i] = -9;

        bx_dg_odd[i] = -9;
        bx_dg_even[i] = -9;
      }
    };

    void book(TTree* t) {
      t->Branch("has_gem_dg_odd", has_gem_dg_odd);
      t->Branch("has_gem_dg2_odd", has_gem_dg2_odd);

      t->Branch("has_gem_dg_even", has_gem_dg_even);
      t->Branch("has_gem_dg2_even", has_gem_dg2_even);

      t->Branch("strip_gemdg_odd", strip_gemdg_odd);
      t->Branch("strip_gemdg_even", strip_gemdg_even);

      t->Branch("bx_dg_odd", bx_dg_odd);
      t->Branch("bx_dg_even", bx_dg_even);
    }
  };
}  // namespace

#endif
