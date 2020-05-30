#ifndef GEMCode_GEMValidation_GEMStubStruct
#define GEMCode_GEMValidation_GEMStubStruct

#include "TTree.h"
#include <string>

namespace gem {

  struct GEMStubStruct {

    int pad_odd;
    int pad_even;
    int copad_odd;
    int copad_even;

    bool has_gem_pad_even;
    bool has_gem_pad2_even;
    bool has_gem_copad_even;

    bool has_gem_pad_odd;
    bool has_gem_pad2_odd;
    bool has_gem_copad_odd;

    int bx_pad_odd;
    int bx_pad_even;
    float phi_pad_odd;
    float phi_pad_even;
    float z_pad_odd;
    float z_pad_even;
    float eta_pad_odd;
    float eta_pad_even;

    float dphi_pad_odd;
    float dphi_pad_even;
    float deta_pad_odd;
    float deta_pad_even;

    void init() {
      for (unsigned i = 0 ; i < nStations; i++) {
        pad_odd[i] = -1;
        pad_even[i] = -1;
        copad_odd[i] = -1;
        copad_even[i] = -1;

        has_gem_pad_even[i] = 0;
        has_gem_pad2_even[i] = 0;
        has_gem_copad_even[i] = 0;

        has_gem_pad_odd[i] = 0;
        has_gem_pad2_odd[i] = 0;
        has_gem_copad_odd[i] = 0;

        bx_pad_odd[i] = -9;
        bx_pad_even[i] = -9;
        phi_pad_odd[i] = -9.;
        phi_pad_even[i] = -9.;
        z_pad_odd[i] = -0.;
        z_pad_even[i] = -0.;
        eta_pad_odd[i] = -9.;
        eta_pad_even[i] = -9.;
        dphi_pad_odd[i] = -9.;
        dphi_pad_even[i] = -9.;
        deta_pad_odd[i] = -9.;
        deta_pad_even[i] = -9.;
      }
    };

    void book(TTree* t) {

      t->Branch("pad_odd", pad_odd);
      t->Branch("pad_even", pad_even);
      t->Branch("copad_odd", copad_odd);
      t->Branch("copad_even", copad_even);

      t->Branch("has_gem_pad_odd", has_gem_pad_odd);
      t->Branch("has_gem_pad2_odd", has_gem_pad2_odd);
      t->Branch("has_gem_copad_odd", has_gem_copad_odd);

      t->Branch("has_gem_pad_even", has_gem_pad_even);
      t->Branch("has_gem_pad2_even", has_gem_pad2_even);
      t->Branch("has_gem_copad_even", has_gem_copad_even);

      t->Branch("bx_pad_odd", bx_pad_odd);
      t->Branch("bx_pad_even", bx_pad_even);
      t->Branch("phi_pad_odd", phi_pad_odd);
      t->Branch("phi_pad_even", phi_pad_even);
      t->Branch("z_pad_odd", z_pad_odd);
      t->Branch("z_pad_even", z_pad_even);
      t->Branch("eta_pad_odd", eta_pad_odd);
      t->Branch("eta_pad_even", eta_pad_even);

      t->Branch("dphi_pad_odd", dphi_pad_odd);
      t->Branch("dphi_pad_even", dphi_pad_even);
      t->Branch("deta_pad_odd", deta_pad_odd);
      t->Branch("deta_pad_even", deta_pad_even);
    }
  };
}  // namespace

#endif
