import ROOT
from array import array

from helpers.stations import *
from helpers.tools import *


def printCSCSimhitsInSimtrack(tree):
    print(cscStations[st].label," simhits in even ", tree.has_csc_sh_even[st], " chamber ", tree.chamber_sh_even[st]," eta ", tree.eta_csc_sh_even[st]," phi ", tree.phi_csc_sh_even[st]," strip ", tree.strip_csc_sh_even[st])
    print(cscStations[st].label," simhits in odd ", tree.has_csc_sh_odd[st], " chamber ", tree.chamber_sh_odd[st]," eta ", tree.eta_csc_sh_odd[st]," phi ", tree.phi_csc_sh_odd[st]," strip ", tree.strip_csc_sh_odd[st])

def printCSCStubInSimtrack(tree, st):
    """print out stubs for the simtrack"""
    print(cscStations[st].label, " Stub in even ", tree.has_lct_even[st], " wg ", tree.wg_lct_even[st], " hs ", tree.hs_lct_even[st],"  es ", tree.es_lct_even[st]," bend ", tree.bend_lct_even[st]," eta ",tree.eta_lct_even[st], " phi ", tree.phi_lct_even[st])
    print(cscStations[st].label, " Stub in odd ", tree.has_lct_odd[st], " wg ", tree.wg_lct_odd[st], " hs ", tree.hs_lct_odd[st],"  es ", tree.es_lct_odd[st]," bend ", tree.bend_lct_odd[st]," eta ",tree.eta_lct_odd[st], " phi ", tree.phi_lct_odd[st])

def printEmtfTrack(tree):
    print("SimTrack pt ", tree.pt, " eta ", tree.eta, " emtf pt ", tree.emtf_pt, " eta ", tree.emtf_eta, " mode ", tree.mode, " dphi12 ",tree.deltaphi12," dphi23 ", tree.deltaphi23)
    print("\tst1_phi ",tree.emtfhit_st1_phi, " st2_phi ", tree.emtfhit_st2_phi, " simStub_st1_phi ", tree.cscstub_st1_phi, " simStub_st2_phi ", tree.cscstub_st2_phi," simhits_st1_phi ", tree.simhits_st1_phi, " simhits_st2_phi ", tree.simhits_st2_phi)
    print("\tst1_hs ", tree.emtfhit_st1_halfstrip," st2_hs ", tree.emtfhit_st2_halfstrip, " simStub_st1_hs ", tree.cscstub_st1_halfstrip," simStub_st2_halfstrip ", tree.cscstub_st2_halfstrip)
    print("\tst1 pattern ", tree.emtfhit_st1_pattern, " st2 pattern ", tree.emtfhit_st2_pattern, " simStub_st1_pattern ", tree.cscstub_st1_pattern, " simStub_st2_pattern ",tree.cscstub_st2_pattern, " st1 stubmatch ", tree.cscstub_st1_matched, " st2 stubmatch ", tree.cscstub_st2_matched )

def analyzeTrees(plotterlist):
    #tree = self.dirAna.Get("simTrack")
    totalEntries  = plotterlist[0].getTree().GetEntries()
    for nEv in range(0, 10):
        for plotter in plotterlist:
            tree = plotter.getTree()
            tree.GetEntry(nEv)
            print(plotter.analyzer," ievent ",  tree.ievent," emtf_pt ", tree.emtf_pt, " emtf_eta ", tree.emtf_eta, " genpt ", tree.pt," geneta ", tree.eta)

def analyzeTwoTrees(plotter0, plotter1, treename, filename):
    f = ROOT.TFile(filename, "recreate"); f.cd()
    newTree = ROOT.TTree(treename, treename)
    totalEntries0 = plotter0.getTree().GetEntries()
    totalEntries1 = plotter1.getTree().GetEntries()
    print("plotter0 ", plotter0.analyzer, " entries ", totalEntries0, " plotter1 ", plotter1.analyzer, " entries ", totalEntries1)
    tree0 = plotter0.getTree()
    tree1 = plotter1.getTree()
    tree0.GetEntry(0)
    tree1.GetEntry(0)

    maxn= 1
    tree0_ievent   = array( 'f', maxn*[ 0 ] )
    tree0_eta      = array( 'f', maxn*[ 0. ] ) #np.zeros(1, dtype=float)
    tree0_phi      = array( 'f', maxn*[ 0. ] ) #np.zeros(1, dtype=float)
    tree0_pt       = array( 'f', maxn*[ 0. ] ) #np.zeros(1, dtype=float)
    tree0_emtf_eta = array( 'f', maxn*[ 0. ] ) #np.zeros(1, dtype=float)
    tree0_emtf_phi = array( 'f', maxn*[ 0. ] ) #np.zeros(1, dtype=float)
    tree0_emtf_pt  = array( 'f', maxn*[ 0. ] ) #np.zeros(1, dtype=float)
    tree1_ievent   = array( 'f', maxn*[ 0 ] )
    tree1_eta      = array( 'f', maxn*[ 0. ] ) #np.zeros(1, dtype=float)
    tree1_phi      = array( 'f', maxn*[ 0. ] ) #np.zeros(1, dtype=float)
    tree1_pt       = array( 'f', maxn*[ 0. ] ) #np.zeros(1, dtype=float)
    tree1_emtf_eta = array( 'f', maxn*[ 0. ] ) #np.zeros(1, dtype=float)
    tree1_emtf_phi = array( 'f', maxn*[ 0. ] ) #np.zeros(1, dtype=float)
    tree1_emtf_pt  = array( 'f', maxn*[ 0. ] ) #np.zeros(1, dtype=float)

    tree0_hasME1  = array('f', maxn*[0])
    tree0_hasME2  = array('f', maxn*[0])
    tree0_hasME3  = array('f', maxn*[0])
    tree0_hasME4  = array('f', maxn*[0])
    tree0_nstubs  = array('f', maxn*[0])
    tree0_mode    = array('f', maxn*[0])
    tree1_hasME1  = array('f', maxn*[0])
    tree1_hasME2  = array('f', maxn*[0])
    tree1_hasME3  = array('f', maxn*[0])
    tree1_hasME4  = array('f', maxn*[0])
    tree1_nstubs  = array('f', maxn*[0])
    tree1_mode    = array('f', maxn*[0])
    
    tree0_simhits_phi_all = []#[array( 'f', maxn*[ -9.0 ] )] * len(cscStations)
    tree0_lct_phi_all     = []#[array( 'f', maxn*[ -9.0 ] )] * len(cscStations)
    tree1_simhits_phi_all = []#[array( 'f', maxn*[ -9.0 ] )] * len(cscStations)
    tree1_lct_phi_all     = []#[array( 'f', maxn*[ -9.0 ] )] * len(cscStations)
    simhits_dphi_all      = []#[array( 'f', maxn*[ -9.0 ] )] * len(cscStations)
    lct_dphi_all          = []#[array( 'f', maxn*[ -9.0 ] )] * len(cscStations)
    tree0_lct_pattern_all = []#[array( 'f', maxn*[ 0 ] )] * len(cscStations)
    tree1_lct_pattern_all = []#[array( 'f', maxn*[ 0 ] )] * len(cscStations)
    
    for st in range(len(cscStations)):
        tree0_simhits_phi_all.append(array( 'f', maxn*[ -9.0 ] ))#] * len(cscStations)
        tree0_lct_phi_all.append(array( 'f', maxn*[ -9.0 ] ))#] * len(cscStations)
        tree1_simhits_phi_all.append(array( 'f', maxn*[ -9.0 ] ))#] * len(cscStations)
        tree1_lct_phi_all.append(array( 'f', maxn*[ -9.0 ] ))#] * len(cscStations)
        simhits_dphi_all.append(array( 'f', maxn*[ -9.0 ] ))#] * len(cscStations)
        lct_dphi_all.append(array( 'f', maxn*[ -9.0 ] ))#] * len(cscStations)
        tree0_lct_pattern_all.append(array( 'f', maxn*[ 0 ] )   )#] * len(cscStations)
        tree1_lct_pattern_all.append(array( 'f', maxn*[ 0 ] )   )#] * len(cscStations)
    
    tree0_emtfhit_st_halfstrip     = []#array( 'f', maxn*[ -9.0 ] )] * 4
    tree0_cscstub_st_halfstrip     = []#array( 'f', maxn*[ -9.0 ] )] * 4
    tree1_emtfhit_st_halfstrip     = []#array( 'f', maxn*[ -9.0 ] )] * 4
    tree1_cscstub_st_halfstrip     = []#array( 'f', maxn*[ -9.0 ] )] * 4
    tree0_emtfhit_st_phi           = []#array( 'f', maxn*[ -9.0 ] )] * 4
    tree0_cscstub_st_phi           = []#array( 'f', maxn*[ -9.0 ] )] * 4
    tree0_simhits_st_phi           = []#array( 'f', maxn*[ -9.0 ] )] * 4
    tree1_emtfhit_st_phi           = []#array( 'f', maxn*[ -9.0 ] )] * 4
    tree1_cscstub_st_phi           = []#array( 'f', maxn*[ -9.0 ] )] * 4
    tree0_emtfhit_st_pattern       = []#array( 'f', maxn*[  0 ] )] * 4
    tree0_cscstub_st_pattern       = []#array( 'f', maxn*[  0 ] )] * 4
    tree1_emtfhit_st_pattern       = []#array( 'f', maxn*[  0 ] )] * 4
    tree1_cscstub_st_pattern       = []#array( 'f', maxn*[  0 ] )] * 4
    tree1_simhits_st_phi           = []#array( 'f', maxn*[ -9.0 ] )] * 4

    emtfhit_st_phidiff = []#array( 'f', maxn*[ -9.0 ] )] * 4
    cscstub_st_phidiff = []#array( 'f', maxn*[ -9.0 ] )] * 4
    simhits_st_phidiff = []#array( 'f', maxn*[ -9.0 ] )] * 4
    emtfhit_st_match   = []#array('f', maxn*[0])] * 4
    cscstub_st_match   = []#array('f', maxn*[0])] * 4
    simhits_st_match   = []#array('f', maxn*[0])] * 4
    for st in range(0,4):
        tree0_emtfhit_st_halfstrip.append(array( 'f', maxn*[ -9.0 ] ))#] * 4
        tree0_cscstub_st_halfstrip.append(array( 'f', maxn*[ -9.0 ] ))#] * 4
        tree1_emtfhit_st_halfstrip.append(array( 'f', maxn*[ -9.0 ] ))#] * 4
        tree1_cscstub_st_halfstrip.append(array( 'f', maxn*[ -9.0 ] ))#] * 4
        tree0_emtfhit_st_phi.append(array( 'f', maxn*[ -9.0 ] )      )#] * 4
        tree0_cscstub_st_phi.append(array( 'f', maxn*[ -9.0 ] )      )#] * 4
        tree0_simhits_st_phi.append(array( 'f', maxn*[ -9.0 ] )      )#] * 4
        tree1_emtfhit_st_phi.append(array( 'f', maxn*[ -9.0 ] )      )#] * 4
        tree1_cscstub_st_phi.append(array( 'f', maxn*[ -9.0 ] )      )#] * 4
        tree0_emtfhit_st_pattern.append(array( 'f', maxn*[  0 ] ))#] * 4
        tree0_cscstub_st_pattern.append(array( 'f', maxn*[  0 ] ))#] * 4
        tree1_emtfhit_st_pattern.append(array( 'f', maxn*[  0 ] ))#] * 4
        tree1_cscstub_st_pattern.append(array( 'f', maxn*[  0 ] ))#] * 4
        tree1_simhits_st_phi.append(array( 'f', maxn*[ -9.0 ] )  )#] * 4

        emtfhit_st_phidiff.append(array( 'f', maxn*[ -9.0 ] ))#] * 4
        cscstub_st_phidiff.append(array( 'f', maxn*[ -9.0 ] ))#] * 4
        simhits_st_phidiff.append(array( 'f', maxn*[ -9.0 ] ))#] * 4
        emtfhit_st_match.append(array('f', maxn*[0]))#] * 4
        cscstub_st_match.append(array('f', maxn*[0]))#] * 4
        simhits_st_match.append(array('f', maxn*[0]))#] * 4

    emtfhit_nmismatch = array('f', maxn*[0])
    cscstub_nmismatch = array('f', maxn*[0])
    simhits_nmismatch = array('f', maxn*[0])

    def extractTree0():
        tree0_ievent[0] = tree0.ievent
        tree0_eta[0] = tree0.eta
        tree0_phi[0] = tree0.phi
        tree0_pt[0]  = tree0.pt
        tree0_emtf_eta[0] = tree0.emtf_eta
        tree0_emtf_phi[0] = tree0.emtf_phi
        tree0_emtf_pt[0]  = tree0.emtf_pt
        tree0_hasME1[0]   = int(tree0.hasME1)
        tree0_hasME2[0]   = int(tree0.hasME2)
        tree0_hasME3[0]   = int(tree0.hasME3)
        tree0_hasME4[0]   = int(tree0.hasME4)
        tree0_nstubs[0]   = tree0.nstubs
        tree0_mode[0]     = tree0.mode
        for st in range(0, len(cscStations)):
            tree0_simhits_phi_all[st][0] = max(tree0.phi_csc_sh_odd[st], tree0.phi_csc_sh_even[st])
            tree0_lct_phi_all[st][0]     = max(tree0.phi_lct_odd[st], tree0.phi_lct_even[st])
            tree0_lct_pattern_all[st][0] = max(tree0.bend_lct_odd[st], tree0.bend_lct_even[st])

        for st in range(0, 4):
            tree0_emtfhit_st_phi[st][0]      = getattr(tree0, "emtfhit_st%d_phi"%(st+1))
            tree0_emtfhit_st_halfstrip[st][0]= getattr(tree0, "emtfhit_st%d_halfstrip"%(st+1))
            tree0_emtfhit_st_pattern[st][0]  = getattr(tree0, "emtfhit_st%d_pattern"%(st+1))
            tree0_cscstub_st_phi[st][0]      = getattr(tree0, "cscstub_st%d_phi"%(st+1))
            tree0_cscstub_st_halfstrip[st][0]= getattr(tree0, "cscstub_st%d_halfstrip"%(st+1))
            tree0_cscstub_st_pattern[st][0]  = getattr(tree0, "cscstub_st%d_pattern"%(st+1))
            tree0_simhits_st_phi[st][0]      = getattr(tree0, "simhits_st%d_phi"%(st+1))


    def extractTree1():
        tree1_ievent[0] = tree1.ievent
        tree1_eta[0] = tree1.eta
        tree1_phi[0] = tree1.phi
        tree1_pt[0]  = tree1.pt
        tree1_emtf_eta[0] = tree1.emtf_eta
        tree1_emtf_phi[0] = tree1.emtf_phi
        tree1_emtf_pt[0]  = tree1.emtf_pt
        tree1_hasME1[0]   = int(tree1.hasME1)
        tree1_hasME2[0]   = int(tree1.hasME2)
        tree1_hasME3[0]   = int(tree1.hasME3)
        tree1_hasME4[0]   = int(tree1.hasME4)
        tree1_nstubs[0]   = tree1.nstubs
        tree1_mode[0]     = tree1.mode
        for st in range(0, len(cscStations)):
            tree1_simhits_phi_all[st][0] = max(tree1.phi_csc_sh_odd[st], tree1.phi_csc_sh_even[st])
            tree1_lct_phi_all[st][0]     = max(tree1.phi_lct_odd[st], tree1.phi_lct_even[st])
            tree1_lct_pattern_all[st][0] = max(tree1.bend_lct_odd[st], tree1.bend_lct_even[st])

        for st in range(0, 4):
            tree1_emtfhit_st_phi[st][0]      = getattr(tree1, "emtfhit_st%d_phi"%(st+1))
            tree1_emtfhit_st_halfstrip[st][0]= getattr(tree1, "emtfhit_st%d_halfstrip"%(st+1))
            tree1_emtfhit_st_pattern[st][0]  = getattr(tree1, "emtfhit_st%d_pattern"%(st+1))
            tree1_cscstub_st_phi[st][0]      = getattr(tree1, "cscstub_st%d_phi"%(st+1))
            tree1_cscstub_st_halfstrip[st][0]= getattr(tree1, "cscstub_st%d_halfstrip"%(st+1))
            tree1_cscstub_st_pattern[st][0]  = getattr(tree1, "cscstub_st%d_pattern"%(st+1))
            tree1_simhits_st_phi[st][0]      = getattr(tree1, "simhits_st%d_phi"%(st+1))



    def initBranches():
        emtfhit_nmismatch[0] = 0
        simhits_nmismatch[0] = 0
        cscstub_nmismatch[0] = 0
        for st in range(0, 4):
            emtfhit_st_match[st][0] = 0  
            simhits_st_match[st][0] = 0 
            cscstub_st_match[st][0] = 0 
            emtfhit_st_phidiff[st][0] = -9.0
            simhits_st_phidiff[st][0] = -9.0
            cscstub_st_phidiff[st][0] = -9.0

        for st in range(0, len(cscStations)):
            if tree0_lct_phi_all[st][0] > -9.0 and tree1_lct_phi_all[st][0] > -9.0:
                lct_dphi_all[st][0] = deltaPhi(tree0_lct_phi_all[st][0], tree1_lct_phi_all[st][0])
            else:
                lct_dphi_all[st][0] =  -9.0
            if tree0_simhits_phi_all[st][0] > -9.0 and tree1_simhits_phi_all[st][0] > -9.0:
                simhits_dphi_all[st][0] = deltaPhi(tree0_simhits_phi_all[st][0], tree1_simhits_phi_all[st][0])
            else:
                simhits_dphi_all[st][0] =  -9.0


    
    #newTree.Branch("deltatheta12",          deltatheta12);
    #newTree.Branch("deltatheta13",          deltatheta13);
    #newTree.Branch("deltatheta14",          deltatheta14);
    #newTree.Branch("deltatheta23",          deltatheta23);
    #newTree.Branch("deltatheta24",          deltatheta24);
    #newTree.Branch("deltatheta34",          deltatheta34);
    #newTree.Branch("lctslope1",             lctslope1);
    #newTree.Branch("lctslope2",             lctslope2);
    #newTree.Branch("lctslope3",             lctslope3);
    #newTree.Branch("lctslope4",             lctslope4);
    #newTree.Branch("lctpattern1",           lctpattern1);
    #newTree.Branch("lctpattern2",           lctpattern2);
    #newTree.Branch("lctpattern3",           lctpattern3);
    #newTree.Branch("lctpattern4",           lctpattern4);
    #newTree.Branch("quality",               quality);
    #newTree.Branch("tree0_mode",                  tree0_mode, "I");
    #newTree.Branch("tree0_deltaphi12",            tree0_deltaphi12, "I");
    #newTree.Branch("tree0_deltaphi13",            tree0_deltaphi13, "I");
    #newTree.Branch("tree0_deltaphi14",            tree0_deltaphi14, "I");
    #newTree.Branch("tree0_deltaphi23",            tree0_deltaphi23, "I");
    #newTree.Branch("tree0_deltaphi24",            tree0_deltaphi24, "I");
    #newTree.Branch("tree0_deltaphi34",            tree0_deltaphi34, "I");

    #newTree.Branch("tree0_cscstub_st1_matched",   tree0_cscstub_st1_matched, "I");
    #newTree.Branch("tree0_cscstub_st1_found",     tree0_cscstub_st1_found, "I");
    #newTree.Branch("tree0_cscstub_st1_wire",      tree0_cscstub_st1_wire);
    #newTree.Branch("tree0_cscstub_st1_halfstrip", tree0_cscstub_st1_halfstrip);
    #newTree.Branch("tree0_cscstub_st1_pattern",   tree0_cscstub_st1_pattern);
    #newTree.Branch("tree0_cscstub_st1_ring",      tree0_cscstub_st1_ring);
    #newTree.Branch("tree0_emtfhit_st1_wire",      tree0_emtfhit_st1_wire);
    #newTree.Branch("tree0_emtfhit_st1_halfstrip", tree0_emtfhit_st1_halfstrip);
    #newTree.Branch("tree0_emtfhit_st1_pattern",   tree0_emtfhit_st1_pattern);
    #newTree.Branch("tree0_emtfhit_st1_ring",      tree0_emtfhit_st1_ring);

    #newTree.Branch("tree0_cscstub_st2_matched",   tree0_cscstub_st2_matched);
    #newTree.Branch("tree0_cscstub_st2_found",     tree0_cscstub_st2_found);
    #newTree.Branch("tree0_cscstub_st2_wire",      tree0_cscstub_st2_wire);
    #newTree.Branch("tree0_cscstub_st2_halfstrip", tree0_cscstub_st2_halfstrip);
    #newTree.Branch("tree0_cscstub_st2_pattern",   tree0_cscstub_st2_pattern);
    #newTree.Branch("tree0_cscstub_st2_ring",      tree0_cscstub_st2_ring);
    #newTree.Branch("tree0_emtfhit_st2_wire",      tree0_emtfhit_st2_wire);
    #newTree.Branch("tree0_emtfhit_st2_halfstrip", tree0_emtfhit_st2_halfstrip);
    #newTree.Branch("tree0_emtfhit_st2_pattern",   tree0_emtfhit_st2_pattern);
    #newTree.Branch("tree0_emtfhit_st2_ring",      tree0_emtfhit_st2_ring);

    #newTree.Branch("tree0_cscstub_st3_matched",   tree0_cscstub_st3_matched);
    #newTree.Branch("tree0_cscstub_st3_found",     tree0_cscstub_st3_found);
    #newTree.Branch("tree0_cscstub_st3_wire",      tree0_cscstub_st3_wire);
    #newTree.Branch("tree0_cscstub_st3_halfstrip", tree0_cscstub_st3_halfstrip);
    #newTree.Branch("tree0_cscstub_st3_pattern",   tree0_cscstub_st3_pattern);
    #newTree.Branch("tree0_cscstub_st3_matched",   tree0_cscstub_st3_matched);
    #newTree.Branch("tree0_cscstub_st3_found",     tree0_cscstub_st3_found);
    #newTree.Branch("tree0_cscstub_st3_wire",      tree0_cscstub_st3_wire);
    #newTree.Branch("tree0_cscstub_st3_halfstrip", tree0_cscstub_st3_halfstrip);
    #newTree.Branch("tree0_cscstub_st3_pattern",   tree0_cscstub_st3_pattern);
    #newTree.Branch("tree0_cscstub_st3_ring",      tree0_cscstub_st3_ring);
    #newTree.Branch("tree0_emtfhit_st3_wire",      tree0_emtfhit_st3_wire);
    #newTree.Branch("tree0_emtfhit_st3_halfstrip", tree0_emtfhit_st3_halfstrip);
    #newTree.Branch("tree0_emtfhit_st3_pattern",   tree0_emtfhit_st3_pattern);
    #newTree.Branch("tree0_emtfhit_st3_ring",      tree0_emtfhit_st3_ring);

    #newTree.Branch("tree0_cscstub_st4_matched",   tree0_cscstub_st4_matched);
    #newTree.Branch("tree0_cscstub_st4_found",     tree0_cscstub_st4_found);
    #newTree.Branch("tree0_cscstub_st4_wire",      tree0_cscstub_st4_wire);
    #newTree.Branch("tree0_cscstub_st4_halfstrip", tree0_cscstub_st4_halfstrip);
    #newTree.Branch("tree0_cscstub_st4_pattern",   tree0_cscstub_st4_pattern);
    #newTree.Branch("tree0_cscstub_st4_ring",      tree0_cscstub_st4_ring);
    #newTree.Branch("tree0_emtfhit_st4_wire",      tree0_emtfhit_st4_wire);
    #newTree.Branch("tree0_emtfhit_st4_halfstrip", tree0_emtfhit_st4_halfstrip);
    #newTree.Branch("tree0_emtfhit_st4_pattern",   tree0_emtfhit_st4_pattern);
    #newTree.Branch("tree0_emtfhit_st4_ring",      tree0_emtfhit_st4_ring);

    #newTree.Branch("tree0_nstubs_matched_TF",     tree0_nstubs_matched_TF);
    #newTree.Branch("tree0_allstubs_matched_TF",   tree0_allstubs_matched_TF);

    newTree.Branch("tree0_ievent",   tree0_ievent, "I")
    newTree.Branch("tree0_gen_eta",  tree0_eta, "F")
    newTree.Branch("tree0_gen_phi",  tree0_phi, "F")
    newTree.Branch("tree0_gen_pt",   tree0_pt, "F")
    newTree.Branch("tree0_emtf_eta", tree0_emtf_eta, "F")
    newTree.Branch("tree0_emtf_phi", tree0_emtf_phi, "F")
    newTree.Branch("tree0_emtf_pt",  tree0_emtf_pt, "F")
    newTree.Branch("tree1_ievent",   tree1_ievent, "I")
    newTree.Branch("tree1_gen_eta",  tree1_eta, "F")
    newTree.Branch("tree1_gen_phi",  tree1_phi, "F")
    newTree.Branch("tree1_gen_pt",   tree1_pt, "F")
    newTree.Branch("tree1_emtf_eta", tree1_emtf_eta, "F")
    newTree.Branch("tree1_emtf_phi", tree1_emtf_phi, "F")
    newTree.Branch("tree1_emtf_pt",  tree1_emtf_pt, "F")

    newTree.Branch("tree0_emtf_hasME1",tree0_hasME1, "I");
    newTree.Branch("tree0_emtf_hasME2",tree0_hasME2, "I");
    newTree.Branch("tree0_emtf_hasME3",tree0_hasME3, "I");
    newTree.Branch("tree0_emtf_hasME4",tree0_hasME4, "I");
    newTree.Branch("tree0_emtf_nstubs",tree0_nstubs, "I");
    newTree.Branch("tree0_emtf_mode",  tree0_mode, "I");
    newTree.Branch("tree1_emtf_hasME1",tree1_hasME1, "I");
    newTree.Branch("tree1_emtf_hasME2",tree1_hasME2, "I");
    newTree.Branch("tree1_emtf_hasME3",tree1_hasME3, "I");
    newTree.Branch("tree1_emtf_hasME4",tree1_hasME4, "I");
    newTree.Branch("tree1_emtf_nstubs",tree1_nstubs, "I");
    newTree.Branch("tree1_emtf_mode",  tree1_mode, "I");

    newTree.Branch("emtfhit_nmismatch", emtfhit_nmismatch,'I')
    newTree.Branch("cscstub_nmismatch", cscstub_nmismatch,'I')
    newTree.Branch("simhits_nmismatch", simhits_nmismatch,'I')
    for st in range(0, 4):
        newTree.Branch("emtfhit_st%d_phidiff"%(st+1), emtfhit_st_phidiff[st],'F')
        newTree.Branch("cscstub_st%d_phidiff"%(st+1), cscstub_st_phidiff[st],'F')
        newTree.Branch("simhits_st%d_phidiff"%(st+1), simhits_st_phidiff[st],'F')
        newTree.Branch("emtfhit_st%d_match"%(st+1), emtfhit_st_match[st],'I')
        newTree.Branch("cscstub_st%d_match"%(st+1), cscstub_st_match[st],'I')
        newTree.Branch("simhits_st%d_match"%(st+1), simhits_st_match[st],'I')

        newTree.Branch("tree0_emtfhit_st%d_phi"%(st+1),       tree0_emtfhit_st_phi[st],'F')
        newTree.Branch("tree0_emtfhit_st%d_pattern"%(st+1),   tree0_emtfhit_st_pattern[st],'I')
        newTree.Branch("tree0_emtfhit_st%d_halfstrip"%(st+1), tree0_emtfhit_st_halfstrip[st],'F')
        newTree.Branch("tree0_cscstub_st%d_phi"%(st+1),       tree0_cscstub_st_phi[st],'F')
        newTree.Branch("tree0_cscstub_st%d_pattern"%(st+1),   tree0_cscstub_st_pattern[st],'I')
        newTree.Branch("tree0_cscstub_st%d_halfstrip"%(st+1), tree0_cscstub_st_halfstrip[st],'F')
        newTree.Branch("tree0_simhits_st%d_phi"%(st+1),       tree0_simhits_st_phi[st],'F')
        newTree.Branch("tree1_emtfhit_st%d_phi"%(st+1),       tree1_emtfhit_st_phi[st],'F')
        newTree.Branch("tree1_emtfhit_st%d_pattern"%(st+1),   tree1_emtfhit_st_pattern[st],'I')
        newTree.Branch("tree1_emtfhit_st%d_halfstrip"%(st+1), tree1_emtfhit_st_halfstrip[st],'F')
        newTree.Branch("tree1_cscstub_st%d_phi"%(st+1),       tree1_cscstub_st_phi[st],'F')
        newTree.Branch("tree1_cscstub_st%d_pattern"%(st+1),   tree1_cscstub_st_pattern[st],'I')
        newTree.Branch("tree1_cscstub_st%d_halfstrip"%(st+1), tree1_cscstub_st_halfstrip[st],'F')
        newTree.Branch("tree1_simhits_st%d_phi"%(st+1),       tree1_simhits_st_phi[st],'F')
    for st in range(0, len(cscStations)):
        newTree.Branch("tree0_simhits_phi_%s"%cscStations[st].labelc, tree0_simhits_phi_all[st],'F')
        newTree.Branch("tree0_lct_phi_%s"%cscStations[st].labelc,     tree0_lct_phi_all[st],'F')
        newTree.Branch("tree0_lct_pattern_%s"%cscStations[st].labelc, tree0_lct_pattern_all[st],'I')
        newTree.Branch("tree1_simhits_phi_%s"%cscStations[st].labelc, tree1_simhits_phi_all[st],'F')
        newTree.Branch("tree1_lct_phi_%s"%cscStations[st].labelc,     tree1_lct_phi_all[st],'F')
        newTree.Branch("tree1_lct_pattern_%s"%cscStations[st].labelc, tree1_lct_pattern_all[st],'I')
        newTree.Branch("lct_dphi_%s"%cscStations[st].labelc,     lct_dphi_all[st],'F')
        newTree.Branch("simhits_dphi_%s"%cscStations[st].labelc,     simhits_dphi_all[st],'F')
    phidiff_cut = 0.002
    for nEv in range(0, totalEntries0):
    #for nEv in range(0, 100):
        tree0.GetEntry(nEv)
        tree1.GetEntry(nEv)

        
        extractTree0()
        extractTree1()

        initBranches()
        
        for st in range(1,5):
          #if getattr(tree0, "emtfhit_st%d_ring"%st) == getattr(tree1, "emtfhit_st%d_ring"%st) and getattr(tree0, "emtfhit_st%d_wire"%st) == getattr(tree1, "emtfhit_st%d_wire"%st) and abs(getattr(tree0, "emtfhit_st%d_halfstrip"%st) - getattr(tree1, "emtfhit_st%d_halfstrip"%st) <= 1.0) and :
          if abs(deltaPhi(getattr(tree0, "emtfhit_st%d_phi"%st), getattr(tree1, "emtfhit_st%d_phi"%st))) <= phidiff_cut:
              emtfhit_st_match[st-1][0] = 1
          if getattr(tree0, "emtfhit_st%d_phi"%st)  > -9 and  getattr(tree1, "emtfhit_st%d_phi"%st) > -9:
              emtfhit_st_phidiff[st-1][0] = deltaPhi(getattr(tree0, "emtfhit_st%d_phi"%st), getattr(tree1, "emtfhit_st%d_phi"%st))
          #if getattr(tree0, "cscstub_st%d_ring"%st) == getattr(tree1, "cscstub_st%d_ring"%st) and getattr(tree0, "cscstub_st%d_wire"%st) == getattr(tree1, "cscstub_st%d_wire"%st) and abs(getattr(tree0, "cscstub_st%d_halfstrip"%st) - getattr(tree1, "cscstub_st%d_halfstrip"%st) <= 1.0) :
          if abs(deltaPhi(getattr(tree0, "cscstub_st%d_phi"%st), getattr(tree1, "cscstub_st%d_phi"%st))) <= phidiff_cut:
              cscstub_st_match[st-1][0] = 1
          if getattr(tree0, "cscstub_st%d_phi"%st)  > -9 and  getattr(tree1, "cscstub_st%d_phi"%st) > -9:
              cscstub_st_phidiff[st-1][0] = deltaPhi(getattr(tree0, "cscstub_st%d_phi"%st), getattr(tree1, "cscstub_st%d_phi"%st))
          if abs(getattr(tree0, "simhits_st%d_phi"%st) - getattr(tree1, "simhits_st%d_phi"%st)) <= phidiff_cut:
              simhits_st_match[st-1][0] = 1
          if getattr(tree0, "simhits_st%d_phi"%st)  > -9 and  getattr(tree1, "simhits_st%d_phi"%st) > -9:
              simhits_st_phidiff[st-1][0] = deltaPhi(getattr(tree0, "simhits_st%d_phi"%st), getattr(tree1, "simhits_st%d_phi"%st))

          emtfhit_nmismatch[0]  =emtfhit_nmismatch[0] + 1-emtfhit_st_match[st-1][0] 
          cscstub_nmismatch[0]  =cscstub_nmismatch[0] + 1-cscstub_st_match[st-1][0] 
          simhits_nmismatch[0]  =simhits_nmismatch[0] + 1-simhits_st_match[st-1][0] 

        newTree.Fill()

        continue
        st1_dphi_stub_sim0 = -9; st1_dphi_emtfhit_sim0 = -9
        st1_dphi_stub_sim1 = -9; st1_dphi_emtfhit_sim1 = -9
        if tree0.emtfhit_st1_phi > -9 and tree0.simhits_st1_phi > -9:
            st1_dphi_stub_sim0 = tree0.cscstub_st1_phi  - tree0.simhits_st1_phi 
            st1_dphi_emtfhit_sim0 = tree0.emtfhit_st1_phi  - tree0.simhits_st1_phi 
        if tree1.emtfhit_st1_phi > -9 and tree1.simhits_st1_phi > -9:
            st1_dphi_stub_sim1 = tree1.cscstub_st1_phi  - tree1.simhits_st1_phi 
            st1_dphi_emtfhit_sim1 = tree1.emtfhit_st1_phi  - tree1.simhits_st1_phi 

        #print("st1_dphi_emtfhit_sim0 ", st1_dphi_emtfhit_sim0, " st1_dphi_emtfhit_sim1 ", st1_dphi_emtfhit_sim1," diff ", abs(st1_dphi_emtfhit_sim1-st1_dphi_emtfhit_sim0))
        #if st1_dphi_emtfhit_sim1 > -9 and st1_dphi_emtfhit_sim0 > -9 and abs(st1_dphi_emtfhit_sim1-st1_dphi_emtfhit_sim0)>0.001:
        if tree0.emtf_pt >= 20 and tree1.emtf_pt < 20:
            print("------------------------------- Analyzing the event with different phi from CSC stub ------------------------------------")
            print("\t ========= Analyzer ", plotter0.analyzer, " =========")
            printEmtfTrack(tree0)
            if abs(tree0.eta)>1.65 and (tree0.has_lct_odd[0] or tree0.has_lct_even[0]):
                printCSCStubInSimtrack(tree0, 0)
            if abs(tree0.eta)>1.65 and (tree0.has_lct_odd[5] or tree0.has_lct_even[5]):
                printCSCStubInSimtrack(tree0, 5)
                
            print("\t ========= Analyzer ", plotter1.analyzer, " =========")
            printEmtfTrack(tree1)
            if abs(tree1.eta)>1.65 and (tree1.has_lct_odd[0] or tree1.has_lct_even[0]):
                printCSCStubInSimtrack(tree1, 0)
            if abs(tree1.eta)>1.65 and (tree1.has_lct_odd[5] or tree1.has_lct_even[5]):
                printCSCStubInSimtrack(tree1, 5)

    newTree.Write()
    f.Close()
    print("Done, analyzeTwoTrees")
