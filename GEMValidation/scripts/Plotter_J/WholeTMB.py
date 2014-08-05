import ROOT

c1 = ROOT.TCanvas()
c1.SetGridx()
c1.SetGridy()
c1.SetTickx()
c1.SetTicky()


tree = "GEMCSCAnalyzer/trk_eff_ME11"
den = "pt>10 && has_csc_sh>0"
den2= "pt>10"
num = "has_csc_sh>0 && has_lct>0 && pt>10"


f2 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_SLHC_eff.root")
t2 = f2.Get("GEMCSCAnalyzer/trk_eff_ME11")
e2 = ROOT.TH1F("e2","e2",40,1.5,2.5)
t2.Draw("eta >> e2",num)
eb = ROOT.TH1F("eb","eb",40,1.5,2.5)
t2.Draw("eta >> eb",den)
ec = ROOT.TH1F("ec","ec",40,1.5,2.5)
t2.Draw("eta >> ec",den2)

e2.SetLineColor(ROOT.kRed)
e2.SetLineWidth(2)
e2.SetLineStyle(1)

eb.SetLineColor(ROOT.kBlue)
eb.SetLineWidth(2)
eb.SetLineStyle(1)

ec.SetLineColor(ROOT.kOrange)
ec.SetLineWidth(4)

b1 = ROOT.TH1F("b1","b1",50,1.4,2.5)
b1.GetYaxis().SetRangeUser(0,2200)
b1.GetYaxis().SetTitleOffset(1.2)
b1.GetYaxis().SetNdivisions(520)
b1.GetYaxis().SetTitle("LCT reconstruction efficiency")
b1.GetXaxis().SetTitle("#eta of simulated muon track")
b1.SetTitle("Tree Based")
b1.SetStats(0)
eb.SetStats(0)
e2.SetStats(0)
ec.SetStats(0)
b1.Draw()
e2.Draw("same")
ec.Draw("same")
eb.Draw("same")



legend = ROOT.TLegend(0.27,0.13,0.72,0.42)
legend.SetFillColor(ROOT.kWhite)
#legend.SetBorderSize(0)
#legend.SetFillStyle(0)
legend.SetHeader("PU140 and 2<Pt<50")
legend.AddEntry(e2,"TMB SLHC num","l")
legend.AddEntry(eb,"TMB SLHC 2 den","l")
legend.AddEntry(ec,"TMB SLHC no csc_sh required","l")

legend.Draw("same")

c1.SaveAs("Num_Den_TreeSLHC.png")
