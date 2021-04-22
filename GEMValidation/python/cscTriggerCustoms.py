import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Modifier_phase2_muon_cff import phase2_muon

def runOn110XMC(process):
    ## customize unpacker
    process.GlobalTag.toGet = cms.VPSet(
        cms.PSet(record = cms.string("GEMeMapRcd"),
                 tag = cms.string("GEMeMapDummy"),
                 connect = cms.string("sqlite_file:GEMeMapDummy.db")
             )
    )
    process.muonGEMDigis.useDBEMap = True
    process.simMuonGEMPadDigis.InputCollection = "muonGEMDigis"
    return process

def runOn120XMC(process):
    ## customize unpacker
    process.muonGEMDigis.useDBEMap = True
    process.simMuonGEMPadDigis.InputCollection = "muonGEMDigis"
    return process

def dropCaloDigis(process):
    process.pdigi_valid.remove(process.simEcalTriggerPrimitiveDigis)
    process.pdigi_valid.remove(process.simEcalDigis)
    process.pdigi_valid.remove(process.simEcalPreshowerDigis)
    process.pdigi_valid.remove(process.simHcalTriggerPrimitiveDigis)
    process.pdigi_valid.remove(process.simHcalDigis)
    process.pdigi_valid.remove(process.simHcalTTPDigis)
    ## don't need DT digis
    process.pdigi_valid.remove(process.simMuonDTDigis)
    return process

def addCSCTriggerRun3(process):
    ## Run-2 patterns without ILT
    process.simCscTriggerPrimitiveDigis.commonParam.runME11ILT = False
    process.simCscTriggerPrimitiveDigis.commonParam.GEMPadDigiClusterProducer = cms.InputTag("")
    process.simEmtfDigis.CSCInput = cms.InputTag(
        'simCscTriggerPrimitiveDigis','MPCSORTED',process._Process__name)

    ## Run-2 patterns with ILT
    process.simCscTriggerPrimitiveDigisILT = process.simCscTriggerPrimitiveDigis.clone()
    process.simCscTriggerPrimitiveDigisILT.commonParam.runME11ILT = True
    process.simCscTriggerPrimitiveDigisILT.commonParam.GEMPadDigiClusterProducer = cms.InputTag("simMuonGEMPadDigiClusters")
    process.simEmtfDigisILT = process.simEmtfDigis.clone()
    process.simEmtfDigisILT.CSCInput = cms.InputTag(
        'simCscTriggerPrimitiveDigisILT','MPCSORTED',process._Process__name)

    ## Run-3 patterns with CCLUT, without ILT
    process.simCscTriggerPrimitiveDigisRun3CCLUT = process.simCscTriggerPrimitiveDigis.clone()
    process.simCscTriggerPrimitiveDigisRun3CCLUT.commonParam.runCCLUT = True
    process.simCscTriggerPrimitiveDigisRun3CCLUT.commonParam.runME11ILT = False
    process.simCscTriggerPrimitiveDigisRun3CCLUT.commonParam.GEMPadDigiClusterProducer = cms.InputTag("")
    process.simEmtfDigisRun3CCLUT = process.simEmtfDigis.clone()
    process.simEmtfDigisRun3CCLUT.CSCInput = cms.InputTag(
        'simCscTriggerPrimitiveDigisRun3CCLUT','MPCSORTED',process._Process__name)

    ## Run-3 patterns with CCLUT, with ILT
    process.simCscTriggerPrimitiveDigisRun3CCLUTILT = process.simCscTriggerPrimitiveDigis.clone()
    process.simCscTriggerPrimitiveDigisRun3CCLUTILT.commonParam.runCCLUT = True
    process.simCscTriggerPrimitiveDigisRun3CCLUTILT.commonParam.runME11ILT = True
    process.simCscTriggerPrimitiveDigisRun3CCLUTILT.commonParam.GEMPadDigiClusterProducer = cms.InputTag("simMuonGEMPadDigiClusters")
    process.simEmtfDigisRun3CCLUTILT = process.simEmtfDigis.clone()
    process.simEmtfDigisRun3CCLUTILT.CSCInput = cms.InputTag(
        'simCscTriggerPrimitiveDigisRun3CCLUTILT','MPCSORTED',process._Process__name)

    ## redefine the L1-step
    process.SimL1Emulator = cms.Sequence(
        process.simMuonGEMPadDigis *
        process.simMuonGEMPadDigiClusters *
        process.simCscTriggerPrimitiveDigis *
        process.simCscTriggerPrimitiveDigisILT *
        process.simCscTriggerPrimitiveDigisRun3CCLUT *
        process.simCscTriggerPrimitiveDigisRun3CCLUTILT *
        process.simEmtfDigis *
        process.simEmtfDigisILT *
        process.simEmtfDigisRun3CCLUT *
        process.simEmtfDigisRun3CCLUTILT
    )

    return process

def addAnalysisRun3(process):

    ana = process.GEMCSCAnalyzer
    processName = "DIGI"
    ana.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","",processName)
    ana.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","",processName)
    ana.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","",processName)
    ana.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigis","MPCSORTED",processName)
    ana.emtfTrack.inputTag = cms.InputTag("simEmtfDigis","",processName)

    useUnpacked = False
    if useUnpacked:
        ana.gemStripDigi.inputTag = "muonGEMDigis"
        ana.muon.inputTag = cms.InputTag("gmtStage2Digis","Muon")

    process.GEMCSCAnalyzerRun3CCLUT = process.GEMCSCAnalyzer.clone()
    anaCCLUT = process.GEMCSCAnalyzerRun3CCLUT
    anaCCLUT.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","",processName)
    anaCCLUT.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","",processName)
    anaCCLUT.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","",processName)
    anaCCLUT.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisRun3CCLUT","MPCSORTED",processName)
    anaCCLUT.emtfTrack.inputTag = cms.InputTag("simEmtfDigisRun3CCLUT","",processName)

    process.GEMCSCAnalyzerNoILT = process.GEMCSCAnalyzer.clone()
    anaCCLUT = process.GEMCSCAnalyzerNoILT
    anaCCLUT.cscALCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisNoILT","",processName)
    anaCCLUT.cscCLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisNoILT","",processName)
    anaCCLUT.cscLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisNoILT","",processName)
    anaCCLUT.cscMPLCT.inputTag = cms.InputTag("simCscTriggerPrimitiveDigisNoILT","MPCSORTED",processName)
    anaCCLUT.emtfTrack.inputTag = cms.InputTag("simEmtfDigisNoILT","",processName)

    process.Analysis = cms.Sequence(
        process.GEMCSCAnalyzer *
        process.GEMCSCAnalyzerRun3CCLUT
    )

    return process
