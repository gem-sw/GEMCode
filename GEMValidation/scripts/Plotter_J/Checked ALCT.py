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

t1="TMB Baseline 1"
t2="alctGhostCancellationBxDepth: 4BX to 1BX"
t3="alctGhostCancellationSideQuality: False to True"
t4="alctNarrowMaskForR1: False to True"
t5="alctPretrigDeadtime: 4BX to 0BX"
t6="TMB Baseline 2"

f1 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_TMB_Baseline_1_eff.root"
f2 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_alctGhostCancellationBxDepth_eff.root"
f3 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_alctGhostCancellationSideQuality_eff.root"
f4 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_alctNarrowMaskForR1_eff.root"
f5 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_alctPretrigDeadtime_eff.root"
f6 = "hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_TMB_Baseline_2_eff.root"

c1 = ROOT.TCanvas()
c1.SetGridx()
c1.SetGridy()
c1.SetTickx()
c1.SetTicky()

input_dir=""

d1 = getRootDirectory(input_dir, f1)
d2 = getRootDirectory(input_dir, f2)
d3 = getRootDirectory(input_dir, f3)
d4 = getRootDirectory(input_dir, f4)
d5 = getRootDirectory(input_dir, f5)
d6 = getRootDirectory(input_dir, f6)
etareb=1

yrange = [0.8,1.02]
xrange = [1.5,2.5]    
xTitle = "Sim track #eta"
yTitle = "Efficiency"
topTitle = "" 

h1 = setEffHisto2("h_eta_me1_after_alct_okAlct","h_eta_me1_initial",d1, etareb, ROOT.kRed+1, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)
h2 = setEffHisto2("h_eta_me1_after_alct_okAlct","h_eta_me1_initial",d2, etareb, ROOT.kBlue+1, 1, 2, ROOT.kGreen+2, 4, topTitle,xTitle,yTitle,xrange,yrange)
h3 = setEffHisto2("h_eta_me1_after_alct_okAlct","h_eta_me1_initial",d3, etareb, ROOT.kBlue+1, 1, 2, ROOT.kGreen+2, 20, topTitle,xTitle,yTitle,xrange,yrange)
h4 = setEffHisto2("h_eta_me1_after_alct_okAlct","h_eta_me1_initial",d4, etareb, ROOT.kBlue+1, 1, 2, ROOT.kGreen+2, 21, topTitle,xTitle,yTitle,xrange,yrange)
h5 = setEffHisto2("h_eta_me1_after_alct_okAlct","h_eta_me1_initial",d5, etareb, ROOT.kBlue+1, 1, 2, ROOT.kGreen+2, 22, topTitle,xTitle,yTitle,xrange,yrange)
h6 = setEffHisto2("h_eta_me1_after_alct_okAlct","h_eta_me1_initial",d6, etareb, ROOT.kBlue+1, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)

b1 = ROOT.TH1F("b1","b1",40,1.4,2.5)
b1.GetYaxis().SetRangeUser(0.8,1.01)
b1.GetYaxis().SetTitleOffset(1.2)
b1.GetYaxis().SetNdivisions(520)
b1.GetYaxis().SetTitle("ALCT reconstruction efficiency")
b1.GetXaxis().SetTitle("#eta of simulated muon track")
b1.SetTitle("PU140" + " "*22 + "SimHit Bug + Layers (ME1a + ME1b) > 4")
b1.SetStats(0)

treename = "GEMCSCAnalyzer/trk_eff_ME11"
den = "pt>10"
num = "pt>10 && has_csc_sh>0 && has_alct>0"


e1 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_TMB_Baseline_1_eff.root",treename,den,num)
e2 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_alctGhostCancellationBxDepth_eff.root",treename,den,num)
e3 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_alctGhostCancellationSideQuality_eff.root",treename,den,num)
e4 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_alctNarrowMaskForR1_eff.root",treename,den,num)
e5 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_alctPretrigDeadtime_eff.root",treename,den,num)
e6 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_TMB_Baseline_2_eff.root",treename,den,num)


#Change the numbers for different histogram. Also change the title 
t=t6
m=e6
n=h6
m.SetLineColor(ROOT.kOrange)
m.SetFillColor(ROOT.kOrange)
m.SetLineWidth(2)

b1.Draw()
m.Draw("same e3")

if (n==h1 or n==h6):
    oo="l"
    n.Draw("same hist")
else:
   oo="p"
   n.Draw("same hist P")

legend = ROOT.TLegend(0.23,0.16,0.82,0.38)
legend.SetFillColor(ROOT.kWhite)
legend.SetHeader(t)
legend.AddEntry(m,"Tree Based Analyzer","l")
legend.AddEntry(n,"Histogram Based Analyzer",oo)

legend.Draw("same")
ext=".png"

c1.SaveAs("ALCT_%s.%s"%(t,ext))
