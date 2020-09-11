#ifndef GEMCode_GEMValidation_MY_GenParticleStruct
#define GEMCode_GEMValidation_MY_GenParticleStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace my {

  struct GenParticleStruct {

    p_floats gen_pt;
    p_floats gen_pz;
    p_floats gen_eta;
    p_floats gen_phi;
    p_ints   gen_charge;
    p_floats gen_dxy;
    p_floats gen_d0;
    p_floats gen_z0;
    p_floats gen_d0_prod;
    p_floats gen_z0_prod;
    p_ints   gen_pdgid;
    p_ints   gen_tpid;

    void init() {
      gen_pt      = new t_floats;
      gen_eta     = new t_floats;
      gen_phi     = new t_floats;
      gen_dxy     = new t_floats;
      gen_d0      = new t_floats;
      gen_z0      = new t_floats;
      gen_d0_prod = new t_floats;
      gen_z0_prod = new t_floats;
      gen_pdgid   = new t_ints;
      gen_charge  = new t_ints;
      gen_tpid   = new t_ints;
    };

    void clear() {
      gen_pt->clear();
      gen_pz->clear();
      gen_eta->clear();
      gen_phi->clear();
      gen_dxy->clear();
      gen_d0->clear();
      gen_z0->clear();
      gen_d0_prod->clear();
      gen_z0_prod->clear();
      gen_pdgid->clear();
      gen_charge->clear();
    }

    void book(TTree* t) {
      t->Branch("gen_pt",     &gen_pt);
      t->Branch("gen_pz",     &gen_pz);
      t->Branch("gen_eta",    &gen_eta);
      t->Branch("gen_phi",    &gen_phi);
      t->Branch("gen_dxy",    &gen_dxy);
      t->Branch("gen_d0",     &gen_d0);
      t->Branch("gen_z0",     &gen_z0);
      t->Branch("gen_d0_prod",     &gen_d0_prod);
      t->Branch("gen_z0_prod",     &gen_z0_prod);
      t->Branch("gen_pdgid",       &gen_pdgid);
      t->Branch("gen_charge",      &gen_charge);
      t->Branch("gen_tpid",       &gen_tpid);
    }
  };
}  // namespace

#endif
