# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step2bis.py --filein file:step3.root --fileout file:step2bis.root --mc --eventcontent FEVTDEBUG --datatier GEN-SIM-DIGI-L1 --conditions auto:phase1_2021_realistic --step L1 --geometry DB:Extended --era Run3 --python_filename step2bis_L1.py --no_exec -n 10
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.Eras.Era_Run3_cff import Run3
from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

options = VarParsing('analysis')
options.register ("test", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool)
options.register ("runOnData", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool)
options.register ("runOnRaw", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool)
options.register ("runAna", True, VarParsing.multiplicity.singleton, VarParsing.varType.bool)
options.register ("run3", True, VarParsing.multiplicity.singleton, VarParsing.varType.bool)
options.register ("crab", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool)
options.parseArguments()

process_era = Run3
if not options.run3:
      process_era = Run2_2018

process = cms.Process("ReL1", process_era)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
#process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('GEMCode.GEMValidation.MuonNtuplizer_cff')

nEvents = -1
if options.test:
    nEvents = 100

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(nEvents),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source(
      "PoolSource",
      fileNames = cms.untracked.vstring(
            "file:/uscms/home/dildick/nobackup/work/LLPStudiesWithSergoEtAL/CMSSW_12_0_0_pre2/src/132B0128-FF59-DB4A-A3AD-AF4D8B4D21D2.root"
            #"/store/user/nimenend/HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm_TuneCP5_14TeV_pythia/HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm_TuneCP5_14TeV_pythia/200710_130547/0000/step2_1.root"
    ),
    secondaryFileNames = cms.untracked.vstring(),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
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

process.FEVTDEBUGoutput = cms.OutputModule(
      "PoolOutputModule",
      dataset = cms.untracked.PSet(
            dataTier = cms.untracked.string('GEN-SIM-DIGI-L1'),
            filterName = cms.untracked.string('')
      ),
      fileName = cms.untracked.string('file:step2bis_run3.root'),
      outputCommands = cms.untracked.vstring('keep *'),
      splitLevel = cms.untracked.int32(0)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("out_ana_muonshower.root")
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
if options.runOnData:
      process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
else:
      process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

from GEMCode.GEMValidation.cscTriggerCustoms import runOn110XMC, runOn110XMC_IgnoreIncorrectGEMDB
if options.runOnRaw:
    process = runOn110XMC_IgnoreIncorrectGEMDB(process, options.crab)

from GEMCode.GEMValidation.sampleProductionCustoms import dropNonMuonCollections
process = dropNonMuonCollections(process)

# the analyzer configuration
ana = process.MuonNtuplizer
ana.verbose = 1
ana.genParticle.pdgIds = cms.vint32(6000113, -6000113, 9000006, -9000006, 9000007, -9000007)
ana.genParticle.stableParticle = False
ana.genParticle.verbose = 0
ana.simTrack.minEta = 0.9
ana.simTrack.maxEta = 2.4
ana.simTrack.minPt = 5
#ana.simTrack.verbose = 1
ana.simTrack.pdgIds = cms.vint32(6000113, -6000113, 9000006, -9000006, 9000007, -9000007)
ana.cscSimHit.simMuOnly = False
ana.cscSimHit.discardEleHits = False
ana.gemStripDigi.matchDeltaStrip = 2
ana.cscLCT.addGhostLCTs = cms.bool(True)
ana.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
ana.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
ana.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
ana.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","MPCSORTED","ReL1")
ana.cscShower.verbose = 1
ana.emtfShower.verbose = 1
ana.muonShower.verbose = 1

if options.runOnRaw:
    ana.gemStripDigi.matchToSimLink = False
    ana.gemStripDigi.inputTag = "muonGEMDigis"
    #ana.muon.inputTag = cms.InputTag("gmtStage2Digis","Muon")

## customize unpacker
process.SimL1Emulator = cms.Sequence(process.SimL1TMuonTask)

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
if not options.run3:
      process.raw2digi_step = cms.Path(process.muonCSCDigis)


process.simCscTriggerPrimitiveDigis.runME11ILT = cms.bool(False)
process.L1simulation_step = cms.Path(
      process.simCscTriggerPrimitiveDigis *
      process.simEmtfShowers *
      process.simGmtShowerDigis
)
process.ana_step = cms.Path(process.MuonNtuplizer)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule()
## unpack
if options.runOnRaw:
    process.schedule.extend([process.raw2digi_step])

## l1
process.schedule.extend([process.L1simulation_step])

## analysis
if options.runAna:
    process.schedule.extend([process.ana_step])

## endjob
process.schedule.extend([process.endjob_step])

from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
