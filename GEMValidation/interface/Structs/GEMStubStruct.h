#ifndef GEMCode_GEMValidation_GEMStubStruct
#define GEMCode_GEMValidation_GEMStubStruct

#include "GEMCode/GEMValidation/interface/Structs/BaseStruct.h"

namespace gem {

  struct GEMStubStruct {

    static const int nStations = 3;

    // bools
    bool has_gem_pad_even[nStations];
    bool has_gem_pad2_even[nStations];
    bool has_gem_copad_even[nStations];
    bool has_gem_cluster_even[nStations];
    bool has_gem_cluster2_even[nStations];

    bool has_gem_pad_odd[nStations];
    bool has_gem_pad2_odd[nStations];
    bool has_gem_copad_odd[nStations];
    bool has_gem_cluster_odd[nStations];
    bool has_gem_cluster2_odd[nStations];

    // ints
    int pad1_odd[nStations];
    int pad1_even[nStations];
    int bx_pad1_odd[nStations];
    int bx_pad1_even[nStations];

    int pad2_odd[nStations];
    int pad2_even[nStations];
    int bx_pad2_odd[nStations];
    int bx_pad2_even[nStations];

    int copad_odd[nStations];
    int copad_even[nStations];
    int bx_copad_odd[nStations];
    int bx_copad_even[nStations];

    int bx_cluster1_odd[nStations];
    int bx_cluster1_even[nStations];
    int bx_cluster2_odd[nStations];
    int bx_cluster2_even[nStations];

    // floats - this is based on mean GEM position
    float z_pad1_odd[nStations];
    float z_pad1_even[nStations];
    float eta_pad1_odd[nStations];
    float eta_pad1_even[nStations];
    float phi_pad1_odd[nStations];
    float phi_pad1_even[nStations];

    float z_pad2_odd[nStations];
    float z_pad2_even[nStations];
    float eta_pad2_odd[nStations];
    float eta_pad2_even[nStations];
    float phi_pad2_odd[nStations];
    float phi_pad2_even[nStations];

    float z_copad_odd[nStations];
    float z_copad_even[nStations];
    float eta_copad_odd[nStations];
    float eta_copad_even[nStations];
    float phi_copad_odd[nStations];
    float phi_copad_even[nStations];

    // floats - between GEM stub and GEM simhit
    float dphi_pad1_odd[nStations];
    float dphi_pad1_even[nStations];
    float deta_pad1_odd[nStations];
    float deta_pad1_even[nStations];

    float dphi_pad2_odd[nStations];
    float dphi_pad2_even[nStations];
    float deta_pad2_odd[nStations];
    float deta_pad2_even[nStations];

    float dphi_copad_odd[nStations];
    float dphi_copad_even[nStations];
    float deta_copad_odd[nStations];
    float deta_copad_even[nStations];

    // floats - between GEM stub and CSC stub
    float dphi_lct_pad1_odd[nStations];
    float dphi_lct_pad1_even[nStations];
    float deta_lct_pad1_odd[nStations];
    float deta_lct_pad1_even[nStations];

    float dphi_lct_pad2_odd[nStations];
    float dphi_lct_pad2_even[nStations];
    float deta_lct_pad2_odd[nStations];
    float deta_lct_pad2_even[nStations];

    float dphi_lct_copad_odd[nStations];
    float dphi_lct_copad_even[nStations];
    float deta_lct_copad_odd[nStations];
    float deta_lct_copad_even[nStations];

    // new stuff
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

      for (unsigned i = 0 ; i < nStations; i++) {

        has_gem_pad_even[i]= false;
        has_gem_pad2_even[i]= false;
        has_gem_copad_even[i]= false;
        has_gem_cluster_even[i]= false;
        has_gem_cluster2_even[i]= false;

        has_gem_pad_odd[i]= false;
        has_gem_pad2_odd[i]= false;
        has_gem_copad_odd[i]= false;
        has_gem_cluster_odd[i]= false;
        has_gem_cluster2_odd[i]= false;

        pad1_odd[i] = -1;
        pad1_even[i] = -1;
        pad2_odd[i] = -1;
        pad2_even[i] = -1;

        bx_pad1_odd[i] = -1;
        bx_pad1_even[i] = -1;
        bx_pad2_odd[i] = -1;
        bx_pad2_even[i] = -1;

        copad_odd[i] = -1;
        copad_even[i] = -1;

        bx_copad_odd[i] = -1;
        bx_copad_even[i] = -1;

        bx_cluster1_odd[i] = -1;
        bx_cluster1_even[i] = -1;
        bx_cluster2_odd[i] = -1;
        bx_cluster2_even[i] = -1;

        z_pad1_odd[i] = -0.;
        z_pad1_even[i] = -0.;
        eta_pad1_odd[i] = -9.;
        eta_pad1_even[i] = -9.;
        phi_pad1_odd[i] = -9.;
        phi_pad1_even[i] = -9.;

        z_pad2_odd[i] = -0.;
        z_pad2_even[i] = -0.;
        eta_pad2_odd[i] = -9.;
        eta_pad2_even[i] = -9.;
        phi_pad2_odd[i] = -9.;
        phi_pad2_even[i] = -9.;

        z_copad_odd[i] = -0.;
        z_copad_even[i] = -0.;
        eta_copad_odd[i] = -9.;
        eta_copad_even[i] = -9.;
        phi_copad_odd[i] = -9.;
        phi_copad_even[i] = -9.;

        deta_pad1_odd[i] = -9.;
        deta_pad1_even[i] = -9.;
        dphi_pad1_odd[i] = -9.;
        dphi_pad1_even[i] = -9.;

        deta_pad2_odd[i] = -9.;
        deta_pad2_even[i] = -9.;
        dphi_pad2_odd[i] = -9.;
        dphi_pad2_even[i] = -9.;

        deta_copad_odd[i] = -9.;
        deta_copad_even[i] = -9.;
        dphi_copad_odd[i] = -9.;
        dphi_copad_even[i] = -9.;



        deta_lct_pad1_odd[i] = -9.;
        deta_lct_pad1_even[i] = -9.;
        dphi_lct_pad1_odd[i] = -9.;
        dphi_lct_pad1_even[i] = -9.;

        deta_lct_pad2_odd[i] = -9.;
        deta_lct_pad2_even[i] = -9.;
        dphi_lct_pad2_odd[i] = -9.;
        dphi_lct_pad2_even[i] = -9.;

        deta_lct_copad_odd[i] = -9.;
        deta_lct_copad_even[i] = -9.;
        dphi_lct_copad_odd[i] = -9.;
        dphi_lct_copad_even[i] = -9.;
      }
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


      t->Branch("has_gem_pad_odd", has_gem_pad_odd, "has_gem_pad_odd[3]/O");
      t->Branch("has_gem_pad2_odd", has_gem_pad2_odd, "has_gem_pad2_odd[3]/O");
      t->Branch("has_gem_copad_odd", has_gem_copad_odd, "has_gem_copad_odd[3]/O");
      t->Branch("has_gem_cluster_odd", has_gem_cluster_odd, "has_gem_cluster_odd[3]/O");
      t->Branch("has_gem_cluster2_odd", has_gem_cluster2_odd, "has_gem_cluster2_odd[3]/O");

      t->Branch("has_gem_pad_even", has_gem_pad_even, "has_gem_pad_even[3]/O");
      t->Branch("has_gem_pad2_even", has_gem_pad2_even, "has_gem_pad2_even[3]/O");
      t->Branch("has_gem_copad_even", has_gem_copad_even, "has_gem_copad_even[3]/O");
      t->Branch("has_gem_cluster_even", has_gem_cluster_even, "has_gem_cluster_even[3]/O");
      t->Branch("has_gem_cluster2_even", has_gem_cluster2_even, "has_gem_cluster2_even[3]/O");

      t->Branch("pad1_odd", pad1_odd, "pad1_odd[3]/I");
      t->Branch("pad1_even", pad1_even, "pad1_even[3]/I");
      t->Branch("pad2_odd", pad2_odd, "pad2_odd[3]/I");
      t->Branch("pad2_even", pad2_even, "pad2_even[3]/I");

      t->Branch("bx_pad1_odd", bx_pad1_odd, "bx_pad1_odd[3]/I");
      t->Branch("bx_pad1_even", bx_pad1_even, "bx_pad1_even[3]/I");
      t->Branch("bx_pad2_odd", bx_pad2_odd, "bx_pad2_odd[3]/I");
      t->Branch("bx_pad2_even", bx_pad2_even, "bx_pad2_even[3]/I");

      t->Branch("copad_odd", copad_odd, "copad_odd[3]/I");
      t->Branch("copad_even", copad_even, "copad_odd[3]/I");
      t->Branch("bx_copad_odd", bx_copad_odd, "bx_copad_odd[3]/I");
      t->Branch("bx_copad_even", bx_copad_even, "bx_copad_odd[3]/I");

      t->Branch("bx_cluster1_odd", bx_cluster1_odd, "bx_cluster1_odd[3]/I");
      t->Branch("bx_cluster1_even", bx_cluster1_even, "bx_cluster1_even[3]/I");
      t->Branch("bx_cluster2_odd", bx_cluster2_odd, "bx_cluster2_odd[3]/I");
      t->Branch("bx_cluster2_even", bx_cluster2_even, "bx_cluster2_even[3]/I");

      t->Branch("z_pad1_odd", z_pad1_odd, "z_pad1_odd[3]/F");
      t->Branch("z_pad1_even", z_pad1_even, "z_pad1_even[3]/F");
      t->Branch("eta_pad1_odd", eta_pad1_odd, "eta_pad1_odd[3]/F");
      t->Branch("eta_pad1_even", eta_pad1_even, "eta_pad1_even[3]/F");
      t->Branch("phi_pad1_odd", phi_pad1_odd, "phi_pad1_odd[3]/F");
      t->Branch("phi_pad1_even", phi_pad1_even, "phi_pad1_even[3]/F");

      t->Branch("z_pad2_odd", z_pad2_odd, "z_pad2_odd[3]/F");
      t->Branch("z_pad2_even", z_pad2_even, "z_pad2_even[3]/F");
      t->Branch("eta_pad2_odd", eta_pad2_odd, "eta_pad2_odd[3]/F");
      t->Branch("eta_pad2_even", eta_pad2_even, "eta_pad2_even[3]/F");
      t->Branch("phi_pad2_odd", phi_pad2_odd, "phi_pad2_odd[3]/F");
      t->Branch("phi_pad2_even", phi_pad2_even, "phi_pad2_even[3]/F");

      t->Branch("z_copad_odd", z_copad_odd, "z_copad_odd[3]/F");
      t->Branch("z_copad_even", z_copad_even, "z_copad_even[3]/F");
      t->Branch("eta_copad_odd", eta_copad_odd, "eta_copad_odd[3]/F");
      t->Branch("eta_copad_even", eta_copad_even, "eta_copad_even[3]/F");
      t->Branch("phi_copad_odd", phi_copad_odd, "phi_copad_odd[3]/F");
      t->Branch("phi_copad_even", phi_copad_even, "phi_copad_even[3]/F");


      t->Branch("dphi_pad1_odd", dphi_pad1_odd, "dphi_pad1_odd[3]/F");
      t->Branch("dphi_pad1_even", dphi_pad1_even, "dphi_pad1_even[3]/F");
      t->Branch("deta_pad1_odd", deta_pad1_odd, "deta_pad1_odd[3]/F");
      t->Branch("deta_pad1_even", deta_pad1_even, "deta_pad1_even[3]/F");

      t->Branch("dphi_pad2_odd", dphi_pad2_odd, "dphi_pad2_odd[3]/F");
      t->Branch("dphi_pad2_even", dphi_pad2_even, "dphi_pad2_even[3]/F");
      t->Branch("deta_pad2_odd", deta_pad2_odd, "deta_pad2_odd[3]/F");
      t->Branch("deta_pad2_even", deta_pad2_even, "deta_pad2_even[3]/F");

      t->Branch("dphi_copad_odd", dphi_copad_odd, "dphi_copad_odd[3]/F");
      t->Branch("dphi_copad_even", dphi_copad_even, "dphi_copad_even[3]/F");
      t->Branch("deta_copad_odd", deta_copad_odd, "deta_copad_odd[3]/F");
      t->Branch("deta_copad_even", deta_copad_even, "deta_copad_even[3]/F");


      t->Branch("dphi_lct_pad1_odd", dphi_lct_pad1_odd, "dphi_lct_pad1_odd[3]/F");
      t->Branch("dphi_lct_pad1_even", dphi_lct_pad1_even, "dphi_lct_pad1_even[3]/F");
      t->Branch("deta_lct_pad1_odd", deta_lct_pad1_odd, "deta_lct_pad1_odd[3]/F");
      t->Branch("deta_lct_pad1_even", deta_lct_pad1_even, "deta_lct_pad1_even[3]/F");

      t->Branch("dphi_lct_pad2_odd", dphi_lct_pad2_odd, "dphi_lct_pad2_odd[3]/F");
      t->Branch("dphi_lct_pad2_even", dphi_lct_pad2_even, "dphi_lct_pad2_even[3]/F");
      t->Branch("deta_lct_pad2_odd", deta_lct_pad2_odd, "deta_lct_pad2_odd[3]/F");
      t->Branch("deta_lct_pad2_even", deta_lct_pad2_even, "deta_lct_pad2_even[3]/F");

      t->Branch("dphi_lct_copad_odd", dphi_lct_copad_odd, "dphi_lct_copad_odd[3]/F");
      t->Branch("dphi_lct_copad_even", dphi_lct_copad_even, "dphi_lct_copad_even[3]/F");
      t->Branch("deta_lct_copad_odd", deta_lct_copad_odd, "deta_lct_copad_odd[3]/F");
      t->Branch("deta_lct_copad_even", deta_lct_copad_even, "deta_lct_copad_even[3]/F");
    }
  };
}  // namespace

#endif
