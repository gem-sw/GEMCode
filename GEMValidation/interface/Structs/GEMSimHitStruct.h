#ifndef GEMCode_GEMValidation_GEMSimHitStruct
#define GEMCode_GEMValidation_GEMSimHitStruct

#include "TTree.h"

namespace gem {

  struct GEMSimHitStruct {

    Float_t dphi_sh_even;
    Float_t dphi_sh_odd;

    Float_t dphipositionpt_gemsh_even, dphipositionpt_gemsh_odd;

    Float_t bending_sh;

    Float_t phi_layer1_sh_even, eta_layer1_sh_even;
    float phi_layer1_sh_odd, eta_layer1_sh_odd;
    float perp_layer1_sh_odd, perp_layer1_sh_even;
    Float_t z_layer1_sh_odd, z_layer1_sh_even;
    Float_t phi_layer6_sh_even, eta_layer6_sh_even;
    float phi_layer6_sh_odd, eta_layer6_sh_odd;
    float perp_layer6_sh_odd, perp_layer6_sh_even;
    Float_t z_layer6_sh_odd, z_layer6_sh_even;
    Float_t perp_gemsh_even, perp_gemsh_odd;
    float centralperp_gemsh_even, centralperp_gemsh_odd;

    bool has_gem_sh_even;
    bool has_gem_sh_odd;

    bool has_gem_sh2_even;
    bool has_gem_sh2_odd;

    bool has_gemcopad_sh_even;
    bool has_gemcopad_sh_odd;

    Float_t strip_gemsh_odd;  // average hits' strip
    Float_t strip_gemsh_even;

    Float_t eta_gemsh_odd;
    Float_t eta_gemsh_even;

    Float_t phi_gemsh_odd;
    Float_t phi_gemsh_even;

    int chamber_sh_odd;
    int chamber_sh_even;

    void init() {
      bending_sh = -10;

      chamber_sh_odd = -1;
      chamber_sh_even = -1;

      perp_gemsh_odd = -0.0;
      perp_gemsh_even = -0.0;

      centralperp_gemsh_odd = -0.0;
      centralperp_gemsh_even = -0.0;

      has_gem_sh_even = false;
      has_gem_sh_odd = false;

      has_gem_sh2_even = false;
      has_gem_sh2_odd = false;

      has_gemcopad_sh_even = false;
      has_gemcopad_sh_odd = false;

      strip_gemsh_odd = -9.;
      strip_gemsh_even = -9.;

      eta_gemsh_odd = -9.;
      eta_gemsh_even = -9.;

      phi_gemsh_odd = -9.;
      phi_gemsh_even = -9.;

      dphi_sh_odd = -9;
      dphi_sh_even = -9;
    };

    void book(TTree* t) {

      t->Branch("bending_sh", &bending_sh);

      t->Branch("chamber_sh_odd", &chamber_sh_odd);
      t->Branch("chamber_sh_even", &chamber_sh_even);

      t->Branch("perp_gemsh_odd", &perp_gemsh_odd);
      t->Branch("perp_gemsh_even", &perp_gemsh_even);

      t->Branch("centralperp_gemsh_odd", &centralperp_gemsh_odd);
      t->Branch("centralperp_gemsh_even", &centralperp_gemsh_even);

      t->Branch("has_gem_sh_odd", &has_gem_sh_odd);
      t->Branch("has_gem_sh_even", &has_gem_sh_even);

      t->Branch("has_gem_sh2_odd", &has_gem_sh2_odd);
      t->Branch("has_gem_sh2_even", &has_gem_sh2_even);

      t->Branch("has_gemcopad_sh_even", &has_gemcopad_sh_even);
      t->Branch("has_gemcopad_sh_odd", &has_gemcopad_sh_odd);

      t->Branch("strip_gemsh_odd", &strip_gemsh_odd);
      t->Branch("strip_gemsh_even", &strip_gemsh_even);

      t->Branch("eta_gemsh_odd", &eta_gemsh_odd);
      t->Branch("eta_gemsh_even", &eta_gemsh_even);

      t->Branch("phi_gemsh_odd", &phi_gemsh_odd);
      t->Branch("phi_gemsh_even", &phi_gemsh_even);

      t->Branch("dphi_sh_odd", &dphi_sh_odd);
      t->Branch("dphi_sh_even", &dphi_sh_even);
    }
  };
}  // namespace

#endif
