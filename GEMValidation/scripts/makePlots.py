import sys
import os

from ROOT import TFile, TDirectory, TTree, gROOT
from efficiency.plots import *
from resolution.plots import *
from occupancy.plots import *

## run quiet mode
sys.argv.append( '-b' )
gROOT.SetBatch(1)

class GEMCSCStubPlotter():
  def __init__(self, analyzer = "GEMCSCAnalyzer"):
    self.inputDir = os.getenv("CMSSW_BASE") + "/src/"
    self.inputFile = self.inputDir + "out_ana_phase2.root"
    self.baseDir = "plots/"
    self.ext = ".pdf"
    self.analyzer = analyzer
    self.targetDir = self.baseDir + self.analyzer + "/"
    self.file = TFile.Open(self.inputFile)
    self.dirAna = (self.file).Get(self.analyzer)
    self.tree = self.dirAna.Get("simTrack")
    self.treeFriends = ["genParticle", "cscSimHit", "cscDigi", "cscStub",
                        "gemSimHit", "gemDigi", "gemStub", "l1Mu", "l1Track"]
    for p in self.treeFriends:
      self.tree.AddFriend(self.dirAna.Get(p))
    self.yMin = 0.5
    self.yMax = 1.1


## needs to be cleaned up
plotter = GEMCSCStubPlotter()
makeEfficiencyPlots(plotter)
makeResolutionPlots(plotter)

plotter2 = GEMCSCStubPlotter("GEMCSCAnalyzerRun3CCLUT")
makeEfficiencyPlots(plotter2)
makeResolutionPlots(plotter2)

## efficiency comparison
makeEfficiencyComparisonPlots(plotter, plotter2)
makeResolutionComparisonPlots(plotter, plotter2)
