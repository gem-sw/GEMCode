#ifndef GEMCode_GEMValidation_MY_GEMStubStruct
#define GEMCode_GEMValidation_MY_GEMStubStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace my {

  struct GEMStubStruct {

    p_ints gem_pad_bx;
    p_ints gem_pad_pad;
    p_ints gem_pad_isodd;
    p_ints gem_pad_region;
    p_ints gem_pad_station;
    p_ints gem_pad_chamber;
    p_ints gem_pad_roll;
    p_ints gem_pad_layer;
    p_ints gem_pad_tpid;

    p_ints gem_copad_bx;
    p_ints gem_copad_pad;
    p_ints gem_copad_isodd;
    p_ints gem_copad_region;
    p_ints gem_copad_station;
    p_ints gem_copad_chamber;
    p_ints gem_copad_roll;
    p_ints gem_copad_tpid;

    p_ints gem_cluster_bx;
    p_ints gem_cluster_pad;
    p_ints gem_cluster_size;
    p_ints gem_cluster_isodd;
    p_ints gem_cluster_region;
    p_ints gem_cluster_station;
    p_ints gem_cluster_chamber;
    p_ints gem_cluster_roll;
    p_ints gem_cluster_layer;
    p_ints gem_cluster_tpid;

    void init() {

      gem_pad_bx = new t_ints;
      gem_pad_pad = new t_ints;
      gem_pad_isodd = new t_ints;
      gem_pad_region = new t_ints;
      gem_pad_station = new t_ints;
      gem_pad_chamber = new t_ints;
      gem_pad_roll = new t_ints;
      gem_pad_layer = new t_ints;
      gem_pad_tpid = new t_ints;

      gem_copad_bx = new t_ints;
      gem_copad_pad = new t_ints;
      gem_copad_isodd = new t_ints;
      gem_copad_region = new t_ints;
      gem_copad_station = new t_ints;
      gem_copad_chamber = new t_ints;
      gem_copad_roll = new t_ints;
      gem_copad_tpid = new t_ints;

      gem_cluster_bx = new t_ints;
      gem_cluster_pad = new t_ints;
      gem_cluster_size = new t_ints;
      gem_cluster_isodd = new t_ints;
      gem_cluster_region = new t_ints;
      gem_cluster_station = new t_ints;
      gem_cluster_chamber = new t_ints;
      gem_cluster_roll = new t_ints;
      gem_cluster_layer = new t_ints;
      gem_cluster_tpid = new t_ints;
    };

    void book(TTree* t) {

      t->Branch("gem_pad_bx", &gem_pad_bx);
      t->Branch("gem_pad_pad", &gem_pad_pad);
      t->Branch("gem_pad_isodd", &gem_pad_isodd);
      t->Branch("gem_pad_region", &gem_pad_region);
      t->Branch("gem_pad_station", &gem_pad_station);
      t->Branch("gem_pad_chamber", &gem_pad_chamber);
      t->Branch("gem_pad_roll", &gem_pad_roll);
      t->Branch("gem_pad_layer", &gem_pad_layer);
      t->Branch("gem_pad_tpid", &gem_pad_tpid);

      t->Branch("gem_copad_bx", &gem_copad_bx);
      t->Branch("gem_copad_pad", &gem_copad_pad);
      t->Branch("gem_copad_isodd", &gem_copad_isodd);
      t->Branch("gem_copad_region", &gem_copad_region);
      t->Branch("gem_copad_station", &gem_copad_station);
      t->Branch("gem_copad_chamber", &gem_copad_chamber);
      t->Branch("gem_copad_roll", &gem_copad_roll);
      t->Branch("gem_copad_tpid", &gem_copad_tpid);

      t->Branch("gem_cluster_bx", &gem_cluster_bx);
      t->Branch("gem_cluster_pad", &gem_cluster_pad);
      t->Branch("gem_cluster_size", &gem_cluster_size);
      t->Branch("gem_cluster_isodd", &gem_cluster_isodd);
      t->Branch("gem_cluster_region", &gem_cluster_region);
      t->Branch("gem_cluster_station", &gem_cluster_station);
      t->Branch("gem_cluster_chamber", &gem_cluster_chamber);
      t->Branch("gem_cluster_roll", &gem_cluster_roll);
      t->Branch("gem_cluster_layer", &gem_cluster_layer);
      t->Branch("gem_cluster_tpid", &gem_cluster_tpid);
    }
  };
}  // namespace

#endif
