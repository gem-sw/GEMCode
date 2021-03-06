# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step2bis.py --filein file:step3.root --fileout file:step2bis.root --mc --eventcontent FEVTDEBUG --datatier GEN-SIM-DIGI-L1 --conditions auto:phase1_2021_realistic --step L1 --geometry DB:Extended --era Run3 --python_filename step2bis_L1.py --no_exec -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('ReL1',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('GEMCode.GEMValidation.GEMCSCAnalyzer_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:FFC59020-EA48-1F41-B4B8-FF34C0E09D88.root'
        '/store/relval/CMSSW_11_0_0_patch1/RelValZMM_14/GEN-SIM-DIGI-RAW/PU_110X_mcRun3_2021_realistic_v6-v1/20000/067CC83E-CD24-514F-9B19-8C6A0FE0A248.root',
        '/store/relval/CMSSW_11_0_0_patch1/RelValZMM_14/GEN-SIM-DIGI-RAW/PU_110X_mcRun3_2021_realistic_v6-v1/20000/11889C40-9C6C-FB4B-BDD9-787A9E24DF2B.root',
        '/store/relval/CMSSW_11_0_0_patch1/RelValZMM_14/GEN-SIM-DIGI-RAW/PU_110X_mcRun3_2021_realistic_v6-v1/20000/1772386A-B293-2343-BC00-CE43D2E4D7E0.root',
        '/store/relval/CMSSW_11_0_0_patch1/RelValZMM_14/GEN-SIM-DIGI-RAW/PU_110X_mcRun3_2021_realistic_v6-v1/20000/1DD5298E-A413-9247-B6F5-90A1947D8470.root',
        '/store/relval/CMSSW_11_0_0_patch1/RelValZMM_14/GEN-SIM-DIGI-RAW/PU_110X_mcRun3_2021_realistic_v6-v1/20000/43E5C33E-45F5-DB49-9D4B-972F36817A9C.root',
        '/store/relval/CMSSW_11_0_0_patch1/RelValZMM_14/GEN-SIM-DIGI-RAW/PU_110X_mcRun3_2021_realistic_v6-v1/20000/4A35113F-0308-3C49-8834-A55D89D8FCC8.root',
        '/store/relval/CMSSW_11_0_0_patch1/RelValZMM_14/GEN-SIM-DIGI-RAW/PU_110X_mcRun3_2021_realistic_v6-v1/20000/6050654C-1EBD-7642-8316-6FB05E1A45AD.root',
        '/store/relval/CMSSW_11_0_0_patch1/RelValZMM_14/GEN-SIM-DIGI-RAW/PU_110X_mcRun3_2021_realistic_v6-v1/20000/89558BB3-16B4-6D45-AB29-BE5FDE8C42C1.root',
        '/store/relval/CMSSW_11_0_0_patch1/RelValZMM_14/GEN-SIM-DIGI-RAW/PU_110X_mcRun3_2021_realistic_v6-v1/20000/8D70223E-5122-D340-AAC7-8599725CC327.root',
        '/store/relval/CMSSW_11_0_0_patch1/RelValZMM_14/GEN-SIM-DIGI-RAW/PU_110X_mcRun3_2021_realistic_v6-v1/20000/93ED664A-EFE0-9E40-8F6E-0F535E50B009.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2bis.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-L1'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step2bis_run3.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

## keep all CSC trigger versions
process.FEVTDEBUGoutput.outputCommands.append('keep *_simCscTriggerPrimitiveDigis*_*_*')
process.FEVTDEBUGoutput.outputCommands.append('keep *_simEmtfDigis*_*_*')

## drop all calorimetry, tracker and raw
process.FEVTDEBUGoutput.outputCommands.append('drop *_simHcal*_*_*')
process.FEVTDEBUGoutput.outputCommands.append('drop *_simEcal*_*_*')
process.FEVTDEBUGoutput.outputCommands.append('drop *_g4SimHits_Tracker*_*')
process.FEVTDEBUGoutput.outputCommands.append('drop *_rawDataCollector_*_*')
process.FEVTDEBUGoutput.outputCommands.append('drop *_g4SimHits_Ecal*_*')
process.FEVTDEBUGoutput.outputCommands.append('drop *_g4SimHits_Hcal*_*')

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

from GEMCode.GEMValidation.cscTriggerCustoms import addCSCTriggerRun3
process = addCSCTriggerRun3(process)

from GEMCode.GEMValidation.cscTriggerCustoms import addAnalysisRun3
process = addAnalysisRun3( process)

process.GEMCSCAnalyzer.gemStripDigi.verbose = 1
process.GEMCSCAnalyzer.gemStripDigi.matchToSimLink = True
process.GEMCSCAnalyzer.gemPadDigi.verbose = 1
process.GEMCSCAnalyzer.gemPadCluster.verbose = 1
process.GEMCSCAnalyzer.gemCoPadDigi.verbose = 1

from GEMCode.GEMValidation.cscTriggerCustoms import runOn110XMC
process = runOn110XMC(process)

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.muonGEMDigis)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.ana_step = cms.Path(
    process.GEMCSCAnalyzer
    #                            * process.GEMCSCAnalyzerRun3CCLUT
)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("out_ana_run3.root")
)

# Schedule definition
process.schedule = cms.Schedule(
    #process.raw2digi_step,
    process.L1simulation_step,
    process.ana_step,
    process.endjob_step
#    process.FEVTDEBUGoutput_step
)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
