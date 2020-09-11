#ifndef GEMCode_GEMValidation_MY_CSCStubStruct
#define GEMCode_GEMValidation_MY_CSCStubStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace my {

  struct CSCStubStruct {

    p_ints alct_bx;
    p_ints alct_wg;
    p_ints alct_isodd;
    p_ints alct_region;
    p_ints alct_station;
    p_ints alct_ring;
    p_ints alct_chamber;
    p_ints alct_quality;
    p_ints alct_tpid;

    p_ints clct_bx;
    p_ints clct_hs;
    p_ints clct_qs;
    p_ints clct_es;
    p_ints clct_isodd;
    p_ints clct_region;
    p_ints clct_station;
    p_ints clct_ring;
    p_ints clct_chamber;
    p_ints clct_quality;
    p_ints clct_pattern;
    p_ints clct_tpid;

    p_ints lct_bx;
    p_ints lct_wg;
    p_ints lct_hs;
    p_ints lct_qs;
    p_ints lct_es;
    p_ints lct_isodd;
    p_ints lct_region;
    p_ints lct_station;
    p_ints lct_ring;
    p_ints lct_chamber;
    p_ints lct_quality;
    p_ints lct_pattern;
    p_ints lct_tpid;

    p_ints mplct_bx;
    p_ints mplct_wg;
    p_ints mplct_hs;
    p_ints mplct_qs;
    p_ints mplct_es;
    p_ints mplct_isodd;
    p_ints mplct_region;
    p_ints mplct_station;
    p_ints mplct_ring;
    p_ints mplct_chamber;
    p_ints mplct_quality;
    p_ints mplct_pattern;
    p_ints mplct_tpid;

    void init() {
      alct_bx = new t_ints;
      alct_wg = new t_ints;
      alct_isodd = new t_ints;
      alct_region = new t_ints;
      alct_station = new t_ints;
      alct_ring = new t_ints;
      alct_chamber = new t_ints;
      alct_quality = new t_ints;
      alct_tpid = new t_ints;

      clct_bx = new t_ints;
      clct_hs = new t_ints;
      clct_qs = new t_ints;
      clct_es = new t_ints;
      clct_isodd = new t_ints;
      clct_region = new t_ints;
      clct_station = new t_ints;
      clct_ring = new t_ints;
      clct_chamber = new t_ints;
      clct_quality = new t_ints;
      clct_pattern = new t_ints;
      clct_tpid = new t_ints;

      lct_bx = new t_ints;
      lct_wg = new t_ints;
      lct_hs = new t_ints;
      lct_qs = new t_ints;
      lct_es = new t_ints;
      lct_isodd = new t_ints;
      lct_region = new t_ints;
      lct_station = new t_ints;
      lct_ring = new t_ints;
      lct_chamber = new t_ints;
      lct_quality = new t_ints;
      lct_pattern = new t_ints;
      lct_tpid = new t_ints;

      mplct_bx = new t_ints;
      mplct_wg = new t_ints;
      mplct_hs = new t_ints;
      mplct_qs = new t_ints;
      mplct_es = new t_ints;
      mplct_isodd = new t_ints;
      mplct_region = new t_ints;
      mplct_station = new t_ints;
      mplct_ring = new t_ints;
      mplct_chamber = new t_ints;
      mplct_quality = new t_ints;
      mplct_pattern = new t_ints;
      mplct_tpid = new t_ints;
    };

    void clear() {
      alct_bx->clear();
      alct_wg->clear();
      alct_isodd->clear();
      alct_region->clear();
      alct_station->clear();
      alct_ring->clear();
      alct_chamber->clear();
      alct_quality->clear();
      alct_tpid->clear();

      clct_bx->clear();
      clct_hs->clear();
      clct_qs->clear();
      clct_es->clear();
      clct_isodd->clear();
      clct_region->clear();
      clct_station->clear();
      clct_ring->clear();
      clct_chamber->clear();
      clct_quality->clear();
      clct_pattern->clear();
      clct_tpid->clear();

      lct_bx->clear();
      lct_wg->clear();
      lct_hs->clear();
      lct_qs->clear();
      lct_es->clear();
      lct_isodd->clear();
      lct_region->clear();
      lct_station->clear();
      lct_ring->clear();
      lct_chamber->clear();
      lct_quality->clear();
      lct_pattern->clear();
      lct_tpid->clear();

      mplct_bx->clear();
      mplct_wg->clear();
      mplct_hs->clear();
      mplct_qs->clear();
      mplct_es->clear();
      mplct_isodd->clear();
      mplct_region->clear();
      mplct_station->clear();
      mplct_ring->clear();
      mplct_chamber->clear();
      mplct_quality->clear();
      mplct_pattern->clear();
      mplct_tpid->clear();
    }


    void book(TTree* t) {

      t->Branch("alct_bx", &alct_bx);
      t->Branch("alct_wg", &alct_wg);
      t->Branch("alct_isodd", &alct_isodd);
      t->Branch("alct_region", &alct_region);
      t->Branch("alct_station", &alct_station);
      t->Branch("alct_ring", &alct_ring);
      t->Branch("alct_chamber", &alct_chamber);
      t->Branch("alct_quality", &alct_quality);
      t->Branch("alct_tpid", &alct_tpid);

      t->Branch("clct_bx", &clct_bx);
      t->Branch("clct_hs", &clct_hs);
      t->Branch("clct_qs", &clct_qs);
      t->Branch("clct_es", &clct_es);
      t->Branch("clct_isodd", &clct_isodd);
      t->Branch("clct_region", &clct_region);
      t->Branch("clct_station", &clct_station);
      t->Branch("clct_ring", &clct_ring);
      t->Branch("clct_chamber", &clct_chamber);
      t->Branch("clct_quality", &clct_quality);
      t->Branch("clct_pattern", &clct_pattern);
      t->Branch("clct_tpid", &clct_tpid);

      t->Branch("lct_bx", &lct_bx);
      t->Branch("lct_wg", &lct_wg);
      t->Branch("lct_hs", &lct_hs);
      t->Branch("lct_qs", &lct_qs);
      t->Branch("lct_es", &lct_es);
      t->Branch("lct_isodd", &lct_isodd);
      t->Branch("lct_region", &lct_region);
      t->Branch("lct_station", &lct_station);
      t->Branch("lct_ring", &lct_ring);
      t->Branch("lct_chamber", &lct_chamber);
      t->Branch("lct_quality", &lct_quality);
      t->Branch("lct_pattern", &lct_pattern);
      t->Branch("lct_tpid", &lct_tpid);

      t->Branch("mplct_bx", &mplct_bx);
      t->Branch("mplct_wg", &mplct_wg);
      t->Branch("mplct_hs", &mplct_hs);
      t->Branch("mplct_qs", &mplct_qs);
      t->Branch("mplct_es", &mplct_es);
      t->Branch("mplct_isodd", &mplct_isodd);
      t->Branch("mplct_region", &mplct_region);
      t->Branch("mplct_station", &mplct_station);
      t->Branch("mplct_ring", &mplct_ring);
      t->Branch("mplct_chamber", &mplct_chamber);
      t->Branch("mplct_quality", &mplct_quality);
      t->Branch("mplct_pattern", &mplct_pattern);
      t->Branch("mplct_tpid", &mplct_tpid);
    }
  };
}  // namespace

#endif
