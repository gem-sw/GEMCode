from ROOT import gStyle, TH1F, TCanvas, TLegend, kRed, kBlue, kOrange, kGreen, kBlack

from helpers.cuts import *
from helpers.Helpers import *
from helpers.stations import *
from style.tdrstyle import *
import style.CMS_lumi as CMS_lumi
from style.canvas import newCanvas

topTitle = ""
#xTitle = "Generated muon |#eta|"
yTitle = "Efficiency"
subdirectory = "efficiency/CSCStub/"
#title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

setTDRStyle()

iPeriod = 0
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12

def CSCALCT(plotter):

    ## variables for the plot
    xTitle = "Generated muon |#eta|"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"

    for st in range(0,len(cscStations)):

        h_bins = "(25,%f,%f)"%(cscStations[st].eta_min,cscStations[st].eta_max)
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(plotter.yMin)
        base.SetMaximum(plotter.yMax)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        h1 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_alct(st), "same", kBlue)

        leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h1, "ALCT","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sEff_CSCALCT_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, h1, leg, csc

def CSCALCTL(plotter):

    xTitle = "Generated muon L"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Sqrt((vx*vx)+(vy*vy))"

    for st in range(0,len(cscStations)):

        h_bins = "(25,%f,%f)"%(cscStations[st].l_min,cscStations[st].l_max)
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(plotter.yMin)
        base.SetMaximum(plotter.yMax)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        h1 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_alct(st), "same", kBlue)

        leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h1, "ALCT","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sEff_CSCALCT_L_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, h1, leg, csc

        
def CSCCLCT(plotter):

    ## variables for the plot
    xTitle = "Generated muon |#eta|"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"

    for st in range(0,len(cscStations)):

        h_bins = "(25,%f,%f)"%(cscStations[st].eta_min,cscStations[st].eta_max)
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(plotter.yMin)
        base.SetMaximum(plotter.yMax)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_clct(st), "same",kBlue)

        leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h2, "CLCT","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sEff_CSCCLCT_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, h2, leg, csc

def CSCCLCTL(plotter):

    xTitle = "Generated muon L"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Sqrt((vx*vx)+(vy*vy))"

    for st in range(0,len(cscStations)):

        h_bins = "(25,%f,%f)"%(cscStations[st].l_min,cscStations[st].l_max)
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(plotter.yMin)
        base.SetMaximum(plotter.yMax)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_clct(st), "same",kBlue)

        leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h2, "CLCT","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sEff_CSCCLCT_L_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, h2, leg, csc
        

def CSCCLCTPattern(plotter):

    toPlot = "pt"

    for st in range(0,len(cscStations)):

        topTitle = ""
        xTitle = "Generated p_{T} GeV"
        yTitle = "Efficiency"
        title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

        h_bins = "(20,0,20)"
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(0.0)
        base.SetMaximum(1.1)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        def ok_csc_clct_pattern(st, p1, p2):
            return AND(ok_csc_clct(st),
                       OR(ok_pattern(st, p1),
                          ok_pattern(st, p2)) )

        h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_clct_pattern(st, 2, 3), "same",kBlack)
        h3 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_clct_pattern(st, 4, 5), "same",kRed)
        h4 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_clct_pattern(st, 6, 7), "same",kBlue)
        h5 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_clct_pattern(st, 8, 9), "same",kOrange)
        h6 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_clct_pattern(st, 10, 10), "same",kGreen+2)

        leg = TLegend(0.7,0.15,.95,0.45, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.SetHeader("PID")
        leg.AddEntry(h2, "#geq 2","pl")
        leg.AddEntry(h3, "#geq 4","pl")
        leg.AddEntry(h4, "#geq 6","pl")
        leg.AddEntry(h5, "#geq 8","pl")
        leg.AddEntry(h6, "#geq 10","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sEff_CSCCLCT_pattern_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, h2, leg, csc, h3, h4, h5, h6


def CSCLCT(plotter):

    ## variables for the plot
    xTitle = "Generated muon |#eta|"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"

    for st in range(0,len(cscStations)):

        h_bins = "(25,%f,%f)"%(cscStations[st].eta_min,cscStations[st].eta_max)
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(plotter.yMin)
        base.SetMaximum(plotter.yMax)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_lct(st), "same", kBlue)

        leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h2, "LCT","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sEff_CSCLCT_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, leg, csc, h2

def CSCLCTL(plotter):

    toPlot = "TMath::Sqrt((vx*vx)+(vy*vy))"
    xTitle = "Generated muon L"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

    for st in range(0,len(cscStations)):

        h_bins = "(25,%f,%f)"%(cscStations[st].l_min,cscStations[st].l_max)
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(plotter.yMin)
        base.SetMaximum(plotter.yMax)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_lct(st), "same", kBlue)

        leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h2, "LCT","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sEff_CSCLCT_L_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, leg, csc, h2
       

def GEMCSCLCT(plotter):

    ## variables for the plot
    xTitle = "Generated muon |#eta|"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"

    for st in [0,5]:

        h_bins = "(25,%f,%f)"%(cscStations[st].eta_min,cscStations[st].eta_max)
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(plotter.yMin)
        base.SetMaximum(plotter.yMax)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        gemst = 1
        if st==5:
            gemst = 2

        ok_alct_clct = ok_csc_clct(st) and ok_csc_alct(st) and ok_gem_pad(gemst)
        ok_alct_gem = ok_csc_alct(st) and ok_gem_copad(gemst)
        ok_clct_gem = ok_csc_clct(st) and ok_gem_copad(gemst)

        ok_any_combination = ok_alct_clct or ok_alct_gem or ok_clct_gem

        h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_any_combination, "same", kBlue)

        leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h2, "LCT","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sEff_GEMCSCLCT_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, leg, csc, h2

def GEMCSCLCTL(plotter):

    toPlot = "TMath::Sqrt((vx*vx)+(vy*vy))"
    xTitle = "Generated Muon L"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

    for st in [0,5]:

        h_bins = "(25,%f,%f)"%(cscStations[st].l_min,cscStations[st].l_max)
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(plotter.yMin)
        base.SetMaximum(plotter.yMax)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        gemst = 1
        if st==5:
            gemst = 2

        ok_alct_clct = ok_csc_clct(st) and ok_csc_alct(st) and ok_gem_pad(gemst)
        ok_alct_gem = ok_csc_alct(st) and ok_gem_copad(gemst)
        ok_clct_gem = ok_csc_clct(st) and ok_gem_copad(gemst)

        ok_any_combination = ok_alct_clct or ok_alct_gem or ok_clct_gem

        h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_any_combination, "same", kBlue)

        leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h2, "LCT","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sEff_GEMCSCLCT_L_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, leg, csc, h2

        


def MultipleCSCLCTPt(plotter):

    xTitle = "Generated muon p_{T} [GeV]"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = genpt

    h_bins = "(20,0,100)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = newCanvas()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(plotter.yMax)
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)
    base.Draw("")
    CMS_lumi.CMS_lumi(c, iPeriod, iPos)

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(2), "same", kBlue)
    h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(3), "same", kRed)
    h3 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(4), "same", kGreen+2)

    leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.05)
    leg.AddEntry(h1, "#geq 2 LCTs","pl")
    leg.AddEntry(h2, "#geq 3 LCTs","pl")
    leg.AddEntry(h3, "4 LCTs","pl")
    leg.Draw("same");

    c.Print("%sEff_MultiLCTs_pt_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg


def MultipleCSCLCTEta(plotter):

    ## variables for the plot
    xTitle = "Generated muon |#eta|"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"

    h_bins = "(20,1.2,2.4)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = newCanvas()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(plotter.yMax)
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)
    base.Draw("")
    CMS_lumi.CMS_lumi(c, iPeriod, iPos)

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(2), "same", kBlue)
    h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(3), "same", kRed)
    h3 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(4), "same", kGreen+2)

    leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "#geq 2 LCTs","pl")
    leg.AddEntry(h2, "#geq 3 LCTs","pl")
    leg.AddEntry(h3, "4 LCTs","pl")
    leg.Draw("same");

    c.Print("%sEff_MultiLCTs_eta_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg

def MultipleCSCLCTPhi(plotter):

    ## variables for the plot
    xTitle = "Generated muon #phi"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = genphi

    h_bins = "(20,-3.2,3.2)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = newCanvas()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(plotter.yMax)
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)
    base.Draw("")
    CMS_lumi.CMS_lumi(c, iPeriod, iPos)

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(2), "same", kBlue)
    h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(3), "same", kRed)
    h3 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(4), "same", kGreen+2)

    leg = TLegend(0.2,0.2,.5,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "#geq 2 LCTs","pl")
    leg.AddEntry(h2, "#geq 3 LCTs","pl")
    leg.AddEntry(h3, "4 LCTs","pl")
    leg.Draw("same");

    c.Print("%sEff_MultiLCTs_phi_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg



def MultipleCSCLCTL(plotter):

    ## variables for the plot
    xTitle = "Generated muon L"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Sqrt((vx*vx)+(vy*vy))"

    h_bins = "(34,0,170)"
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = newCanvas()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(0)
    base.SetMaximum(plotter.yMax)
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)
    base.Draw("")
    CMS_lumi.CMS_lumi(c, iPeriod, iPos)

    h1 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(2), "same", kBlue)
    h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(3), "same", kRed)
    h3 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_eta(1.2, 2.4), ok_csc_lcts(4), "same", kGreen+2)

    leg = TLegend(0.2,0.2,.5,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "#geq 2 LCTs","pl")
    leg.AddEntry(h2, "#geq 3 LCTs","pl")
    leg.AddEntry(h3, "4 LCTs","pl")
    leg.Draw("same");

    c.Print("%sEff_MultiLCTs_L_%s"%(plotter.targetDir + subdirectory, plotter.ext))

    del c, base, h1, leg
    


def CSCStub(plotter):
    CSCALCT(plotter)
    CSCALCTL(plotter)
    CSCCLCT(plotter)
    CSCCLCTL(plotter)
    CSCLCT(plotter)
    CSCLCTL(plotter)
    GEMCSCLCT(plotter)
    GEMCSCLCTL(plotter)
    CSCCLCTPattern(plotter)
    MultipleCSCLCTPt(plotter)
    MultipleCSCLCTEta(plotter)
    MultipleCSCLCTPhi(plotter)
    MultipleCSCLCTL(plotter)

def CSCStubComparison(plotter, plotter2):

    toPlot = "TMath::Abs(eta)"
    xTitle = "Generated muon |#eta|"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

    for st in range(0,len(cscStations)):

        h_bins = "(25,%f,%f)"%(cscStations[st].eta_min,cscStations[st].eta_max)
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(plotter.yMin)
        base.SetMaximum(plotter.yMax)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        h2 = draw_geff(plotter.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_clct(st), "same", kBlack)
        h3 = draw_geff(plotter2.tree, title, h_bins, toPlot, ok_csc_sh(st), ok_csc_clct(st), "same", kBlue)

        leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h2, "Run-1/2 CLCT","pl")
        leg.AddEntry(h3, "Run-3 CLCT","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sEff_CSCCLCT_comparison_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, leg, csc, h2, h3
