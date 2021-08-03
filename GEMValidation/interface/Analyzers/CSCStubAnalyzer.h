#ifndef GEMCode_GEMValidation_CSCStubAnalyzer_h
#define GEMCode_GEMValidation_CSCStubAnalyzer_h

#include "GEMCode/GEMValidation/interface/Helpers.h"
#include "GEMCode/GEMValidation/interface/MatcherSuperManager.h"
#include "GEMCode/GEMValidation/interface/TreeManager.h"

class CSCStubAnalyzer
{
public:

  // constructor
  CSCStubAnalyzer(const edm::ParameterSet& conf, edm::ConsumesCollector&& iC);

  // destructor
  ~CSCStubAnalyzer() {}

  void init(const edm::Event& iEvent, const edm::EventSetup& iSetup);

  void setMatcher(const CSCStubMatcher& match_sh);

  // initialize the event
  void analyze(const edm::Event& ev, const edm::EventSetup& es, const MatcherSuperManager& manager, my::TreeManager& tree);
  void analyze(TreeManager& tree);

 private:

  edm::EDGetTokenT<CSCCLCTDigiCollection> clctToken_;
  edm::EDGetTokenT<CSCALCTDigiCollection> alctToken_;
  edm::EDGetTokenT<CSCCorrelatedLCTDigiCollection> lctToken_;
  edm::EDGetTokenT<CSCCorrelatedLCTDigiCollection> mplctToken_;

  edm::Handle<CSCCLCTDigiCollection> clctsH_;
  edm::Handle<CSCALCTDigiCollection> alctsH_;
  edm::Handle<CSCCorrelatedLCTDigiCollection> lctsH_;
  edm::Handle<CSCCorrelatedLCTDigiCollection> mplctsH_;

  bool verboseALCT_;
  bool verboseCLCT_;
  bool verboseLCT_;
  bool verboseMPLCT_;

  int minBXCLCT_, maxBXCLCT_;
  int minBXALCT_, maxBXALCT_;
  int minBXLCT_, maxBXLCT_;
  int minBXMPLCT_, maxBXMPLCT_;

  // best here means "closest in phi"
  std::pair<GEMDigi, GlobalPoint>
  bestGEMDigi(const GEMDetId& gemId,
              const GEMDigiContainer& gem_digis,
              const GlobalPoint& csc_gp) const;

  std::pair<GEMPadDigi, GlobalPoint>
  bestGEMPadDigi(const GEMDetId& gemId,
                 const GEMPadDigiContainer& gem_digis,
                 const GlobalPoint& csc_gp) const;

  std::pair<GEMCoPadDigi, GlobalPoint>
  bestGEMCoPadDigi(const GEMDetId& gemId,
                   const GEMCoPadDigiContainer& gem_digis,
                   const GlobalPoint& csc_gp) const;

  edm::ESHandle<CSCGeometry> csc_geom_;
  edm::ESHandle<GEMGeometry> gem_geom_;

  const CSCGeometry* cscGeometry_;
  const GEMGeometry* gemGeometry_;

  std::unique_ptr<CSCStubMatcher> match_;
  int minNHitsChamber_;
};

#endif
