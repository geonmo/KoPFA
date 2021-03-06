import FWCore.ParameterSet.Config as cms

source = cms.Source(
        "PoolSource",
        noEventSort = cms.untracked.bool(True),
        duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
        fileNames = cms.untracked.vstring()
)
source.fileNames.extend([
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_100_2_XSi.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_103_2_UvH.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_105_1_6jp.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_106_1_RJ1.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_108_1_eP2.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_10_1_38i.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_110_1_dd9.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_117_1_fi0.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_120_1_4LD.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_121_2_7Qr.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_123_1_DbX.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_126_1_G5K.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_127_1_y5n.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_130_1_U2k.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_131_1_vSx.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_132_1_nzy.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_133_1_sLg.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_134_1_r4m.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_141_1_18m.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_145_1_rs9.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_146_1_KvR.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_14_1_bZd.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_15_2_K5h.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_160_1_UWR.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_16_1_dAF.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_171_1_4j9.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_172_1_nv6.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_175_1_W63.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_17_1_5UT.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_180_1_CCR.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_181_1_FHS.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_182_1_cdT.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_18_1_cuF.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_195_1_Iak.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_197_1_NDt.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_1_1_Tdz.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_20_1_vy5.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_211_2_S6M.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_216_2_rOk.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_219_2_nvY.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_21_1_lXn.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_22_1_54H.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_23_1_cG7.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_244_2_ptK.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_24_1_J04.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_258_2_NEg.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_25_1_P7P.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_260_2_zUj.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_261_2_tRM.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_275_2_LMN.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_278_2_rSh.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_27_1_9Z6.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_290_1_n43.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_292_1_9T3.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_29_1_IJH.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_2_1_wCG.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_304_2_wny.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_307_2_1is.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_30_1_JcG.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_31_1_m3V.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_324_1_xQ2.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_32_1_8Wn.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_333_2_w32.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_339_1_STI.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_33_1_tnC.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_340_1_5XA.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_341_1_QeH.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_342_1_O8s.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_343_1_j3M.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_346_1_mpJ.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_347_1_RDm.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_348_1_IqU.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_34_1_Oam.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_350_1_P8q.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_352_1_ut0.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_35_1_1bW.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_36_1_tcb.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_385_1_yCT.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_388_2_6Gi.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_38_2_36U.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_390_2_0qO.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_3_1_U0x.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_402_2_ON6.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_403_1_z0z.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_42_2_aAK.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_43_2_m6s.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_44_1_4fz.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_45_1_haU.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_46_1_V8C.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_47_1_390.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_48_1_xU2.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_49_1_oRz.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_4_1_BVA.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_50_1_284.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_51_1_Z5M.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_52_1_8Nk.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_53_2_8OM.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_56_2_W6R.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_57_1_4Pk.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_58_1_ItC.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_5_1_TJE.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_60_2_nLt.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_61_1_wXF.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_62_1_xpC.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_63_1_Zfo.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_67_2_RFp.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_6_1_8tt.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_70_2_zV2.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_73_2_pOK.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_75_2_oEO.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_76_2_QJZ.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_78_2_JFI.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_7_1_tsC.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_81_1_DcE.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_87_1_wWf.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_88_1_DgH.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_8_2_5xc.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_91_1_79N.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_93_1_2yy.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_94_2_Dln.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_95_1_ciZ.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_96_2_2wL.root',
      'rfio:/castor/cern.ch/user/j/jkim/TopPattupleP11/SemiLeptP11/patTuple_97_2_wkz.root',
])
