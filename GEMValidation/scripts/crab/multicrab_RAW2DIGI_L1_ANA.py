from CRABClient.UserUtilities import config
from samples import *
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-s", dest="sampleChoice",  type=int, default=0, help='0:central signal; 1: private signal; 2: data')
(options,args) = parser.parse_args()

chosenSample = []

## make a choice
if options.sampleChoice == 0:
    chosenSample = central_signal

if options.sampleChoice == 1:
    chosenSample = private_signal

if options.sampleChoice == 2:
    chosenSample = data

jobString = '_L1_ANA_20210226_v2'

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for sample in chosenSample:
        cconfig = config()
        cconfig.General.workArea = 'crab_projects' + jobString
        cconfig.General.transferLogs = True
        cconfig.General.requestName = sample[0] + jobString
        cconfig.JobType.pluginName = 'Analysis'
        cconfig.JobType.psetName = sample[3]
        cconfig.Site.storageSite = 'T3_US_FNALLPC'
        cconfig.Data.splitting = 'FileBased'
        cconfig.Data.unitsPerJob = 5
        cconfig.Data.outLFNDirBase = '/store/user/dildick/'
        cconfig.Data.inputDataset = sample[1]
        cconfig.Data.inputDBS = sample[2]
        print cconfig
        crabCommand('submit', config = cconfig)
