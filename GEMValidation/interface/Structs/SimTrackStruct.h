#ifndef GEMCode_GEMValidation_SimTrackStruct
#define GEMCode_GEMValidation_SimTrackStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace gem {

  struct SimTrackStruct {
    // old code
    float pt, eta, phi, pz, px, py, vx, vy, vz;
    int charge;
    int endcap;
    int pdgid;

    // new code
    p_floats sim_pt;
    p_floats sim_px;
    p_floats sim_py;
    p_floats sim_pz;
    p_floats sim_eta;
    p_floats sim_phi;
    p_ints   sim_charge;
    p_floats sim_dxy;
    p_floats sim_vx;
    p_floats sim_vy;
    p_floats sim_vz;
    p_floats sim_d0;
    p_floats sim_z0;
    p_floats sim_d0_prod;
    p_floats sim_z0_prod;
    p_ints   sim_pdgid;

    void init() {
      pt = 0.;
      phi = 0.;
      eta = -9.;
      px = 0.;
      py = 0.;
      pz = 0.;
      // in cm
      vx = -9999.;
      vy = -9999.;
      vz = -9999.;
      charge = -9;
      endcap = -9;
      pdgid = -9999;

      sim_pt      = new t_floats;
      sim_px      = new t_floats;
      sim_py      = new t_floats;
      sim_pz      = new t_floats;
      sim_eta     = new t_floats;
      sim_phi     = new t_floats;
      sim_dxy     = new t_floats;
      sim_vx     = new t_floats;
      sim_vy     = new t_floats;
      sim_vz     = new t_floats;
      sim_d0      = new t_floats;
      sim_z0      = new t_floats;
      sim_d0_prod = new t_floats;
      sim_z0_prod = new t_floats;
      sim_pdgid   = new t_ints;
      sim_charge  = new t_ints;
    };

    void book(TTree* t) {
      t->Branch("pt", &pt);
      t->Branch("px", &pz);
      t->Branch("py", &pz);
      t->Branch("pz", &pz);
      t->Branch("eta", &eta);
      t->Branch("phi", &phi);
      t->Branch("vx", &vz);
      t->Branch("vy", &vz);
      t->Branch("vz", &vz);
      t->Branch("charge", &charge);
      t->Branch("endcap", &endcap);
      t->Branch("pdgid", &pdgid);

      t->Branch("sim_pt",     &sim_pt);
      t->Branch("sim_px",     &sim_px);
      t->Branch("sim_py",     &sim_py);
      t->Branch("sim_pz",     &sim_pz);
      t->Branch("sim_eta",    &sim_eta);
      t->Branch("sim_phi",    &sim_phi);
      t->Branch("sim_dxy",    &sim_dxy);
      t->Branch("sim_vx",    &sim_vx);
      t->Branch("sim_vy",    &sim_vy);
      t->Branch("sim_vz",    &sim_vz);
      t->Branch("sim_d0",     &sim_d0);
      t->Branch("sim_z0",     &sim_z0);
      t->Branch("sim_d0_prod",     &sim_d0_prod);
      t->Branch("sim_z0_prod",     &sim_z0_prod);
      t->Branch("sim_pdgid",       &sim_pdgid);
      t->Branch("sim_charge",      &sim_charge);
    }
  };
}  // namespace

#endif
