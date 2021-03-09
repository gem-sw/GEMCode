import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Modifier_phase2_muon_cff import phase2_muon

def runOn110XMC(process):
    ## customize unpacker
    process.GlobalTag.toGet = cms.VPSet(
        cms.PSet(record = cms.string("GEMeMapRcd"),
                 tag = cms.string("GEMeMapDummy"),
                 connect = cms.string("sqlite_file:GEMCode/GEMValidation/python/GEMeMapDummy.db")
             )
    )
    process.muonGEMDigis.useDBEMap = True
    process.simMuonGEMPadDigis.InputCollection = "muonGEMDigis"
    return process

def addCSCTriggerRun3(process):
    ## Run-3 patterns with CCLUT
    process.simCscTriggerPrimitiveDigisRun3CCLUT = process.simCscTriggerPrimitiveDigis.clone()
    process.simCscTriggerPrimitiveDigisRun3CCLUT.commonParam.runCCLUT = True
    process.simEmtfDigisRun3CCLUT = process.simEmtfDigis.clone()

    process.simEmtfDigis.CSCInput = cms.InputTag(
        'simCscTriggerPrimitiveDigis','MPCSORTED',process._Process__name)
    process.simEmtfDigisRun3CCLUT.CSCInput = cms.InputTag(
        'simCscTriggerPrimitiveDigisRun3CCLUT','MPCSORTED',process._Process__name)

    ## redefine the L1-step
    process.SimL1Emulator = cms.Sequence(
        process.simMuonGEMPadDigis *
        process.simMuonGEMPadDigiClusters *
        process.simCscTriggerPrimitiveDigis *
        process.simCscTriggerPrimitiveDigisRun3CCLUT *
        process.simEmtfDigis *
        process.simEmtfDigisRun3CCLUT
    )

    return process

def addAnalysisRun3(process):

    ana = process.GEMCSCAnalyzer
    ana.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
    ana.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
    ana.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
    ana.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","MPCSORTED","ReL1")
    ana.emtfTrack.inputTag = cms.InputTag("simEmtfDigis","","ReL1")

    useUnpacked = False
    if useUnpacked:
        ana.gemStripDigi.inputTag = "muonGEMDigis"
        ana.muon.inputTag = cms.InputTag("gmtStage2Digis","Muon")

    process.GEMCSCAnalyzerRun3CCLUT = process.GEMCSCAnalyzer.clone()
    anaCCLUT = process.GEMCSCAnalyzerRun3CCLUT
    anaCCLUT.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","","ReL1")
    anaCCLUT.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","","ReL1")
    anaCCLUT.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","","ReL1")
    anaCCLUT.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","MPCSORTED","ReL1")
    anaCCLUT.emtfTrack.inputTag = cms.InputTag("simEmtfDigisRun3CCLUT","","ReL1")

    return process


def addAnalysisRun3HST(process):

    ana = process.GEMCSCAnalyzer
    ana.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
    ana.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
    ana.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","","ReL1")
    ana.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","MPCSORTED","ReL1")
    ana.emtfTrack.inputTag = cms.InputTag("simEmtfDigis","","ReL1")

    useUnpacked = True
    if useUnpacked:
        ana.gemStripDigi.matchToSimLink = False
        ana.gemStripDigi.inputTag = "muonGEMDigis"
        ana.muon.inputTag = cms.InputTag("gmtStage2Digis","Muon")

    return process
