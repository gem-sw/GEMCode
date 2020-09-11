#ifndef GEMCode_GEMValidation_GEMDigiStruct
#define GEMCode_GEMValidation_GEMDigiStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace gem {

  struct GEMDigiStruct {

    static const int nStations = 3;

    bool has_gem_dg_even[nStations];
    bool has_gem_dg2_even[nStations];

    bool has_gem_dg_odd[nStations];
    bool has_gem_dg2_odd[nStations];

    Int_t strip_gem_dg_odd[nStations];
    Int_t strip_gem_dg_even[nStations];

    int bx_dg_odd[nStations];
    int bx_dg_even[nStations];

    // dphi with simhits
    p_ints gem_digi_bx;
    p_ints gem_digi_strip;
    p_ints gem_digi_isodd;
    p_ints gem_digi_region;
    p_ints gem_digi_station;
    p_ints gem_digi_chamber;
    p_ints gem_digi_roll;
    p_ints gem_digi_layer;
    p_ints gem_digi_tpid;

    void init() {

      gem_digi_bx = new t_ints;
      gem_digi_strip = new t_ints;
      gem_digi_isodd = new t_ints;
      gem_digi_region = new t_ints;
      gem_digi_station = new t_ints;
      gem_digi_chamber = new t_ints;
      gem_digi_roll = new t_ints;
      gem_digi_layer = new t_ints;
      gem_digi_tpid = new t_ints;

      for (unsigned i = 0 ; i < nStations; i++) {
        has_gem_dg_even[i] = 0;
        has_gem_dg2_even[i] = 0;

        has_gem_dg_odd[i] = 0;
        has_gem_dg2_odd[i] = 0;

        strip_gem_dg_odd[i] = -9;
        strip_gem_dg_even[i] = -9;

        bx_dg_odd[i] = -9;
        bx_dg_even[i] = -9;
      }
    };

    void book(TTree* t) {

      t->Branch("gem_digi_bx", &gem_digi_bx);
      t->Branch("gem_digi_strip", &gem_digi_strip);
      t->Branch("gem_digi_isodd", &gem_digi_isodd);
      t->Branch("gem_digi_region", &gem_digi_region);
      t->Branch("gem_digi_station", &gem_digi_station);
      t->Branch("gem_digi_chamber", &gem_digi_chamber);
      t->Branch("gem_digi_roll", &gem_digi_roll);
      t->Branch("gem_digi_layer", &gem_digi_layer);
      t->Branch("gem_digi_tpid", &gem_digi_tpid);


      t->Branch("has_gem_dg_odd", has_gem_dg_odd, "has_gem_dg_odd[3]/O");
      t->Branch("has_gem_dg2_odd", has_gem_dg2_odd, "has_gem_dg2_odd[3]/O");

      t->Branch("has_gem_dg_even", has_gem_dg_even, "has_gem_dg_even[3]/O");
      t->Branch("has_gem_dg2_even", has_gem_dg2_even, "has_gem_dg2_even[3]/O");

      t->Branch("strip_gem_dg_odd", strip_gem_dg_odd, "strip_gem_dg_odd[3]/I");
      t->Branch("strip_gem_dg_even", strip_gem_dg_even, "strip_gem_dg_even[3]/I");

      t->Branch("bx_dg_odd", bx_dg_odd, "bx_dg_odd[3]/I");
      t->Branch("bx_dg_even", bx_dg_even, "bx_dg_even[3]/I");
    }
  };
}  // namespace

#endif
