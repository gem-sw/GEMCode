#ifndef GEMCode_GEMValidation_CSCSimHitStruct
#define GEMCode_GEMValidation_CSCSimHitStruct

#include "TTree.h"

namespace gem {

  struct CSCSimHitStruct {

    static const int nStations = 11;

    // bools
    bool chamber_ME1_csc_sh_odd[nStations];
    bool chamber_ME1_csc_sh_even[nStations];

    bool chamber_ME2_csc_sh_even[nStations];
    bool chamber_ME2_csc_sh_odd[nStations];

    bool has_csc_sh_odd[nStations];
    bool has_csc_sh_even[nStations];

    // ints
    Int_t nlayers_csc_sh_even[nStations];
    Int_t nlayers_csc_sh_odd[nStations];

    int chamber_sh_odd[nStations];
    int chamber_sh_even[nStations];

    // floats
    Float_t dphi_sh_even[nStations];
    Float_t dphi_sh_odd[nStations];

    Float_t dphipositionpt_cscsh_even[nStations];
    float dphipositionpt_cscsh_odd[nStations];

    Float_t bending_sh[nStations];
    Float_t phi_cscsh_even[nStations];
    float phi_cscsh_odd[nStations];
    float eta_cscsh_even[nStations];
    float eta_cscsh_odd[nStations];

    Float_t phi_layer1_sh_even[nStations];
    float eta_layer1_sh_even[nStations];
    float phi_layer1_sh_odd[nStations];
    float eta_layer1_sh_odd[nStations];
    float perp_layer1_sh_odd[nStations];
    float perp_layer1_sh_even[nStations];
    Float_t z_layer1_sh_odd[nStations];
    float z_layer1_sh_even[nStations];
    Float_t phi_layer6_sh_even[nStations];
    float eta_layer6_sh_even[nStations];
    float phi_layer6_sh_odd[nStations];
    float eta_layer6_sh_odd[nStations];
    float perp_layer6_sh_odd[nStations];
    float perp_layer6_sh_even[nStations];
    Float_t z_layer6_sh_odd[nStations];
    float z_layer6_sh_even[nStations];
    float perp_cscsh_even[nStations];
    float perp_cscsh_odd[nStations];

    void init() {
      for (unsigned i = 0 ; i < nStations; i++) {

        bending_sh[i] = -10;

        chamber_ME1_csc_sh_even[i] = 0;
        chamber_ME1_csc_sh_odd[i] = 0;

        chamber_ME2_csc_sh_even[i] = 0;
        chamber_ME2_csc_sh_odd[i] = 0;

        chamber_sh_odd[i] = -1;
        chamber_sh_even[i] = -1;

        nlayers_csc_sh_odd[i] = -1;
        nlayers_csc_sh_even[i] = -1;

        perp_cscsh_odd[i] = -0.0;
        perp_cscsh_even[i] = -0.0;

        phi_cscsh_even[i] = -9.0;
        phi_cscsh_odd[i] = -9.0;

        eta_cscsh_even[i] = -9.0;
        eta_cscsh_odd[i] = -9.0;

        has_csc_sh_even[i] = false;
        has_csc_sh_odd[i] = false;

        dphi_sh_odd[i] = -9;
        dphi_sh_even[i] = -9;
      }
    };

    void book(TTree* t) {

      t->Branch("bending_sh", &bending_sh);

      t->Branch("has_csc_sh_even", &has_csc_sh_even);
      t->Branch("has_csc_sh_odd", &has_csc_sh_odd);

      t->Branch("chamber_ME1_csc_sh_odd", &chamber_ME1_csc_sh_odd);
      t->Branch("chamber_ME1_csc_sh_even", &chamber_ME1_csc_sh_even);

      t->Branch("chamber_ME2_csc_sh_odd", &chamber_ME2_csc_sh_odd);
      t->Branch("chamber_ME2_csc_sh_even", &chamber_ME2_csc_sh_even);

      t->Branch("chamber_sh_odd", &chamber_sh_odd);
      t->Branch("chamber_sh_even", &chamber_sh_even);

      t->Branch("nlayers_csc_sh_odd", &nlayers_csc_sh_odd);
      t->Branch("nlayers_csc_sh_even", &nlayers_csc_sh_even);

      t->Branch("perp_cscsh_odd", &perp_cscsh_odd);
      t->Branch("perp_cscsh_even", &perp_cscsh_even);

      t->Branch("phi_cscsh_even", &phi_cscsh_even);
      t->Branch("phi_cscsh_odd", &phi_cscsh_odd);

      t->Branch("eta_cscsh_even", &eta_cscsh_even);
      t->Branch("eta_cscsh_odd", &eta_cscsh_odd);

      t->Branch("dphi_sh_odd", &dphi_sh_odd);
      t->Branch("dphi_sh_even", &dphi_sh_even);
    }
  };
}  // namespace

#endif
