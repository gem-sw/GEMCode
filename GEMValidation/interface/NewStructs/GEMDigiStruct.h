#ifndef GEMCode_GEMValidation_MY_GEMDigiStruct
#define GEMCode_GEMValidation_MY_GEMDigiStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace my {

  struct GEMDigiStruct {

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
    }
  };
}  // namespace

#endif
