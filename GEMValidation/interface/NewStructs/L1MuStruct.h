#ifndef GEMCode_GEMValidation_MY_L1MuStruct
#define GEMCode_GEMValidation_MY_L1MuStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace my {

  struct L1MuStruct {

    p_floats emtftrack_pt;
    p_floats emtftrack_eta;
    p_floats emtftrack_phi;
    p_ints   emtftrack_charge;
    p_ints   emtftrack_bx;
    p_ints   emtftrack_tpid;

    p_floats emtfcand_pt;
    p_floats emtfcand_eta;
    p_floats emtfcand_phi;
    p_ints   emtfcand_charge;
    p_ints   emtfcand_bx;
    p_ints   emtfcand_tpid;

    p_floats l1mu_pt;
    p_floats l1mu_eta;
    p_floats l1mu_phi;
    p_ints   l1mu_charge;
    p_ints   l1mu_bx;
    p_ints   l1mu_tpid;

    void init() {
      emtftrack_pt = new t_floats;
      emtftrack_eta = new t_floats;
      emtftrack_phi = new t_floats;
      emtftrack_charge = new t_ints;
      emtftrack_bx = new t_ints;

      emtfcand_pt = new t_floats;
      emtfcand_eta = new t_floats;
      emtfcand_phi = new t_floats;
      emtfcand_charge = new t_ints;
      emtfcand_bx = new t_ints;

      l1mu_pt = new t_floats;
      l1mu_eta = new t_floats;
      l1mu_phi = new t_floats;
      l1mu_charge = new t_ints;
      l1mu_bx = new t_ints;
    };

    void clear(){
      emtftrack_pt->clear();
      emtftrack_eta->clear();
      emtftrack_phi->clear();
      emtftrack_charge->clear();
      emtftrack_bx->clear();

      emtfcand_pt->clear();
      emtfcand_eta->clear();
      emtfcand_phi->clear();
      emtfcand_charge->clear();
      emtfcand_bx->clear();

      l1mu_pt->clear();
      l1mu_eta->clear();
      l1mu_phi->clear();
      l1mu_charge->clear();
      l1mu_bx->clear();
    }

    void book(TTree* t) {
      t->Branch("emtftrack_pt", &emtftrack_pt);
      t->Branch("emtftrack_eta", &emtftrack_eta);
      t->Branch("emtftrack_phi", &emtftrack_phi);
      t->Branch("emtftrack_charge", &emtftrack_charge);
      t->Branch("emtftrack_bx", &emtftrack_bx);
      t->Branch("emtftrack_tpid", &emtftrack_tpid);


      t->Branch("emtfcand_pt", &emtfcand_pt);
      t->Branch("emtfcand_eta", &emtfcand_eta);
      t->Branch("emtfcand_phi", &emtfcand_phi);
      t->Branch("emtfcand_charge", &emtfcand_charge);
      t->Branch("emtfcand_bx", &emtfcand_bx);
      t->Branch("emtfcand_tpid", &emtfcand_tpid);

      t->Branch("l1mu_pt", &l1mu_pt);
      t->Branch("l1mu_eta", &l1mu_eta);
      t->Branch("l1mu_phi", &l1mu_phi);
      t->Branch("l1mu_charge", &l1mu_charge);
      t->Branch("l1mu_bx", &l1mu_bx);
      t->Branch("l1mu_tpid", &l1mu_tpid);
    }
  };
}  // namespace

#endif
