import ROOT

c1 = ROOT.TCanvas()
c1.SetGridx()
c1.SetGridy()
c1.SetTickx()
c1.SetTicky()


tree = "GEMCSCAnalyzer/trk_eff_ME11"
den = "pt>10"
num = "has_csc_sh>0 && has_lct>0 && pt>10"
'''
f1 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_TMB_Baseline_1_eff.root")
t1 = f1.Get("GEMCSCAnalyzer/trk_eff_ME11")
e1 = ROOT.TH1F("e1","e1",40,1.5,2.5)
t1.Draw("eta >> e1",num)
ea = ROOT.TH1F("ea","ea",40,1.5,2.5)
t1.Draw("eta >> ea",den)
e1.Divide(ea)
'''

f2 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_TMB_Baseline_2_eff.root")
t2 = f2.Get("GEMCSCAnalyzer/trk_eff_ME11")
e2 = ROOT.TH1F("e2","e2",40,1.5,2.5)
t2.Draw("eta >> e2",num)
eb = ROOT.TH1F("eb","eb",40,1.5,2.5)
t2.Draw("eta >> eb",den)
e2.Divide(eb)


f3 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_matchTrigWindowSize_eff.root")
t3 = f3.Get("GEMCSCAnalyzer/trk_eff_ME11")
e3 = ROOT.TH1F("e3","e3",40,1.5,2.5)
t3.Draw("eta >> e3",num)
ec = ROOT.TH1F("ec","ec",40,1.5,2.5)
t3.Draw("eta >> ec",den)
e3.Divide(ec)

f4 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_alctUseCorrectedBx_eff.root")
t4 = f4.Get("GEMCSCAnalyzer/trk_eff_ME11")
e4 = ROOT.TH1F("e4","e4",40,1.5,2.5)
t4.Draw("eta >> e4",num)
ed = ROOT.TH1F("ed","ed",40,1.5,2.5)
t4.Draw("eta >> ed",den)
e4.Divide(ed)


f5 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_clctUseCorrectedBx_eff.root")
t5 = f5.Get("GEMCSCAnalyzer/trk_eff_ME11")
e5 = ROOT.TH1F("e5","e5",40,1.5,2.5)
t5.Draw("eta >> e5",num)
ee = ROOT.TH1F("ee","ee",40,1.5,2.5)
t5.Draw("eta >> ee",den)
e5.Divide(ee)

f6 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_clctToAlct_eff.root")
t6 = f6.Get("GEMCSCAnalyzer/trk_eff_ME11")
e6 = ROOT.TH1F("e6","e6",40,1.5,2.5)
t6.Draw("eta >> e6",num)
ef = ROOT.TH1F("ef","ef",40,1.5,2.5)
t6.Draw("eta >> ef",den)
e6.Divide(ef)


f7 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_tmbDropUsedClcts_matchEarliestClctME11Only_eff.root")
t7 = f7.Get("GEMCSCAnalyzer/trk_eff_ME11")
e7 = ROOT.TH1F("e7","e7",40,1.5,2.5)
t7.Draw("eta >> e7",num)
eg = ROOT.TH1F("eg","eg",40,1.5,2.5)
t7.Draw("eta >> eg",den)
e7.Divide(eg)


f8 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_tmbCrossBxAlgorithm_eff.root")
t8 = f8.Get("GEMCSCAnalyzer/trk_eff_ME11")
e8 = ROOT.TH1F("e8","e8",40,1.5,2.5)
t8.Draw("eta >> e8",num)
eh = ROOT.TH1F("eh","eh",40,1.5,2.5)
t8.Draw("eta >> eh",den)
e8.Divide(eh)



f9 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_tmbReadoutEarliest2_eff.root")
t9 = f9.Get("GEMCSCAnalyzer/trk_eff_ME11")
e9 = ROOT.TH1F("e9","e9",40,1.5,2.5)
t9.Draw("eta >> e9",num)
ei = ROOT.TH1F("ei","ei",40,1.5,2.5)
t9.Draw("eta >> ei",den)
e9.Divide(ei)




f10 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_SLHC_eff.root")
t10 = f10.Get("GEMCSCAnalyzer/trk_eff_ME11")
e10 = ROOT.TH1F("e10","e10",40,1.5,2.5)
t10.Draw("eta >> e10",num)
ej = ROOT.TH1F("ej","ej",40,1.5,2.5)
t10.Draw("eta >> ej",den)
e10.Divide(ej)


#e1.SetLineColor(ROOT.kBlack)
#e1.SetLineWidth(2)
#e1.SetLineStyle(2)


e2.SetLineColor(ROOT.kRed)
e2.SetLineWidth(2)
e2.SetLineStyle(1)

e3.SetLineColor(ROOT.kGreen+2)
e3.SetLineWidth(2)
e3.SetMarkerStyle(4)
e3.SetMarkerColor(ROOT.kGreen+2)

e4.SetLineColor(ROOT.kYellow)
e4.SetLineWidth(2)
e4.SetMarkerStyle(21)
e4.SetMarkerColor(ROOT.kGreen+2)

e5.SetLineColor(ROOT.kViolet-2)
e5.SetLineWidth(4)
e5.SetMarkerStyle(22)
e5.SetMarkerColor(ROOT.kGreen+2)

e6.SetLineColor(ROOT.kYellow-1)
e6.SetLineWidth(2)
e6.SetMarkerStyle(23)
e6.SetMarkerColor(ROOT.kGreen+2)

e7.SetLineColor(ROOT.kPink+1)
e7.SetLineWidth(2)
e7.SetMarkerStyle(25)
e7.SetMarkerColor(ROOT.kGreen+2)

e8.SetLineColor(ROOT.kOrange+2)
e8.SetLineWidth(2)
e8.SetMarkerStyle(26)
e8.SetMarkerColor(ROOT.kGreen+2)

e9.SetLineColor(ROOT.kGreen-2)
e9.SetLineWidth(4)
e9.SetMarkerStyle(20)
e9.SetMarkerColor(ROOT.kGreen+2)

e10.SetLineColor(ROOT.kBlue)
e10.SetLineWidth(2)
e10.SetLineStyle(2)               

b1 = ROOT.TH1F("b1","b1",50,1.4,2.5)
b1.GetYaxis().SetRangeUser(0.5,1.01)
b1.GetYaxis().SetTitleOffset(1.2)
b1.GetYaxis().SetNdivisions(520)
b1.GetYaxis().SetTitle("LCT reconstruction efficiency")
b1.GetXaxis().SetTitle("#eta of simulated muon track")
b1.SetTitle("Tree Based")
b1.SetStats(0)

b1.Draw()
e2.Draw("same")
e3.Draw("same P")
e4.Draw("same P")
e5.Draw("same P")
e6.Draw("same p")
e7.Draw("same p")
e8.Draw("same p")
e9.Draw("same p")
e10.Draw("same")

legend = ROOT.TLegend(0.17,0.13,0.72,0.52)
legend.SetFillColor(ROOT.kWhite)
#legend.SetBorderSize(0)
#legend.SetFillStyle(0)
legend.SetHeader("PU140 and 2<Pt<50")
#legend.AddEntry(e1,"TMB Baseline 1","l")
legend.AddEntry(e2,"TMB Baseline 2 num","l")
#legend.AddEntry(eb,"TMB Baseline 2 den","l")
legend.AddEntry(e3,"matchTrigWindowSize: 7BX to 3BX","p")
legend.AddEntry(e4,"alctUseCorrectedBx: False to True","p")
legend.AddEntry(e5,"clctUseCorrectedBx: False to True","p")
legend.AddEntry(e6,"clctToAlct: True to False","p")
legend.AddEntry(e7,"tmbDropUsedClcts && matchEarliestClctME11Only: False to True","p")
legend.AddEntry(e8,"tmbCrossBxAlgorithm: 0 to 1","p")
legend.AddEntry(e9,"tmbReadoutEarliest2: True to False","p")
legend.AddEntry(e10,"TMB SLHC","l")
legend.Draw("same")

c1.SaveAs("Whole3LCT.png")
