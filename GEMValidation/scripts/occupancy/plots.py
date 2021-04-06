import os

from occupancy.CSCStub import *

## need to create directory structure - assume it does not exist yet
def makeDir(plotter):
    base = plotter.baseDir + "/"
    analyzer = plotter.analyzer
    paths = [
        base,
        base + analyzer,
        base + analyzer + "/occupancy",
        base + analyzer + "/occupancy/CSCStub",
    ]
    for p in paths:
        if not os.path.exists(p):
            os.mkdir(p)

def makeOccupancyPlots(plotter):
    makeDir(plotter)
    CSCStub(plotter)
