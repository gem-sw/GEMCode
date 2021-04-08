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

        toPlot1 = "%s:simTrack.pt"%(slope_clct(st, even))

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
        [0.000,  0.001,  0.003,  0.006,  0.009,  0.014,  0.019,  0.026,  0.033,  0.041,  0.051,  0.061,  0.072,  0.084,  0.097,  0.110,  0.125  ],
        [0.000,  0.002,  0.006,  0.011,  0.018,  0.028,  0.039,  0.051,  0.066,  0.083,  0.101,  0.121,  0.143,  0.167,  0.193,  0.221,  0.250  ],
        [0.000,  0.004,  0.011,  0.022,  0.037,  0.055,  0.077,  0.103,  0.132,  0.165,  0.202,  0.243,  0.287,  0.335,  0.386,  0.441,  0.500  ],
        [0.000,  0.006,  0.017,  0.033,  0.055,  0.083,  0.116,  0.154,  0.199,  0.248,  0.303,  0.364,  0.430,  0.502,  0.579,  0.662,  0.750  ],
        [0.000,  0.007,  0.022,  0.044,  0.074,  0.110,  0.154,  0.206,  0.265,  0.331,  0.404,  0.485,  0.574,  0.669,  0.772,  0.882,  1.000  ],
        [0.000,  0.008,  0.024,  0.049,  0.081,  0.121,  0.170,  0.226,  0.291,  0.364,  0.445,  0.534,  0.631,  0.736,  0.849,  0.971,  1.100  ],
        [0.000,  0.009,  0.026,  0.053,  0.088,  0.132,  0.185,  0.247,  0.318,  0.397,  0.485,  0.582,  0.688,  0.803,  0.926,  1.059,  1.200  ],
        [0.000,  0.010,  0.029,  0.057,  0.096,  0.143,  0.201,  0.268,  0.344,  0.430,  0.526,  0.631,  0.746,  0.870,  1.004,  1.147,  1.300  ],
        [0.000,  0.010,  0.031,  0.062,  0.103,  0.154,  0.216,  0.288,  0.371,  0.463,  0.566,  0.679,  0.803,  0.937,  1.081,  1.235,  1.400  ],
        [0.000,  0.011,  0.033,  0.066,  0.110,  0.165,  0.232,  0.309,  0.397,  0.496,  0.607,  0.728,  0.860,  1.004,  1.158,  1.324,  1.500  ],
        [0.000,  0.012,  0.035,  0.071,  0.118,  0.176,  0.247,  0.329,  0.424,  0.529,  0.647,  0.776,  0.918,  1.071,  1.235,  1.412,  1.600  ],
        [0.000,  0.012,  0.037,  0.075,  0.125,  0.187,  0.262,  0.350,  0.450,  0.562,  0.687,  0.825,  0.975,  1.137,  1.312,  1.500,  1.700  ],
        [0.000,  0.013,  0.040,  0.079,  0.132,  0.199,  0.278,  0.371,  0.476,  0.596,  0.728,  0.874,  1.032,  1.204,  1.390,  1.588,  1.800  ],
        [0.000,  0.014,  0.042,  0.084,  0.140,  0.210,  0.293,  0.391,  0.503,  0.629,  0.768,  0.922,  1.090,  1.271,  1.467,  1.676,  1.900  ],
        [0.000,  0.015,  0.044,  0.088,  0.147,  0.221,  0.309,  0.412,  0.529,  0.662,  0.809,  0.971,  1.147,  1.338,  1.544,  1.765,  2.000  ],
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
