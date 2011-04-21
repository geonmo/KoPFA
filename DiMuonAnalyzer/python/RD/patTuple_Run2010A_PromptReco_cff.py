
import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
		     noEventSort = cms.untracked.bool(True),
		     duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
		     fileNames = readFiles
                    )
readFiles.extend([
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_100_0_5j3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_101_0_BGp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_102_0_8Id.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_103_0_HFX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_104_0_A0C.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_105_0_RMN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_106_0_zML.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_107_0_5gk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_108_0_S15.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_109_0_4qE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_10_0_j1q.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_110_0_yBQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_111_0_29o.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_112_0_5jq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_113_0_wBd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_114_0_89n.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_115_0_58J.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_116_0_sOS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_117_0_sMh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_118_0_jmw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_119_0_nQS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_11_0_oO3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_120_0_z9N.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_121_0_DGT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_122_0_ESk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_123_0_TQv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_124_0_UpN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_125_0_VRD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_126_0_DV6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_127_0_bEV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_128_0_9eG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_129_0_gyC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_12_0_Lvr.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_130_0_3Vd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_131_0_7Ox.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_132_0_DGD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_133_0_CQU.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_134_0_qdf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_135_0_qsJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_136_0_Qkz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_137_0_Ng5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_138_0_4uh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_139_0_T17.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_13_0_l99.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_140_0_CV4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_141_0_MOl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_142_0_BZS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_143_0_gUV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_144_0_yOW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_145_0_Ctj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_146_0_jxm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_148_0_Zt7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_149_0_O8U.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_14_0_Hhm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_150_0_RYW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_151_0_3nm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_152_0_beS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_153_0_ml4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_154_0_T2Q.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_155_0_45Q.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_156_0_3X8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_157_0_Buw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_158_0_i8p.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_159_0_nLC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_15_0_z4K.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_160_0_6yN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_161_0_5g7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_162_0_qMX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_163_0_WzI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_164_0_yqX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_166_0_0ux.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_167_0_5pv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_168_0_lH4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_169_0_N5B.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_16_0_kIj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_170_0_cLg.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_171_0_BX3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_172_0_9KX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_173_0_dJz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_174_0_xP6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_175_0_Rl0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_176_0_fbh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_177_0_Nwk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_178_0_f1j.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_179_0_Wce.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_17_0_OHR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_180_0_OkM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_181_0_ehq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_182_0_cZf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_183_0_yK0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_184_0_O37.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_185_0_3pL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_186_0_EVj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_187_0_PT7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_188_0_AJ4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_189_0_MQ6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_18_0_4lG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_190_0_agJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_191_0_Yc1.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_192_0_paa.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_193_0_d82.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_194_0_na3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_195_0_IfF.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_196_0_LDI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_197_0_CEK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_198_0_hBe.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_199_0_w0I.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_19_0_NPe.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_1_1_tZS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_200_0_EgJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_201_0_EJr.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_202_0_pdN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_203_0_Ep0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_204_0_KPt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_205_0_J4V.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_206_0_DBH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_207_0_fft.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_208_0_T7S.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_209_0_HBU.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_20_0_rFf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_210_0_kVJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_211_0_ugK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_212_0_Npw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_213_0_3bZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_214_0_wT5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_215_0_3UF.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_216_0_pnU.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_217_0_lDd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_218_0_E3E.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_219_0_1Ae.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_21_0_Ljn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_220_0_tfy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_221_0_FtV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_222_0_BT1.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_223_0_yZ5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_224_0_DHx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_225_0_2Yh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_226_0_PSC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_227_0_Ocb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_228_0_g2X.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_229_0_KuQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_22_0_0Cp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_230_0_KtQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_231_0_SZW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_232_0_2me.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_233_0_PJu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_234_0_i4K.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_235_0_Iac.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_236_0_7wn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_237_0_XLV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_238_0_1ut.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_239_0_V7W.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_23_0_PnN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_240_0_nKY.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_241_0_eJ3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_242_0_Rbu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_243_0_Llt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_244_0_41c.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_245_0_l7u.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_246_0_trp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_247_0_5If.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_248_0_L7g.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_249_0_U8U.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_24_0_SaG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_250_0_v2H.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_251_0_dYQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_252_0_YKq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_253_0_6qs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_254_0_Odu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_255_0_Mgv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_256_0_oCj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_257_0_vrp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_258_0_Otn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_259_0_JRk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_25_0_LSh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_260_0_Zw1.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_261_0_CZt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_262_0_J2X.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_263_0_Pck.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_264_0_B9i.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_265_0_5of.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_266_0_XWt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_267_0_EBN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_268_0_3DQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_269_0_OgS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_26_0_kGW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_270_0_U3M.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_271_0_CjB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_272_0_H9G.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_273_0_Vml.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_274_0_4L7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_275_0_WXR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_276_0_M2K.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_277_0_DHA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_278_0_tbK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_279_0_aXN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_27_0_YzT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_280_0_Lcy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_281_0_hjT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_282_0_DHR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_283_0_nHp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_284_0_pw5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_285_0_afC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_286_0_7mc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_287_0_4kn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_288_0_Cj3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_289_0_NKo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_28_0_JLN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_290_0_bSq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_291_0_KUA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_292_0_sDl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_293_0_cCb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_294_0_icP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_295_0_dvd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_297_0_I1f.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_298_0_rYv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_299_0_ouv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_29_0_oTx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_2_1_D15.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_300_0_bMP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_301_0_11N.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_302_0_xhm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_303_0_fZy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_304_0_2XA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_305_0_2nk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_306_0_Z2A.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_307_0_vxJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_308_0_onv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_309_0_QA8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_30_0_vE5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_310_0_lCW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_311_0_Fx6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_312_0_o2n.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_313_0_VUa.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_31_0_v3O.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_32_0_u8M.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_33_0_z9A.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_34_0_QaQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_35_0_xcv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_36_0_7Rr.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_37_0_ma0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_38_0_DMD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_39_0_EBY.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_3_1_8zo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_40_0_o07.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_41_0_wvC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_42_0_BOn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_43_0_LDO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_44_0_PHu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_45_0_jo6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_46_0_CYb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_47_0_IlC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_48_0_FyT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_49_0_6FN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_4_0_0t2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_50_0_wet.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_51_0_4jD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_52_0_pkN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_53_0_lrW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_54_0_CGD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_55_0_xVL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_56_0_PDS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_57_0_y8X.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_58_0_kqu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_59_0_ql8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_5_0_A33.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_60_0_piW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_61_0_k9Q.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_62_0_bBN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_63_0_yV5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_64_0_i28.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_65_0_M88.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_66_0_Zli.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_67_0_Sld.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_68_0_Tj4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_69_0_9nc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_6_0_DMm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_70_0_arZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_71_0_BTm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_72_0_L2h.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_73_0_36l.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_74_0_7Sl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_75_0_zoL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_76_0_oi1.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_77_0_hQk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_78_0_TzC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_79_0_yff.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_7_0_r0S.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_80_0_Xnd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_81_0_MSN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_82_0_fX9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_83_0_BP9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_84_0_E1j.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_85_0_EHR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_86_0_XUY.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_87_0_bAd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_88_0_ETW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_89_0_WbS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_8_0_djR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_90_0_LD8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_91_0_G4p.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_92_0_JGz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_93_0_Y6g.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_94_0_3vS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_95_0_REx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_96_0_dW5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_97_0_mwL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_98_0_tHn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_99_0_A6F.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Sep3/Run2010A-PromptReco-v4/patTuple_muon_9_0_7vB.root',
]
        )