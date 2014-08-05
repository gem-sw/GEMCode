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


def TreeBasedPT():
    c1 = ROOT.TCanvas()
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()
    
    f2 = ROOT.TFile(file)
    t2 = f2.Get("GEMCSCAnalyzer/trk_eff_ME11")
    e2 = ROOT.TH1F("e2","e2",40,10,50)
    t2.Draw("pt >> e2",num)
    eb = ROOT.TH1F("eb","eb",40,10,50)
    t2.Draw("pt >> eb",den)

    e2.SetLineColor(ROOT.kRed)
    e2.SetLineWidth(2)
    e2.SetLineStyle(1)

    e2.SetLineWidth(3)
    eb.SetLineWidth(3)
    
    b1 = ROOT.TH1F("b1","b1",60,0,60)
    b1.GetYaxis().SetRangeUser(0,5000)
    b1.GetYaxis().SetTitleOffset(1.2)
    b1.GetYaxis().SetNdivisions()
    #b1.GetYaxis().SetTitle("LCT reconstruction efficiency")
    b1.GetXaxis().SetTitle("PT")
    b1.SetTitle("Tree Based PT" )
    b1.SetStats(0)
    b1.Draw()

    eb.Draw("same")
    #e2.Draw("same")

    legend = ROOT.TLegend(0.25,0.13,0.72,0.42)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetHeader("PU140 and 10<Pt<50")
    #legend.AddEntry(e2,"TMB Baseline 2: num","l")
    legend.AddEntry(eb,"TMB Baseline 2: den","l")
    legend.Draw("same")

    c1.SaveAs("Tree_Based_PT.png")

def TreeBasedETa():
    c1 = ROOT.TCanvas()
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()
    den = "pt>10"
    num = "has_lct>0 && pt>10"
    den2="has_csc_sh>0 && pt>10"
    num2 = "has_lct>0 && pt>10 && has_csc_sh>0"
    f2 = ROOT.TFile(file)
    t2 = f2.Get("GEMCSCAnalyzer/trk_eff_ME11")
    e2 = ROOT.TH1F("e2","e2",40,1.5,2.5)
    t2.Draw("eta >> e2",num)
    eb = ROOT.TH1F("eb","eb",40,1.5,2.5)
    t2.Draw("eta >> eb",den)
    ec = ROOT.TH1F("ec","ec",40,1.5,2.5)
    t2.Draw("eta >> ec",den2)
    ed = ROOT.TH1F("ed","ed",40,1.5,2.5)
    t2.Draw("eta >> ed",num2)
        
    e2.SetLineColor(ROOT.kRed)
    e2.SetLineWidth(4)
    e2.SetLineStyle(1)

    e2.SetLineWidth(3)
    eb.SetLineWidth(4)
    
    b1 = ROOT.TH1F("b1","b1",50,1.4,2.5)
    b1.GetYaxis().SetRangeUser(0,2500)
    b1.GetYaxis().SetTitleOffset(1.2)
    b1.GetYaxis().SetNdivisions()
    #b1.GetYaxis().SetTitle("LCT reconstruction efficiency")
    b1.GetXaxis().SetTitle("#eta of SimTrack muon")
    b1.SetTitle("Tree Based Eta" )
    b1.SetStats(0)
    b1.Draw()
    ec.SetLineColor(ROOT.kGreen+2)
    ec.SetLineWidth(3)
    ed.SetLineColor(ROOT.kOrange)
    ed.SetLineWidth(3)
    eb.Draw("same")
    e2.Draw("same")
    ec.Draw("same")
    ed.Draw("same")

    legend = ROOT.TLegend(0.25,0.13,0.72,0.42)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetHeader("PU140 and 10<Pt<50")
    legend.AddEntry(e2,"TMB Baseline 2: num, no csc_sh reqired","l")
    legend.AddEntry(ed,"TMB Baseline 2: num, 4 simhits required","l")
    legend.AddEntry(eb,"TMB Baseline 2: den, no csc sh required","l")
    legend.AddEntry(ec,"TMB Baseline 2: den, 4 simhits required","l")
    legend.Draw("same")

    c1.SaveAs("Tree_Based_Eta.png")

def HistBasedEta():
    input_dir=""
    d1 = getRootDirectory(input_dir, f1)
    etareb = 1
    yrange = [0,2500]
    xrange = [1.4,2.5]    
    xTitle = "Sim track #eta"
    yTitle = "Number of Samples"
    topTitle = "Hist. Based eta"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

    h1 = setEffHisto2("h_eta_me1_after_lct_okAlctClct","h_eta_me1_initial",d1, etareb, ROOT.kRed+1, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)
    h7 = setEffHisto2("h_eta_me1_initial","h_eta_me1_after_lct_okAlctClct",d1, etareb, ROOT.kBlue, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)

    c = ROOT.TCanvas("h_eta_me1_after_lct_okAlctClct","h_eta_me1_initial",1000,600 )     
    c.cd()
    c.SetGridx()
    c.SetGridy()
    c.SetTickx()
    c.SetTicky()
    h1.SetStats(0)
    h7.SetStats(0)
    h1.Draw("hist")
    h7.Draw("same hist")

    leg = ROOT.TLegend(0.18,0.18,0.78,0.44,"","brNDC")
    leg.SetMargin(0.15)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.AddEntry(h1,"TMB Baseline 2 PU140 num","l")
    leg.AddEntry(h7,"TMB Baseline 2 PU140 den","l")
    leg.Draw()
    #tex = drawPULabel()
    c.SaveAs("Hist_Based_Eta.png")

def HistBasedPT():
    input_dir=""
    d1 = getRootDirectory(input_dir, f1)
    etareb = 1
    yrange = [0,5000]
    xrange = [0,50]    
    xTitle = "Sim track #eta"
    yTitle = "Number of Samples"
    topTitle = "Number of Samples, eta"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

    h1 = setEffHisto2("h_pt_me1_initial","h_pt_initial0",d1, etareb, ROOT.kRed+1, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)
    h7 = setEffHisto2("h_pt_initial0","h_pt_me1_initial",d1, etareb, ROOT.kBlue, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)

    c = ROOT.TCanvas("h_pt_me1_initial","h_pt_me1_initial",1000,600 )     
    c.cd()
    c.SetGridx()
    c.SetGridy()
    c.SetTickx()
    c.SetTicky()
    b1 = ROOT.TH1F("b1","b1",40,0,60)
    b1.GetYaxis().SetRangeUser(0,5000)
    b1.GetYaxis().SetTitleOffset(1.2)
    b1.GetYaxis().SetNdivisions()
    #b1.GetYaxis().SetTitle("LCT reconstruction efficiency")
    b1.GetXaxis().SetTitle("#eta of SimTrack muon")
    b1.SetTitle("Hist Based PT" )
    b1.SetStats(0)
    b1.Draw()
    h7.Draw("same hist")

    leg = ROOT.TLegend(0.18,0.18,0.88,0.58,"","brNDC")
    leg.SetMargin(0.15)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.AddEntry(h7,"TMB Baseline 2 PU140 den","l")
    leg.Draw()
    #tex = drawPULabel()
    c.SaveAs("Hist_Based_PT.png")

def ComparisonPT():
    den = "pt>10"
    den2 = "has_csc_sh>0 && pt>10"
    num = "has_lct>0 && pt>10"
    input_dir=""
    d1 = getRootDirectory(input_dir, f1)
    etareb = 1
    yrange = [0,5000]
    xrange = [0,50]    
    xTitle = "Sim track #eta"
    yTitle = "Number of Samples"
    topTitle = "Number of Samples, eta"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

    h1 = setEffHisto2("h_pt_me1_initial","h_pt_initial0",d1, etareb, ROOT.kRed+1, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)
    h7 = setEffHisto2("h_pt_initial0","h_pt_me1_initial",d1, etareb, ROOT.kBlue, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)

    c1 = ROOT.TCanvas()
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()
    
    f2 = ROOT.TFile(file)
    t2 = f2.Get("GEMCSCAnalyzer/trk_eff_ME11")
    e2 = ROOT.TH1F("e2","e2",40,10,50)
    t2.Draw("pt >> e2",num)
    eb = ROOT.TH1F("eb","eb",40,10,50)
    t2.Draw("pt >> eb",den)
    ec = ROOT.TH1F("ec","ec",40,10,50)
    t2.Draw("pt >> ec",den2)

    eb.SetLineColor(ROOT.kRed)
    eb.SetLineWidth(6)
    eb.SetLineStyle(1)

    ec.SetLineColor(ROOT.kGreen+2)
    ec.SetLineWidth(5)
    b1 = ROOT.TH1F("b1","b1",60,0,60)
    b1.GetYaxis().SetRangeUser(0,5000)
    b1.GetYaxis().SetTitleOffset(1.2)
    b1.GetYaxis().SetNdivisions()
    #b1.GetYaxis().SetTitle("LCT reconstruction efficiency")
    b1.GetXaxis().SetTitle("PT")
    b1.SetTitle("Comparison PT" )
    b1.SetStats(0)
    b1.Draw()
    eb.Draw("same")
    h7.Draw("same hist")
    ec.Draw("same")

    #e2.Draw("same")

    legend = ROOT.TLegend(0.25,0.13,0.72,0.42)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetHeader("PU140 and 10<Pt<50")
    legend.AddEntry(h7,"Histogram Based denominator","l")
    legend.AddEntry(eb,"Tree Based denominator, no csc_sh required","l")
    legend.AddEntry(ec,"Tree Based denominator, csc_sh required","l")
    legend.Draw("same")

    c1.SaveAs("Comparison_PT.png")
#### Main 

f1="hp_dimu_CMSSW_6_2_0_SLHC7_upgrade2019_w3PU140_TMB_Baseline_2_eff.root"
file= "hp_CMSSW14_usingL1SLHC7_PU140_TMB_Baseline_2_eff.root"

tree = "GEMCSCAnalyzer/trk_eff_ME11"
den = "pt>10"
num = "has_lct>0 && pt>10"

TreeBasedPT()
TreeBasedETa()
HistBasedEta()
HistBasedPT()
ComparisonPT()
