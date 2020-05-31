import sys

from ROOT import *
from style import CMS_lumi

from cuts import *
from drawPlots import *

## run quiet mode
import sys
sys.argv.append( '-b' )

import ROOT
ROOT.gROOT.SetBatch(1)

from BaseValidation import *
from GEMCSCValidation import *

plotter = GEMCSCStubPlotter()

#simTrackToCscSimHitMatching(plotter)
#simTrackToCscStripsWiresMatching(plotter,st)
#simTrackToCscStripsWiresMatching_2(plotter,st)
#simTrackToCscAlctClctMatching(plotter,st)
#simTrackToCscAlctClctMatching_2(plotter,st)
#simTrackToCscLctMatching(plotter,st)
