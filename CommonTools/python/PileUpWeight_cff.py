import FWCore.ParameterSet.Config as cms

PileUpRD2011A = cms.vdouble(
    1.29654e+07,
    5.58514e+07,
    1.29329e+08,
    2.12134e+08,
    2.76138e+08,
    3.03604e+08,
    2.93258e+08,
    2.55633e+08,
    2.0497e+08,
    1.53264e+08,
    1.07936e+08,
    7.21006e+07,
    4.5913e+07,
    2.797e+07,
    1.63426e+07,
    9.17598e+06,
    4.95861e+06,
    2.58239e+06,
    1.2977e+06,
    629975,
    295784,
    134470,
    59260.1,
    25343.9,
    10530.1,
    4255.05,
    1673.95,
    641.776,
    240.022,
    87.6504,
    31.281,
    10.9195,
    3.73146,
    1.24923,
    0.602368,
)

PileUpRD2011 = cms.vdouble(
    1.33292e+07,
    5.82902e+07,
    1.38195e+08,
    2.34756e+08,
    3.21463e+08,
    3.79604e+08,
    4.04376e+08,
    4.01352e+08,
    3.79854e+08,
    3.48163e+08,
    3.11793e+08,
    2.73789e+08,
    2.35748e+08,
    1.98694e+08,
    1.63533e+08,
    1.31152e+08,
    1.02327e+08,
    7.75916e+07,
    5.71533e+07,
    4.08939e+07,
    2.84315e+07,
    1.92177e+07,
    1.2638e+07,
    8.09273e+06,
    5.05059e+06,
    3.07491e+06,
    1.82803e+06,
    1.06222e+06,
    603854,
    336150,
    183399,
    98148.8,
    51561.9,
    26609.6,
    26557.3,
)

# Flat10+Tail distribution taken directly from MixingModule input:  (Can be used for Spring11 and Summer11 if you don't worry about small shifts in the mean)

probdistFlat10 = cms.vdouble(
    0.0698146584,
    0.0698146584,
    0.0698146584,
    0.0698146584,
    0.0698146584,
    0.0698146584,
    0.0698146584,
    0.0698146584,
    0.0698146584,
    0.0698146584,
    0.0698146584,
    0.0630151648,
    0.0526654164,
    0.0402754482,
    0.0292988928,
    0.0194384503,
    0.0122016783,
    0.007207042,
    0.004003637,
    0.0020278322,
    0.0010739954,
    0.0004595759,
    0.0002229748,
    0.0001028162,
    4.58337152809607E-05
)
 
# Summer11 PU_S4, distribution obtained by averaging the number of interactions
# in each beam crossing to estimate the true mean.  

PoissonIntDist = cms.vdouble(
    0.104109,
    0.0703573,
    0.0698445,
    0.0698254,
    0.0697054,
    0.0697907,
    0.0696751,
    0.0694486,
    0.0680332,
    0.0651044,
    0.0598036,
    0.0527395,
    0.0439513,
    0.0352202,
    0.0266714,
    0.019411,
    0.0133974,
    0.00898536,
    0.0057516,
    0.00351493,
    0.00212087,
    0.00122891,
    0.00070592,
    0.000384744,
    0.000219377
)

# Summer11 PU_S4, distribution obtained by only looking at the in-time crossing.
# THIS IS THE RECOMMENDED ONE for reweighting.
PoissonOneXDist = cms.vdouble(
    1.45346E-01,
    6.42802E-02,
    6.95255E-02,
    6.96747E-02,
    6.92955E-02,
    6.84997E-02,
    6.69528E-02,
    6.45515E-02,
    6.09865E-02,
    5.63323E-02,
    5.07322E-02,
    4.44681E-02,
    3.79205E-02,
    3.15131E-02,
    2.54220E-02,
    2.00184E-02,
    1.53776E-02,
    1.15387E-02,
    8.47608E-03,
    6.08715E-03,
    4.28255E-03,
    2.97185E-03,
    2.01918E-03,
    1.34490E-03,
    8.81587E-04,
    5.69954E-04,
    3.61493E-04,
    2.28692E-04,
    1.40791E-04,
    8.44606E-05,
    5.10204E-05,
    3.07802E-05,
    1.81401E-05,
    1.00201E-05,
    5.80004E-06
)
