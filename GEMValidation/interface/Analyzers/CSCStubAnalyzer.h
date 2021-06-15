#ifndef GEMCode_GEMValidation_CSCStubAnalyzer_h
#define GEMCode_GEMValidation_CSCStubAnalyzer_h

#include "GEMCode/GEMValidation/interface/Helpers.h"
#include "GEMCode/GEMValidation/interface/MatcherSuperManager.h"
#include "GEMCode/GEMValidation/interface/TreeManager.h"
#include "L1Trigger/CSCTriggerPrimitives/interface/CSCLUTReader.h"
#include "DataFormats/CSCDigi/interface/CSCCLCTPreTriggerDigiCollection.h"

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

  edm::EDGetTokenT<CSCCLCTPreTriggerDigiCollection> preclctToken_;
  edm::EDGetTokenT<CSCCLCTDigiCollection> clctToken_;
  edm::EDGetTokenT<CSCALCTDigiCollection> alctToken_;
  edm::EDGetTokenT<CSCCorrelatedLCTDigiCollection> lctToken_;
  edm::EDGetTokenT<CSCCorrelatedLCTDigiCollection> mplctToken_;
  edm::EDGetTokenT<CSCShowerDigiCollection> showerToken_;

  edm::Handle<CSCCLCTPreTriggerDigiCollection> preclctsH_;
  edm::Handle<CSCCLCTDigiCollection> clctsH_;
  edm::Handle<CSCALCTDigiCollection> alctsH_;
  edm::Handle<CSCCorrelatedLCTDigiCollection> lctsH_;
  edm::Handle<CSCCorrelatedLCTDigiCollection> mplctsH_;
  edm::Handle<CSCShowerDigiCollection> showersH_;

  bool verboseALCT_;
  bool verbosePreCLCT_;
  bool verboseCLCT_;
  bool verboseLCT_;
  bool verboseMPLCT_;
  bool verboseShower_;

  int minBXPreCLCT_, maxBXPreCLCT_;
  int minBXCLCT_, maxBXCLCT_;
  int minBXALCT_, maxBXALCT_;
  int minBXLCT_, maxBXLCT_;
  int minBXMPLCT_, maxBXMPLCT_;
  int minBXShower_, maxBXShower_;

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

  std::vector<std::string> positionLUTFiles_;
  std::vector<std::string> positionFloatLUTFiles_;
  std::vector<std::string> slopeLUTFiles_;
  std::vector<std::string> slopeFloatLUTFiles_;
  std::vector<std::string> patternConversionLUTFiles_;

  // unique pointers to the luts
  std::array<std::unique_ptr<CSCLUTReader>, 5> lutpos_;
  std::array<std::unique_ptr<CSCLUTReader>, 5> lutposfloat_;
  std::array<std::unique_ptr<CSCLUTReader>, 5> lutslope_;
  std::array<std::unique_ptr<CSCLUTReader>, 5> lutslopefloat_;
  std::array<std::unique_ptr<CSCLUTReader>, 5> lutpatconv_;
};

#endif
