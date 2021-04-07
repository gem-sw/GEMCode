from ROOT import gStyle, TH1F, TCanvas, TLegend, kRed, kBlue, kOrange, kGreen, TH2F, gPad

from helpers.cuts import *
from helpers.Helpers import *
from helpers.stations import *
from style.tdrstyle import *
from array import *
import style.CMS_lumi as CMS_lumi
from style.canvas import newCanvas, newCanvas2D
import numpy

topTitle = ""
xTitle = "Strip_{L1T} - Strip_{SIM}"
yTitle = "Entries"
subdirectory = "occupancy/CSCStub/"
title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

setTDRStyle()

iPeriod = 0
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12

def CLCTPattern(plotter):

    for st in range(0,len(cscStations)):

        h_bins = "(100,0,1.5)"
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(0)
        base.SetMaximum(0.08)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        toPlot1 = delta_fhs_clct(st)
        toPlot2 = delta_fqs_clct(st)
        toPlot3 = delta_fes_clct(st)

        h1 = draw_1D(plotter.tree, title, h_bins, toPlot1, "", "same", kBlue)
        h2 = draw_1D(plotter.tree, title, h_bins, toPlot2, "", "same", kGreen+2)
        h3 = draw_1D(plotter.tree, title, h_bins, toPlot3, "", "same", kRed+1)

        h1.Scale(1./h1.GetEntries())
        h2.Scale(1./h2.GetEntries())
        h3.Scale(1./h3.GetEntries())
        h1.Draw("histsame")
        h2.Draw("histsame")
        h3.Draw("histsame")

        leg = TLegend(0.15,0.6,.45,0.9, "", "brNDC");
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h1, "1/2 strip","pl")
        leg.AddEntry(h2, "1/4 strip","pl")
        leg.AddEntry(h3, "1/8 strip","pl")
        leg.Draw("same");

        csc = drawCSCLabel(cscStations[st].label, 0.85,0.85,0.05)

        c.Print("%sOcc_CSCCLCT_pos_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, h2, leg, csc, h1, h3

def CSCFloatSlope(plotter, even):

    xTitle = "True muon pT [GeV]"
    yTitle = "CLCT Slope [Half-strips/layer]"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

    for st in range(0,len(cscStations)):

        h_bins = "(50,0,50)"
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        h_binsY = "(100,-2.5,2.5)"
        nBinsY = int(h_binsY[1:-1].split(',')[0])
        minBinY = float(h_binsY[1:-1].split(',')[1])
        maxBinY = float(h_binsY[1:-1].split(',')[2])

        toPlot1 = "fabs(%s):simTrack.pt"%(slope_clct(st, even))

        c = newCanvas2D()
        gPad.SetLogz()
        base = draw_2D(plotter.tree, title, h_bins, h_binsY, toPlot1, "fabs(%s)<2.5"%(slope_clct(st, even)), "COLZ")
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)

        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        csc = drawCSCLabel(cscStations[st].label, 0.75,0.85,0.05)

        if even:
            c.Print("%sOcc_CSCCLCT_floatslope_even_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))
        else:
            c.Print("%sOcc_CSCCLCT_floatslope_odd_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, csc

    ## optimization based on ME1/b and ME1/2
    binYOptions = [
        [0.000,  0.001,  0.003,  0.006,  0.009,  0.014,  0.019,  0.026,  0.033,  0.041,  0.051,  0.061,  0.072,  0.084,  0.097,  0.110,  0.125],
        [0.000,  0.002,  0.006,  0.011,  0.018,  0.028,  0.039,  0.051,  0.066,  0.083,  0.101,  0.121,  0.143,  0.167,  0.193,  0.221,  0.250],
        [0.000,  0.004,  0.011,  0.022,  0.037,  0.055,  0.077,  0.103,  0.132,  0.165,  0.202,  0.243,  0.287,  0.335,  0.386,  0.441,  0.500],
        [0.000,  0.006,  0.017,  0.033,  0.055,  0.083,  0.116,  0.154,  0.199,  0.248,  0.303,  0.364,  0.430,  0.502,  0.579,  0.662,  0.750],
        [0.00,  0.01,  0.02,  0.04,  0.07,  0.11,  0.15,  0.21,  0.26,  0.33,  0.40,  0.49,  0.57,  0.67,  0.77,  0.88,  1.00],
        [0.00,  0.01,  0.02,  0.05,  0.08,  0.12,  0.17,  0.23,  0.29,  0.36,  0.44,  0.53,  0.63,  0.74,  0.85,  0.97,  1.10],
        [0.00,  0.01,  0.03,  0.05,  0.09,  0.13,  0.19,  0.25,  0.32,  0.40,  0.49,  0.58,  0.69,  0.80,  0.93,  1.06,  1.20],
        [0.00,  0.01,  0.03,  0.06,  0.10,  0.14,  0.20,  0.27,  0.34,  0.43,  0.53,  0.63,  0.75,  0.87,  1.00,  1.15,  1.30],
        [0.00,  0.01,  0.03,  0.06,  0.10,  0.15,  0.22,  0.29,  0.37,  0.46,  0.57,  0.68,  0.80,  0.94,  1.08,  1.24,  1.40],
        [0.00,  0.01,  0.03,  0.07,  0.11,  0.17,  0.23,  0.31,  0.40,  0.50,  0.61,  0.73,  0.86,  1.00,  1.16,  1.32,  1.50],
        [0.00,  0.01,  0.04,  0.07,  0.12,  0.18,  0.25,  0.33,  0.42,  0.53,  0.65,  0.78,  0.92,  1.07,  1.24,  1.41,  1.60],
        [0.00,  0.01,  0.04,  0.07,  0.12,  0.19,  0.26,  0.35,  0.45,  0.56,  0.69,  0.82,  0.97,  1.14,  1.31,  1.50,  1.70],
        [0.00,  0.01,  0.04,  0.08,  0.13,  0.20,  0.28,  0.37,  0.48,  0.60,  0.73,  0.87,  1.03,  1.20,  1.39,  1.59,  1.80],
        [0.00,  0.01,  0.04,  0.08,  0.14,  0.21,  0.29,  0.39,  0.50,  0.63,  0.77,  0.92,  1.09,  1.27,  1.47,  1.68,  1.90],
        [0.00,  0.01,  0.04,  0.09,  0.15,  0.22,  0.31,  0.41,  0.53,  0.66,  0.81,  0.97,  1.15,  1.34,  1.54,  1.76,  2.00]
    ]

    def calculateEntropy(histo):
        sumxy = 0
        for iX in range(1, histo.GetNbinsX()):
            for iY in range(1, histo.GetNbinsY()):
                binXY = histo.GetBinContent(iX,iY)
                if binXY > 0:
                    sumxy += binXY * numpy.log(binXY)
        entropy = -sumxy
        return entropy

    iBinOption = 0
    for binYOption in binYOptions:
        iBinOption += 1
        ## change last one to 2.5 - captures the overflow
        binYOption[-1] = 2.5
        if even:
            print( binYOption)

        c = newCanvas2D()
        gPad.SetLogz()

        toPlot1 = "%s:simTrack.pt"%(slope_clct(st, even))

        base = draw_2Dbis(plotter.tree, title, h_bins, 16, array('d',binYOption), toPlot1, "fabs(%s)<2.5"%(slope_clct(0, even)), "COLZ")
        base2 = draw_2Dbis(plotter.tree, title, h_bins, 16, array('d',binYOption), toPlot1, "fabs(%s)<2.5"%(slope_clct(3, even)), "COLZ")
        base2.Add(base,1)
        base2.Scale(1./base2.GetEntries())
        base2.GetXaxis().SetLabelSize(0.05)
        base2.GetYaxis().SetLabelSize(0.05)
        base2.GetXaxis().SetTitleSize(0.05)
        base2.GetYaxis().SetTitleSize(0.05)

        if even:
            print("& %.3f"%calculateEntropy(base2))
        else:
            print("& %.3f \\\\"%calculateEntropy(base2))

        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        csc = drawCSCLabel("ME1", 0.75,0.85,0.05)

        if even:
            c.Print("%sOcc_CSCCLCT_floatslope_even_binOption%d_ME1%s"%(plotter.targetDir + subdirectory, iBinOption, plotter.ext))
        else:
            c.Print("%sOcc_CSCCLCT_floatslope_odd_binOption%d_ME1%s"%(plotter.targetDir + subdirectory, iBinOption, plotter.ext))

        del c, base, base2, csc


def CSCFloatSlopeV2(plotter, even):

    xTitle = "True muon pT [GeV]"
    yTitle = "CLCT Slope [Half-strips/layer]"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

    for st in range(0,len(cscStations)):

        h_bins = "(50,0,50)"
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        h_binsY = [0.0,0.01,0.031,0.062,0.103,0.154,0.216,0.288,0.371,0.463,0.566,0.679,0.803,0.937,1.081,1.235,2.5]

        toPlot1 = "fabs(%s):simTrack.pt"%(slope_clct(st, even))

        c = newCanvas2D()
        gPad.SetLogz()
        base = draw_2Dbis(plotter.tree, title, h_bins, 16, array('d',h_binsY), toPlot1, "fabs(%s)<2.5"%(slope_clct(st, even)), "COLZ")
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)

        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        csc = drawCSCLabel(cscStations[st].label, 0.75,0.85,0.05)

        if even:
            c.Print("%sOcc_CSCCLCT_floatslope_even_final_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))
        else:
            c.Print("%sOcc_CSCCLCT_floatslope_odd_final_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, csc


def CSCFloatSlope1D(plotter, even):

    yTitle = "Entries"
    xTitle = "CLCT Slope [Half-strips/layer]"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)

    for st in range(0,len(cscStations)):

        h_bins = "(100,-2.5,2.5)"
        nBins = int(h_bins[1:-1].split(',')[0])
        minBin = float(h_bins[1:-1].split(',')[1])
        maxBin = float(h_bins[1:-1].split(',')[2])

        c = newCanvas()
        base  = TH1F("base",title,nBins,minBin,maxBin)
        base.SetMinimum(0)
        base.SetMaximum(0.08)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.05)
        base.GetYaxis().SetTitleSize(0.05)
        base.Draw("")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)

        toPlot1 = slope_clct(st, even)

        h1 = draw_1D(plotter.tree, title, h_bins, toPlot1, "", "same", kBlue)

        csc = drawCSCLabel(cscStations[st].label, 0.75,0.85,0.05)

        if even:
            c.Print("%sOcc_CSCCLCT_floatslope_even_1D_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))
        else:
            c.Print("%sOcc_CSCCLCT_floatslope_odd_1D_%s%s"%(plotter.targetDir + subdirectory, cscStations[st].labelc,  plotter.ext))

        del c, base, csc, h1

def CSCStub(plotter):
    #CLCTPattern(plotter)
    CSCFloatSlope(plotter,True)
    CSCFloatSlope(plotter,False)
    CSCFloatSlopeV2(plotter,True)
    CSCFloatSlopeV2(plotter,False)


    #CSCFloatSlope1D(plotter,False)
    #CSCFloatSlope1D(plotter,True)
