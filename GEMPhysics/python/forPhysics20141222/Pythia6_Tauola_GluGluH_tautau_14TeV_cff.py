import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

# Z2star tune with pT-ordered showers
from Configuration.Generator.PythiaUEZ2starSettings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         maxEventsToPrint = cms.untracked.int32(0),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.),
                         crossSection = cms.untracked.double(1.4),
                         comEnergy = cms.double(14000.0),

                         ExternalDecays = cms.PSet(
                               Tauola = cms.untracked.PSet(
                                   TauolaPolar,
                                   TauolaDefaultInputCards
                                   #InputCards = cms.PSet(
	                            #    pjak1 = cms.int32(0),
	                             #   pjak2 = cms.int32(0),
	                             #   mdtau = cms.int32(230)
	                            #)
                                ),
                                parameterSets = cms.vstring('Tauola')
                          ),
                         
                         UseExternalGenerators = cms.untracked.bool(True),
                         PythiaParameters = cms.PSet(
                             pythiaUESettingsBlock, 
                             processParameters = cms.vstring(
                                'MSEL      = 0      ! User defined processes',
                                'MSUB(102)  = 1      ! gg->H (SM)',
                                
                                'PMAS(25,1)= 125.   ! m_H',
                                'PMAS(5,1) = 4.75   ! b quark mass', 
                                'PMAS(6,1) = 173.3  ! t quark mass',
                                'PMAS(23,1)= 91.187 ! mass of Z',
                                'PMAS(24,1)= 80.39  ! mass of W',
            
                                'MDME(210,1)=0    ! Higgs decay into dd',
                                'MDME(211,1)=0    ! Higgs decay into uu',
                                'MDME(212,1)=0    ! Higgs decay into ss',
                                'MDME(213,1)=0    ! Higgs decay into cc',
                                'MDME(214,1)=0    ! Higgs decay into bb',
                                'MDME(215,1)=0    ! Higgs decay into tt',
                                'MDME(216,1)=0    ! Higgs decay into bbbar prime',
                                'MDME(217,1)=0    ! Higgs decay into ttbar prime',
                                'MDME(218,1)=0    ! Higgs decay into e e',
                                'MDME(219,1)=0    ! Higgs decay into mu mu',
                                'MDME(220,1)=1    ! Higgs decay into tau tau',
                                'MDME(221,1)=0    ! Higgs decay into tau tau prime',
                                'MDME(222,1)=0    ! Higgs decay into g g',
                                'MDME(223,1)=0    ! Higgs decay into gam gam',
                                'MDME(224,1)=0    ! Higgs decay into gam Z',
                                'MDME(225,1)=0    ! Higgs decay into Z Z',
                                'MDME(226,1)=0    ! Higgs decay into W W'
            ),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
        )
    )

