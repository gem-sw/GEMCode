import ROOT

c1 = ROOT.TCanvas()
c1.SetGridx()
c1.SetGridy()
c1.SetTickx()
c1.SetTicky()


tree = "GEMCSCAnalyzer/trk_eff_ME11"
den = "pt>10"
num = "pt>10 && has_csc_sh>0 && has_clct>0"

f2 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_TMB_Baseline_1_eff.root")
t2 = f2.Get("GEMCSCAnalyzer/trk_eff_ME11")
e2 = ROOT.TH1F("e2","e2",40,1.5,2.5)
t2.Draw("eta >> e2",num)
eb = ROOT.TH1F("eb","eb",40,1.5,2.5)
t2.Draw("eta >> eb",den)
e2.Divide(eb)


f3 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_useDeadTimeZoning_eff.root")
t3 = f3.Get("GEMCSCAnalyzer/trk_eff_ME11")
e3 = ROOT.TH1F("e3","e3",40,1.5,2.5)
t3.Draw("eta >> e3",num)
ec = ROOT.TH1F("ec","ec",40,1.5,2.5)
t3.Draw("eta >> ec",den)
e3.Divide(ec)

f4 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_useDynamicStateMachineZone_eff.root")
t4 = f4.Get("GEMCSCAnalyzer/trk_eff_ME11")
e4 = ROOT.TH1F("e4","e4",40,1.5,2.5)
t4.Draw("eta >> e4",num)
ed = ROOT.TH1F("ed","ed",40,1.5,2.5)
t4.Draw("eta >> ed",den)
e4.Divide(ed)


f5 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_clctPidThreshPretrig_eff.root")
t5 = f5.Get("GEMCSCAnalyzer/trk_eff_ME11")
e5 = ROOT.TH1F("e5","e5",40,1.5,2.5)
t5.Draw("eta >> e5",num)
ee = ROOT.TH1F("ee","ee",40,1.5,2.5)
t5.Draw("eta >> ee",den)
e5.Divide(ee)

f6 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_clctMinSeparation_eff.root")
t6 = f6.Get("GEMCSCAnalyzer/trk_eff_ME11")
e6 = ROOT.TH1F("e6","e6",40,1.5,2.5)
t6.Draw("eta >> e6",num)
ef = ROOT.TH1F("ef","ef",40,1.5,2.5)
t6.Draw("eta >> ef",den)
e6.Divide(ef)


f7 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_TMB_Baseline_2_eff.root")
t7 = f7.Get("GEMCSCAnalyzer/trk_eff_ME11")
e7 = ROOT.TH1F("e7","e7",40,1.5,2.5)
t7.Draw("eta >> e7",num)
eg = ROOT.TH1F("eg","eg",40,1.5,2.5)
t7.Draw("eta >> eg",den)
e7.Divide(eg)



e2.SetLineColor(ROOT.kRed)
e2.SetLineWidth(2)
e2.SetLineStyle(2)
e2.SetStats(0)
e3.SetLineColor(ROOT.kGreen+2)
e3.SetLineWidth(2)
e3.SetMarkerStyle(4)
e3.SetMarkerColor(ROOT.kGreen+2)
e3.SetStats(0)
e4.SetLineColor(ROOT.kYellow)
e4.SetLineWidth(2)
e4.SetMarkerStyle(20)
e4.SetMarkerColor(ROOT.kGreen+2)
e4.SetStats(0)
e5.SetLineColor(ROOT.kViolet-2)
e5.SetLineWidth(4)
e5.SetMarkerStyle(21)
e5.SetMarkerColor(ROOT.kGreen+2)
e5.SetStats(0)
e6.SetLineColor(ROOT.kYellow-1)
e6.SetLineWidth(2)
e6.SetMarkerStyle(22)
e6.SetMarkerColor(ROOT.kGreen+2)
e6.SetStats(0)
e7.SetLineColor(ROOT.kBlue)
e7.SetLineWidth(2)
e7.SetLineStyle(2)
e7.SetMarkerStyle(25)
e7.SetMarkerColor(ROOT.kGreen+2)
e7.SetStats(0)
b1 = ROOT.TH1F("b1","b1",50,1.4,2.5)
b1.GetYaxis().SetRangeUser(0.5,1.02)
b1.GetYaxis().SetTitleOffset(1.2)
b1.GetYaxis().SetNdivisions(520)
b1.GetYaxis().SetTitle("CLCT reconstruction efficiency")
b1.GetXaxis().SetTitle("#eta of simulated muon track")
b1.SetTitle(" "*64 + "CMS Simulation Preliminary")
b1.SetStats(0)

b1.Draw()
e2.Draw("same")
e3.Draw("same P")
e4.Draw("same P")
e5.Draw("same P")
e6.Draw("same p")
e7.Draw("same")


legend = ROOT.TLegend(0.25,0.13,0.75,0.48)
legend.SetFillColor(ROOT.kWhite)
legend.SetHeader("PU140 and 2<pT<50")
legend.AddEntry(e2,"TMB Baseline 1","l")
legend.AddEntry(e3,"useDeadTimeZoning: False to True","p")
legend.AddEntry(e4,"useDynamicStateMachineZone: False to True","p")
legend.AddEntry(e5,"clctPidThreshPretrig: 2 to 4","p")
legend.AddEntry(e6,"clctMinSeparation: 10 to 5","p")
legend.AddEntry(e7,"TMB Baseline 2","l")
legend.Draw("same")

c1.SaveAs("Whole3CLCT.png")