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
    #heff.Divide(heff,hd)
    heff.SetLineColor(lcolor)
    heff.SetLineStyle(lstyle)
    heff.SetMarkerColor(mcolor)
    heff.SetLineWidth(lwidth)

    return heff


def setEffHisto3(num_name, den_name, dir, nrebin, lcolor, lstyle, lwidth, mcolor, mstyle,
                htitle, xtitle, ytitle, x_range, y_range):
    hd = getH(dir, den_name)
    hn = getH(dir, num_name)
    hd.Sumw2()
    hn.Sumw2()
    myRebin(hd, nrebin)
    myRebin(hn, nrebin)
    heff = hd.Clone(num_name+"_eff")
    hd.Sumw2()
    heff.Sumw2()
    #heff.Divide(heff,hd)
    heff.SetLineColor(lcolor)
    heff.SetLineStyle(lstyle)
    heff.SetMarkerColor(mcolor)
    heff.SetLineWidth(lwidth)

    return heff

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
f2a = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_matchTrigWindowSize_eff.root"
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

tree = "GEMCSCAnalyzer/trk_eff_ME11"
den = "pt>10 && has_csc_sh>0"
den2= "pt>10"
num = "has_csc_sh>0 && has_lct>0 && pt>10"
num2 = "has_lct>0 && pt>10"

f2 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_TMB_Baseline_2_eff.root")
t2 = f2.Get("GEMCSCAnalyzer/trk_eff_ME11")
e2 = ROOT.TH1F("e2","e2",40,1.5,2.5)
t2.Draw("eta >> e2",num)
eb = ROOT.TH1F("eb","eb",40,1.5,2.5)
t2.Draw("eta >> eb",den)
ec = ROOT.TH1F("ec","ec",40,1.5,2.5)
t2.Draw("eta >> ec",den2)
e3 = ROOT.TH1F("e3","e3",40,1.5,2.5)
t2.Draw("eta >> e3",num2)

e2.SetLineColor(ROOT.kGreen+2)
e2.SetLineWidth(4)
e2.SetLineStyle(1)

eb.SetLineColor(ROOT.kGreen+2)
eb.SetLineWidth(2)
eb.SetLineStyle(1)

ec.SetLineColor(ROOT.kOrange)
ec.SetLineWidth(2)

e3.SetLineColor(ROOT.kBlack)
e3.SetLineWidth(2)

input_dir=""
d0 = getRootDirectory(input_dir, f0) 
d1 = getRootDirectory(input_dir, f1)
d2 = getRootDirectory(input_dir, f2a)
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

h0 = setEffHisto2("h_eta_me1_after_lct_okAlctClct","h_eta_me1_initial",d1, etareb, ROOT.kBlack, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)
h1 = setEffHisto2("h_eta_me11_after_lct_okAlctClct","h_eta_me11_initial",d1, etareb, ROOT.kRed, 1, 2, ROOT.kBlue, 4, topTitle,xTitle,yTitle,xrange,yrange)
ha = setEffHisto3("h_eta_me1_after_lct_okAlctClct","h_eta_me1_initial",d1, etareb, ROOT.kBlue, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)

var="Numerator"

b1 = ROOT.TH1F("b1","b1",40,1.4,2.5)
b1.GetYaxis().SetRangeUser(0.5,2200)
b1.GetYaxis().SetTitleOffset(1.2)
b1.GetYaxis().SetNdivisions(520)
b1.GetYaxis().SetTitle("LCT reconstruction efficiency")
b1.GetXaxis().SetTitle("#eta of simulated muon track")
b1.SetTitle("PU140" + " "*22 + "SLHC "+var)
b1.SetStats(0)
b1.Draw()

etamin=1.65
etamax=2.375
xmin=0
xmax=40
jkl=0
ppp=0 
for x in range(xmin, xmax):
    jkl = jkl+e2.GetBinContent(e2.FindBin(etamin+(etamax-etamin)*x/40))
    ppp = ppp+h1.GetBinContent(h1.FindBin(etamin+(etamax-etamin)*x/40))

print jkl
print ppp
    
ha.SetLineWidth(4)

b1.SetStats(0)
eb.SetStats(0)
e2.SetStats(0)
ec.SetStats(0)
e3.SetStats(0)
#Change Between 1 to 9 to use the different histograms and legends

if var=="Numerator":
    h1.Draw("same hist")
    e2.Draw("same")
    e3.Draw("same")
else:
    ha.Draw("same hist")
    ec.Draw("same")
    eb.Draw("same")

legend = ROOT.TLegend(0.25,0.16,0.82,0.38)
legend.SetFillColor(ROOT.kWhite)
legend.SetHeader(var+" Definition")
if var=="Numerator":
    legend.AddEntry(h1,"Histogram Based","l")

    legend.AddEntry(e2,"Tree Based","l")
    legend.AddEntry(e3,"Tree Based: no minimum # hits required","l")
else:
    legend.AddEntry(ha,"Histogram Based","l")
    legend.AddEntry(eb,"Tree Based","l")
    legend.AddEntry(ec,"Tree Based: no minimun # hits required","l")

legend.Draw("same")




c1.SaveAs("sdafdasfad"+var+"_SLHC.png")
