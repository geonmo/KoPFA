import FWCore.ParameterSet.Config as cms

source = cms.Source(
	"PoolSource",
	noEventSort = cms.untracked.bool(True),
	duplicateCheckMode = cms.untracked.string(noDuplicateCheck),
	fileNames = cms.untracked.vstring()
)
source.fileNames.extend([
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_0.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_1.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_2.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_3.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_4.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_5.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_6.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_7.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_8.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_9.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_10.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_11.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_12.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_13.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_14.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_15.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_16.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_17.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_18.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_19.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_20.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_21.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_22.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_23.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_24.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_25.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_26.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_27.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_28.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_29.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_30.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_31.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_32.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_33.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_34.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_35.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_36.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_37.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_38.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_39.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_40.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_41.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_42.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_43.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_44.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_45.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_46.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_47.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_48.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_49.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_50.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_51.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_52.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_53.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_54.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_55.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_56.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_57.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_58.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_59.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_60.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_61.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_62.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_63.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_64.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_65.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_66.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_67.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_68.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_69.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_70.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_71.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_72.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_73.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_74.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_75.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_76.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_77.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_78.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_79.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_80.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_81.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_82.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_83.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_84.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_85.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_86.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_87.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_88.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_89.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_90.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_91.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_92.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_93.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_94.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_95.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_96.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_97.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_98.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_99.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_100.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_101.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_102.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_103.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_104.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_105.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_106.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_107.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_108.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_109.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_110.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_111.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_112.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_113.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_114.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_115.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_116.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_117.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_118.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_119.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_120.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_121.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_122.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_123.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_124.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_125.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_126.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_127.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_128.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_129.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_130.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_131.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_132.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_133.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_134.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_135.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_136.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_137.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_138.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_139.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_140.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_141.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_142.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_143.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_144.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_145.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_146.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_147.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_148.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_149.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_150.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_151.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_152.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_153.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_154.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_155.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_156.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_157.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_158.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_159.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_160.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_161.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_162.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_163.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_164.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_165.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_166.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_167.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_168.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_169.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_170.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_171.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_172.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_173.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_174.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_175.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_176.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_177.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_178.root',
'/store/cmst3/user/cmgtools/CMG/MuEG/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_7_0/cmgTuple_179.root',
])
