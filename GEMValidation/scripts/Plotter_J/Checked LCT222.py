import ROOT
import sys

#_______________________________________________________________________________
def getRootDirectory(input_dir2, file_name2, dir2_name = "GEMCSCTriggerEfficiency"):
    """Get the ROOT directory from the GEMCSCTriggerEfficiency analyzer. Normally,
    the directory should be called GEMCSCTriggerEfficiency. You should check it anyway"""

    ### get the ROOT file
    file = ROOT.TFile.Open(input_dir2 + file_name2)
    if not file:
        sys.exit('Input ROOT file %s is missing.' %(file_name2))

    ## get the ROOT directory
    dir = file.Get(dir2_name)
    if not dir:
        sys.exit('Directory %s does not exist.' %(dir2_name))

    return dir

#_______________________________________________________________________________
def getH(dir, histo_name):
  """Get the histogram from a directory"""
  histo = dir.Get("%s;1"%(histo_name))
  if not histo:
    print "No such histogram: ", histo_name
  return histo

#_______________________________________________________________________________
def myRebin(h, n):
  """Custom rebin function"""
  nb = h.GetNbinsX()
  entr = h.GetEntries()
  bin0 = h.GetBinContent(0)
  binN1 = h.GetBinContent(nb+1)
  if (nb % n):
    binN1 += h.Integral(nb - nb%n + 1, nb)
  h.Rebin(n)
  nb = h.GetNbinsX()
  h.SetBinContent(0, bin0)
  h.SetBinContent(nb+1, binN1)
  h.SetEntries(entr)

#______________________________________________________________________________

def setEffHisto2(num_name, den_name, dir, nrebin, lcolor, lstyle, lwidth, mcolor, mstyle,
                htitle, xtitle, ytitle, x_range, y_range):
    hd = getH(dir, den_name)
    hn = getH(dir, num_name)
    hd.Sumw2()
    hn.Sumw2()
    myRebin(hd, nrebin)
    myRebin(hn, nrebin)
    heff = hn.Clone(num_name+"_eff")
    hd.Sumw2()
    heff.Sumw2()
    heff.Divide(heff,hd)
    heff.SetLineColor(lcolor)
    heff.SetLineStyle(lstyle)
    heff.SetMarkerColor(mcolor)
    heff.SetMarkerStyle(mstyle)
    heff.SetLineWidth(lwidth)
    heff.SetTitle(htitle)
    heff.GetXaxis().SetTitle(xtitle)
    heff.GetYaxis().SetTitle(ytitle)
    heff.GetXaxis().SetRangeUser(x_range[0],x_range[1])
    heff.GetYaxis().SetRangeUser(y_range[0],y_range[1])
    heff.GetXaxis().SetTitleSize(0.05)
    heff.GetXaxis().SetTitleOffset(1.)
    heff.GetYaxis().SetTitleSize(0.05)
    heff.GetYaxis().SetTitleOffset(1.)
    heff.GetXaxis().SetLabelOffset(0.015)
    heff.GetYaxis().SetLabelOffset(0.015)
    heff.GetXaxis().SetLabelSize(0.05)
    heff.GetYaxis().SetLabelSize(0.05)
    return heff

#_____________________________________________________________________________________
def getEff(file,dir,den,num):
    f = ROOT.TFile(file)
    t = f.Get(dir)
    h1 = ROOT.TH1F("h1","h1",40,1.5,2.5)
    t.Draw("eta >> h1",den)
    h2 = ROOT.TH1F("h2","h2",40,1.5,2.5)
    t.Draw("eta >> h2",num)
    e = ROOT.TEfficiency(h2,h1)
    return e

##################3 End of functions set up #################

t0 = "TMB Baseline 1"
t1 = "TMB Baseline 2"
t2 = "matchTrigWindowSize: 7BX to 3BX"
t3 = "alctUseCorrectedBx: False to True"
t4 = "clctUseCorrectedBx: False to True"
t5 = "clctToAlct: True to False"
t6 = "tmbDropUsedClcts_matchEarliestClctME11Only: True to False"
t7 = "tmbCrossBxAlgorithm: 0 to 1"
t8 = "tmbReadoutEarliest2: True to False"
t9 = "TMB SLHC"

f0 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_TMB_Baseline_1_eff.root"
f1 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_TMB_Baseline_2_eff.root"
f2 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_matchTrigWindowSize_eff.root"
f3 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_alctUseCorrectedBx_eff.root"
f4 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_clctUseCorrectedBx_eff.root"
f5 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_clctToAlct_eff.root"
f6 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_tmbDropUsedClcts_matchEarliestClctME11Only_eff.root"
f7 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_tmbCrossBxAlgorithm_eff.root"
f8 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_tmbReadoutEarliest2_eff.root"
f9 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_SLHC_eff.root"

c1 = ROOT.TCanvas()
c1.SetGridx()
c1.SetGridy()
c1.SetTickx()
c1.SetTicky()

input_dir=""
d0 = getRootDirectory(input_dir, f0) 
d1 = getRootDirectory(input_dir, f1) 
d2 = getRootDirectory(input_dir, f2) 
d3 = getRootDirectory(input_dir, f3) 
d4 = getRootDirectory(input_dir, f4) 
d5 = getRootDirectory(input_dir, f5) 
d6 = getRootDirectory(input_dir, f6) 
d7 = getRootDirectory(input_dir, f7) 
d8 = getRootDirectory(input_dir, f8) 
d9 = getRootDirectory(input_dir, f9)

etareb=1
yrange = [0.5,1.02]
xrange = [1.5,2.5]    
xTitle = "Sim track #eta"
yTitle = "Efficiency"
topTitle = " "

h0 = setEffHisto2("h_eta_me1_after_lct_okAlctClct","h_eta_me1_initial",d0, etareb, ROOT.kBlack, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)
h1 = setEffHisto2("h_eta_me1_after_lct_okClctAlct","h_eta_me1_initial",d1, etareb, ROOT.kRed+1, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)
h2 = setEffHisto2("h_eta_me1_after_lct_okAlctClct","h_eta_me1_initial",d2, etareb, ROOT.kGreen+2, 1, 2, ROOT.kGreen+2, 4, topTitle,xTitle,yTitle,xrange,yrange)
h3 = setEffHisto2("h_eta_me1_after_lct_okAlctClct","h_eta_me1_initial",d3, etareb, ROOT.kGreen+2, 1, 2, ROOT.kGreen+2, 21, topTitle,xTitle,yTitle,xrange,yrange)
h4 = setEffHisto2("h_eta_me1_after_lct_okAlctClct","h_eta_me1_initial",d4, etareb, ROOT.kGreen+2, 1, 2, ROOT.kGreen+2, 22, topTitle,xTitle,yTitle,xrange,yrange)
h5 = setEffHisto2("h_eta_me1_after_lct_okAlctClct","h_eta_me1_initial",d5, etareb, ROOT.kGreen+2, 1, 2, ROOT.kGreen+2, 23, topTitle,xTitle,yTitle,xrange,yrange)
h6 = setEffHisto2("h_eta_me1_after_lct_okAlctClct","h_eta_me1_initial",d6, etareb, ROOT.kGreen+2, 1, 2, ROOT.kGreen+2, 25, topTitle,xTitle,yTitle,xrange,yrange)
h7 = setEffHisto2("h_eta_me1_after_lct_okAlctClct","h_eta_me1_initial",d7, etareb, ROOT.kGreen+2, 1, 2, ROOT.kGreen+2, 26, topTitle,xTitle,yTitle,xrange,yrange)
h8 = setEffHisto2("h_eta_me1_after_lct_okAlctClct","h_eta_me1_initial",d8, etareb, ROOT.kGreen+2, 1, 2, ROOT.kGreen+2, 20, topTitle,xTitle,yTitle,xrange,yrange)
h9 = setEffHisto2("h_eta_me1_after_lct_okAlctClct","h_eta_me1_initial",d9, etareb, ROOT.kBlue+1, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)

b1 = ROOT.TH1F("b1","b1",40,1.4,2.5)
b1.GetYaxis().SetRangeUser(0.5,1.02)
b1.GetYaxis().SetTitleOffset(1.2)
b1.GetYaxis().SetNdivisions(520)
b1.GetYaxis().SetTitle("LCT reconstruction efficiency")
b1.GetXaxis().SetTitle("#eta of simulated muon track")
b1.SetTitle("PU140" + " "*22 + "Comparison between Analyzers on SLHC14")
b1.SetStats(0)

treename = "GEMCSCAnalyzer/trk_eff_ME11"
den = "pt>10 && has_csc_sh>0"
num = "has_csc_sh>0 && has_lct>0 && pt>10"

e0 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_TMB_Baseline_1_eff.root",treename,den,num)
e1 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_TMB_Baseline_2_eff.root",treename,den,num)
e2 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_matchTrigWindowSize_eff.root",treename,den,num)
e3 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_alctUseCorrectedBx_eff.root",treename,den,num)
e4 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_clctUseCorrectedBx_eff.root",treename,den,num)
e5 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_clctToAlct_eff.root",treename,den,num)
e6 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_tmbDropUsedClcts_matchEarliestClctME11Only_eff.root",treename,den,num)
e7 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_tmbCrossBxAlgorithm_eff.root",treename,den,num)
e8 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_tmbReadoutEarliest2_eff.root",treename,den,num)
e9 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_SLHC_eff.root",treename,den,num)

#Change Between 1 to 9 to use the different histograms and legends
op=t1
m=e1
n=h1

m.SetLineColor(ROOT.kOrange)
m.SetFillColor(ROOT.kOrange)
m.SetLineWidth(2)

b1.Draw()
m.Draw("same e3")
if (n==h1 or n==h9 or n==h0):
    oo="l"
    n.Draw("same hist")
else:
   oo="p"
   n.Draw("same hist P")

legend = ROOT.TLegend(0.23,0.16,0.82,0.38)
legend.SetFillColor(ROOT.kWhite)
legend.SetHeader(op)
legend.AddEntry(m,"Tree Based Analyzer","l")
legend.AddEntry(n,"Histogram Based Analyzer",oo)

legend.Draw("same")

ext=".png"

c1.SaveAs("LCTA_%s.%s"%(op,ext))
