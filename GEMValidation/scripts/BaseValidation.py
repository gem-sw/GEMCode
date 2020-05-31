import os
from ROOT import TFile

class GEMCSCStubPlotter():
  def __init__(self):
    self.inputDir = os.getenv("CMSSW_BASE") + "/src/"
    self.inputFile = "out_ana.root"
    self.targetDir = "gem_csc_matching/"
    self.ext = ".png"
    self.analyzer = "MuonAnalyzer"
    self.file = TFile.Open(self.inputDir + self.inputFile)
    self.dirAna = (self.file).Get(self.analyzer)
    self.tree = self.dirAna.Get("SimTrack")
    self.yMin = 0.5
    self.yMax = 1.1
    self.etaMin = 0.9
    self.etaMax = 2.4
    self.pu = 140
