import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    crossSection = cms.untracked.double(1.504*0.0632),
    comEnergy = cms.double(14000.0),
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            TauolaPolar,
            TauolaDefaultInputCards
        ),
        parameterSets = cms.vstring('Tauola')
    ),                    
    UseExternalGenerators = cms.untracked.bool(True),
    PythiaParameters = cms.PSet(
    pythiaUESettingsBlock,             
# set proccess to be simulated
    processParameters = cms.vstring(
            'MSEL=0            ! User defined processes', 
            'MSUB(24)= 1       ! ff->ZH (SM)', 
            'PMAS(25,1)= 125.  ! m_h',
            'PMAS(6,1)= 173.3  ! mass of top quark',
            'PMAS(23,1)=91.187 ! mass of Z',
            'PMAS(24,1)=80.39  ! mass of W',
            
            # Z decay
            'MDME( 174,1) = 0    !Z decay into d dbar', 
            'MDME( 175,1) = 0    !Z decay into u ubar', 
            'MDME( 176,1) = 0    !Z decay into s sbar', 
            'MDME( 177,1) = 0    !Z decay into c cbar', 
            'MDME( 178,1) = 0    !Z decay into b bbar', 
            'MDME( 179,1) = 0    !Z decay into t tbar', 
            'MDME( 182,1) = 1    ! Z decay into e- e+',
            'MDME( 183,1) = 0    !Z decay into nu_e nu_ebar', 
            'MDME( 184,1) = 1    ! Z decay into mu- mu+',
            'MDME( 185,1) = 0    !Z decay into nu_mu nu_mubar',
            'MDME( 186,1) = 1    ! Z decay into tau- tau+',
            'MDME( 187,1) = 0    !Z decay into nu_tau nu_taubar',
            
            # Higgs boson decays
            
            'MDME(210,1)=0    ! Higgs decay into dd',
            'MDME(211,1)=0    ! Higgs decay into uu',
            'MDME(212,1)=0    ! Higgs decay into ss',
            'MDME(213,1)=0    ! Higgs decay into cc',
            'MDME(214,1)=0    ! Higgs decay into bb',
            'MDME(215,1)=0    ! Higgs decay into tt',
            'MDME(216,1)=0    ! Higgs decay into bbbar prime',
            'MDME(217,1)=0    ! Higgs decay into ttbar prime',
            'MDME(218,1)=0    ! Higgs decay into e- e+', 
            'MDME(219,1)=1    ! Higgs decay into mu- mu+', 
            'MDME(220,1)=0    ! Higgs decay into tau- tau+',
            'MDME(221,1)=0    ! Higgs decay into tau tau prime',
            'MDME(222,1)=0    ! Higgs decay into g g',
            'MDME(223,1)=0    ! Higgs decay into gam gam',
            'MDME(224,1)=0    ! Higgs decay into gam Z',
            'MDME(225,1)=0    ! Higgs decay into Z Z',
            'MDME(226,1)=0    ! Higgs decay into W W'
        ),                            
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring(
            'pythiaUESettings', 
            'processParameters')
    )
)

