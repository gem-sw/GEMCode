#ifndef GEMCode_GEMValidation_CSCDigiStruct
#define GEMCode_GEMValidation_CSCDigiStruct

#include "TTree.h"

namespace gem {

  struct CSCDigiStruct {

    // CSC
    bool has_csc_strips_even;
    bool has_csc_strips_odd;

    bool has_csc_wires_even;
    bool has_csc_wires_odd;

    Int_t nlayers_wg_dg_odd;
    Int_t nlayers_st_dg_odd;

    Int_t nlayers_wg_dg_even;
    Int_t nlayers_st_dg_even;

    int chamber_dg_odd, chamber_dg_even;
    Int_t wiregroup_odd;
    Int_t wiregroup_even;

    Int_t halfstrip_odd;
    Int_t halfstrip_even;

    void init() {
      has_csc_strips_even = 0;
      has_csc_strips_odd = 0;

      has_csc_wires_even = 0;
      has_csc_wires_odd = 0;

      nlayers_wg_dg_odd = -1;
      nlayers_st_dg_odd = -1;
      nlayers_wg_dg_even = -1;
      nlayers_st_dg_even = -1;

      chamber_dg_odd = -1;
      chamber_dg_even = -1;
      wiregroup_odd = -1;
      wiregroup_even = -1;
      halfstrip_odd = -1;
      halfstrip_even = -1;

    };

    void book(TTree* t) {

      t->Branch("chamber_dg_odd", &chamber_dg_odd);
      t->Branch("chamber_dg_even", &chamber_dg_even);

      t->Branch("nlayers_wg_dg_odd", &nlayers_wg_dg_odd);
      t->Branch("nlayers_wg_dg_even", &nlayers_wg_dg_even);
      t->Branch("nlayers_st_dg_odd", &nlayers_st_dg_odd);
      t->Branch("nlayers_st_dg_even", &nlayers_st_dg_even);

      t->Branch("wiregroup_odd", &wiregroup_odd);
      t->Branch("wiregroup_even", &wiregroup_even);
      t->Branch("halfstrip_odd", &halfstrip_odd);
      t->Branch("halfstrip_even", &halfstrip_even);

      t->Branch("has_csc_strips_odd", &has_csc_strips_odd);
      t->Branch("has_csc_wires_odd", &has_csc_wires_odd);
      t->Branch("has_csc_strips_even", &has_csc_strips_even);
      t->Branch("has_csc_wires_even", &has_csc_wires_even);
    }
  };
}  // namespace

#endif
