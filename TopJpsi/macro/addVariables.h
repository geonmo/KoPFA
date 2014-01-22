void addTopVariables(TopAnalyzerLite* analyzer){
  analyzer->addMonitorPlot("JPsiMass", "JPsiMass", "JPsi Mass;J/#psi mass [GeV];Events/(0.01 GeV)", 20, 3.0, 3.2, 0.0, 0.02, false); //1
  analyzer->addMonitorPlot("ssJPsiMass", "ssJPsiMass", "SS JPsi Mass;mass_{#mu^{#pm}#mu^{#pm}} [GeV];Events/(2 GeV)", 50, 0, 100, 0.0, 0.02, false); //2
  analyzer->addMonitorPlot("JPsiMassFit", "JPsiMass", "JPsi Mass;J/#psi mass [GeV];Events/(0.01 GeV)", 60, 2.8, 3.4, 0.0, 0.02, false); //3
  analyzer->addMonitorPlot("JPsiPt", "JPsiPt", "JPsi p_{T};J/#psi p_{T} [GeV];Events/(5 GeV)", 28, 0.0, 140, 0.0, 0.02, false); //4
  analyzer->addMonitorPlot("JPsiEta", "JPsiEta", "JPsi #eta;J/#psi #eta ;Events/0.2", 25, -2.5, 2.5, 0.1, 100000); //5
  analyzer->addMonitorPlot("JPsiMassFull", "JPsiMass", "JPsi Mass;J/#psi mass [GeV];Events/(0.01 GeV)", 1000, 0.0, 10.0, 0.0, 0.01, false); //6
  analyzer->addMonitorPlot("JPsiMassFull02", "JPsiMass", "JPsi Mass;J/#psi mass [GeV];Events/(0.2 GeV)", 35, 0.0, 7.0, 0.0, 0.01, false); //7
  analyzer->addMonitorPlot("JPsiMassFulllog", "JPsiMass", "JPsi Mass;J/#psi mass [GeV];Events/(0.1 GeV)", 70, 0.0, 7.0, 0.0, 6);
  analyzer->addMonitorPlot("JPsidlPV", "JPsidlPV", "JPsidlPV;3D distance PV-J/#psi vertex [cm];Events/(0.1 cm)", 22, 0.0, 2.2, 0.0, 0.02,false); //8
  analyzer->addMonitorPlot("JPsidlErrPV", "JPsidlErrPV", "JPsi L/sigma;3D distance PV-J/#psi vertex/#sigma [cm];Events/0.1", 50, 0.0, 5, 0.0, 0.02,false); //9
  analyzer->addMonitorPlot("JPsidlPVZoom", "JPsidlPV", "JPsidlPV;3D distance PV-J/#psi vertex [cm];Events/0.01", 10, 0.0, 0.1, 0.0, 0.02,false); //10
  analyzer->addMonitorPlot("JPsiJetMinDR", "JPsiJetMinDR", "JPsiJetMinDR;#Delta R(J/#psi-jet) min;Events/0.05", 20, 0.0, 1, 0.0, 0.02,false); //11
  analyzer->addMonitorPlot("JPsiJetMinDPhi", "JPsiJetMinMinDPhi", "JPsiJetMinMinDPhi;#Delta #phi(J/#psi-jet) min;Events/0.05", 20, 0.0, 1.0, 0.0, 0.02,false);
  analyzer->addMonitorPlot("JPsiJetMinPtFrac", "JPsiJetMinPtFrac", "JPsiJetMinPtFrac;(p_{T}(nearest jet)-p_{T}(J/#psi))/p_{T}(nearest jet);Events/0.05", 22, 0.0, 1.1, 0.0, 0.02,false); //12
  analyzer->addMonitorPlot("JPsiJetJPsiPtFrac", "JPsiJetJPsiPtFrac", "JPsiJetJPsiPtFrac;p_{T}(J/#psi)/p_{T}(nearest jet);Events/0.05", 20, 0.0, 1, 0.0, 0.02,false); //13
  analyzer->addMonitorPlot("JPsiJetJPsiPtFrac01", "JPsiJetJPsiPtFrac", "JPsiJetJPsiPtFrac;p_{T}(J/#psi)/p_{T}(nearest jet);Events/0.1", 10, 0.0, 1, 0.0, 0.02,false); //13
  analyzer->addMonitorPlot("lep3_pixlayers", "lep3_pixlayers", "lep3_pixlayers;leading lepton pixel layers;Events/1", 7, 0.0, 7, 0.0, 0.02,false); //14
  analyzer->addMonitorPlot("lep4_pixlayers", "lep4_pixlayers", "lep4_pixlayers;second lepton pixel layers;Events/1", 7, 0.0, 7, 0.0, 0.02,false); //15
  analyzer->addMonitorPlot("JPsivProb", "JPsivProb", "JPsivProb;J/#psi vertex prob.;Events/0.1", 10, 0.0, 1, 0.0, 0.02,false); //16
  analyzer->addMonitorPlot("LepJPsiMass1", "LepJPsiMass1", "Leading lep+JPsi Mass; M_{l+J/#psi} (GeV/c^{2});Events/10.0 GeV/c^{2}", 20, 0, 200, 0.0, 0.02, false);
  analyzer->addMonitorPlot("LepJPsiMass1log", "LepJPsiMass1", "Leading lep+JPsi Mass; M_{l+J/#psi} (GeV/c^{2});Events/5 GeV/c^{2}", 40, 0, 200, 0.0, 6);
  analyzer->addMonitorPlot("LepJPsiMass2", "LepJPsiMass2", "Second leading lep+JPsi Mass; M_{l+J/#psi} (GeV/c^{2});Events/10.0 GeV/c^{2}", 20, 0, 200, 0.0, 0.02, false);
  analyzer->addMonitorPlot("LepJPsiMass2log", "LepJPsiMass2", "Second leading lep+JPsi Mass; M_{l+J/#psi} (GeV/c^{2});Events/5 GeV/c^{2}", 40, 0, 200, 0.0, 6);
  analyzer->addMonitorPlot("LepJPsidPhilower", "LepJPsidPhilower", "#Delta #phi(J/#psi-isolated lepton);#Delta #phi(J/#psi-isolated lepton) min;Events/0.2", 20, 0, 4, 0.0, 0.02,false);
  analyzer->addMonitorPlot("LepJPsidPhibigger", "LepJPsidPhibigger", "#Delta #phi(J/#psi-isolated lepton);#Delta #phi(J/#psi-isolated lepton) max;Events/0.2", 20, 0, 4, 0.0, 0.02,false);
  analyzer->addMonitorPlot("LepJPsidRlower", "LepJPsidRlower", "#Delta R(J/#psi-isolated lepton);#Delta R(J/#psi-isolated lepton) min;Events/0.2", 20, 0, 4, 0.0, 0.02,false);
  analyzer->addMonitorPlot("LepJPsidRbigger", "LepJPsidRbigger", "#Delta R(J/#psi-isolated lepton);#Delta R(J/#psi-isolated lepton) max;Events/0.2", 20, 0, 4, 0.0, 0.02,false);
  analyzer->addMonitorPlot("LepJPsidthetalower", "LepJPsidthetalower", "#Delta #theta(J/#psi-isolated lepton);#Delta #theta(J/#psi-isolated lepton) min;Events/0.2", 20, 0, 4, 0.0, 0.02,false);
  analyzer->addMonitorPlot("LepJPsidthetabigger", "LepJPsidthetabigger", "#Delta #theta(J/#psi-isolated lepton);#Delta #theta(J/#psi-isolated lepton) max;Events/0.2", 20, 0, 4, 0.0, 0.02,false);
  analyzer->addMonitorPlot("ZMass", "ZMass", "Dilepton mass;Dilepton mass (GeV/c^{2});Events/5 GeV/c^{2}", 40, 0, 250, 0.1, 1500);
  analyzer->addMonitorPlot("ZMassFinal", "ZMass", "Dilepton mass;Dilepton mass (GeV/c^{2});Events/40 GeV/c^{2}", 5, 0, 250, 0.1, 1500);

  analyzer->addMonitorPlot("nJetlog", "nJet30", "Jet Multiplicity;Jet Multiplicity;Events", 10, 0, 10, 0.05, 20000);
  analyzer->addMonitorPlot("nVertexlog", "nvertex", "Vertex Multiplicity;Vertex Multiplicity;Events", 25, 0, 25, 0.05, 5000);
  analyzer->addMonitorPlot("nVertex", "nvertex", "Vertex Multiplicity;Vertex Multiplicity;Events", 15, 0, 30, 0, 1,false);
  analyzer->addMonitorPlot("METlog", "MET", "Missing E_{T};Missing E_{T} (GeV);Events", 18, 0, 180, 0.1, 5000);
  analyzer->addMonitorPlot("nJet", "nJet30", "Jet Multiplicity;Jet Multiplicity(p_{T}>30 GeV/c);Events/1.0", 10, 0, 10, 0.1, 0.05,false);
  analyzer->addMonitorPlot("nJetlog5", "nJet30", "Jet Multiplicity;Jet Multiplicity;Events", 10, 0, 10, 0.1, 0.05);
  analyzer->addMonitorPlot("MET", "MET", "Missing E_{T};Missing E_{T} (GeV);Events", 18, 0, 180, 0.1, 1.5, false);
  analyzer->addMonitorPlot("METQCD", "MET", "Missing E_{T};Missing E_{T} (GeV);Events", 18, 0, 180, 0.1, 150.0, false);

  analyzer->addMonitorPlot("pt1", "lep1_pt", "Leading lepton p_{T};p_{T} (GeV/c);Events/10.0 GeV/c", 25, 0, 250, 0.1, 20000);
  analyzer->addMonitorPlot("pt2", "lep2_pt", "Second leading lepton p_{T};p_{T} (GeV/c);Events/10.0 GeV/c", 25, 0, 250, 0.1, 20000);
  analyzer->addMonitorPlot("pt3", "lep3_pt", "JPsi leading lepton p_{T};p_{T} (GeV/c);Events/10.0 GeV/c", 250, 0, 250, 0.1, 20000);
  analyzer->addMonitorPlot("pt4", "lep4_pt", "JPsi second leading lepton p_{T};p_{T} (GeV/c);Events/10.0 GeV/c", 250, 0, 250, 0.1, 20000);
  analyzer->addMonitorPlot("eta1", "lep1_eta", "Leading lepton #eta;#eta;Events/0.2", 35, -3.5, 3.5, 0.1, 100000);
  analyzer->addMonitorPlot("eta2", "lep2_eta", "Second leading lepton #eta;#eta;Events/0.2", 35, -3.5, 3.5, 0.1, 100000);
  analyzer->addMonitorPlot("eta3", "lep3_eta", "JPsi leading lepton #eta;#eta;Events/0.2", 35, -3.5, 3.5, 0.1, 100000);
  analyzer->addMonitorPlot("eta4", "lep4_eta", "JPsi second leading lepton #eta;#eta;Events/0.2", 35, -3.5, 3.5, 0.1, 100000);

  analyzer->addMonitorPlot("jetspt30", "jets_pt", "jet p_{T}(p_{T}>30 GeV/c);p_{T} (GeV/c);Events/20.0 GeV/c",20, 0.0, 400, 0.1, 100000);
  analyzer->addMonitorPlot("jet1pt30", "jets_pt[0]", "Leading jet p_{T};p_{T} (GeV/c);Events/10 GeV/c",48, 20, 500, 0.1, 100000);
  analyzer->addMonitorPlot("jet1eta30", "jets_eta[0]", "Leading jet #eta;#eta;Events/0.2", 35, -3.5, 3.5, 0.1, 100000);
  analyzer->addMonitorPlot("jet1phi30", "jets_phi[0]", "Leading jet #phi;#phi (Radian);Events/0.2 rad.", 35, -3.5, 3.5, 0.1, 100000);

  analyzer->addMonitorPlot("jet2pt30", "jets_pt[1]", "Second leading jet p_{T};p_{T} (GeV/c);Events/10 GeV/c",48, 20, 500, 0.1, 100000);
  analyzer->addMonitorPlot("jet2eta30", "jets_eta[1]", "Second leading jet #eta;#eta;Events/0.2", 35, -3.5, 3.5, 0.1, 100000);
  analyzer->addMonitorPlot("jet2phi30", "jets_phi[1]", "Second leading jet #phi;#phi (Radian);Events/0.2 rad.", 35, -3.5, 3.5, 0.1, 100000);

  analyzer->addMonitorPlot("jet3pt30", "jets_pt[2]", "Third jet p_{T};p_{T} (GeV/c);Events/10 GeV/c",48, 20, 500, 0.1, 100000);
  analyzer->addMonitorPlot("jet3eta30", "jets_eta[2]", "Third jet #eta;#eta;Events/0.2", 35, -3.5, 3.5, 0.1, 100000);
  analyzer->addMonitorPlot("jet3phi30", "jets_phi[2]", "Third jet #phi;#phi (Radian);Events/0.2 rad.", 35, -3.5, 3.5, 0.1, 100000);

  analyzer->addMonitorPlot("jet4pt30", "jets_pt[3]", "Fourth jet p_{T};p_{T} (GeV/c);Events/10 GeV/c",48, 20, 500, 0.1, 100000);
  analyzer->addMonitorPlot("jet4eta30", "jets_eta[3]", "Fourth jet #eta;#eta;Events/0.2", 35, -3.5, 3.5, 0.1, 100000);
  analyzer->addMonitorPlot("jet4phi30", "jets_phi[3]", "Fourth jet #phi;#phi (Radian);Events/0.2 rad.", 35, -3.5, 3.5, 0.1, 100000);

  analyzer->addMonitorPlot("Iso03lep1","lep1_relIso03","lep1 relIso;relIso;Events/0.02", 10, 0, 0.2, 0.1, 20000);
  analyzer->addMonitorPlot("Iso03lep2","lep2_relIso03","lep2 relIso;relIso;Events/0.02", 10, 0, 0.2, 0.1, 20000);

  analyzer->addMonitorPlot("nbJet30_CSVL", "nbjets30_CSVL", "b-Jet Multiplicity;b-Jet Multiplicity (CSVL);Events", 5, 0, 5, 0.1, 1,true);
  analyzer->addMonitorPlot("nbJet30_CSVM", "nbjets30_CSVM", "b-Jet Multiplicity;b-Jet Multiplicity (CSVM);Events", 5, 0, 5, 0.1, 1,true);
  analyzer->addMonitorPlot("nbJet30_CSVT", "nbjets30_CSVT", "b-Jet Multiplicity;b-Jet Multiplicity (CSVT);Events", 5, 0, 5, 0.1, 1,true);
  analyzer->addMonitorPlot("nbJet30_CSVL1", "nbjets30_CSVL", "b-Jet Multiplicity;b-Jet Multiplicity (CSVL);Events", 5, 0, 5, 0.1, 10,true);
  analyzer->addMonitorPlot("nbJet30_CSVM1", "nbjets30_CSVM", "b-Jet Multiplicity;b-Jet Multiplicity (CSVM);Events", 5, 0, 5, 0.1, 10,true);
  analyzer->addMonitorPlot("nbJet30_CSVT1", "nbjets30_CSVT", "b-Jet Multiplicity;b-Jet Multiplicity (CSVT);Events", 5, 0, 5, 0.1, 10,true);
  analyzer->addMonitorPlot("nbJet30_JPM", "nbjets30_JPM", "b-Jet Multiplicity;b-Jet Multiplicity (JPM);Events", 5, 0, 5, 0.1, 10,true);
  analyzer->addMonitorPlot("nbJet30_JPT", "nbjets30_JPT", "b-Jet Multiplicity;b-Jet Multiplicity (JPT);Events", 5, 0, 5, 0.1, 10,true);

  analyzer->addMonitorPlot("addjet1_bDisCSV", "jets_bDiscriminatorCSV[csvd_jetid[2]]","b-Discriminator; b-Discriminator (CSV);Events/0.1", 10, 0.0, 1.0, 0.1,10,true);
  analyzer->addMonitorPlot("addjet2_bDisCSV", "jets_bDiscriminatorCSV[csvd_jetid[3]]","b-Discriminator; b-Discriminator (CSV);Events/0.1", 10, 0.0, 1.0, 0.1,10,true);
 
  analyzer->addMonitorPlot("addjet1_bDisJP", "jets_bDiscriminatorJP[jpd_jetid[2]]", "b-Discriminator; b-Discriminator (JP);Events", 30, 0.0, 1.5, 0.1, 10,true);
  analyzer->addMonitorPlot("addjet2_bDisJP", "jets_bDiscriminatorJP[jpd_jetid[3]]", "b-Discriminator; b-Discriminator (JP);Events", 30, 0.0, 1.5, 0.1, 10,true);

  analyzer->addMonitorPlot("addjet1_secvtxm", "jets_secvtxmass[csvd_jetid[2]]", "Secondary Vertex Mass;Secondary Vertex Mass (GeV);Events", 10, 0.0, 5.0, 0.1, 10,true);
  analyzer->addMonitorPlot("addjet2_secvtxm", "jets_secvtxmass[csvd_jetid[3]]", "Secondary Vertex Mass;Secondary Vertex Mass (GeV);Events", 10, 0.0, 5.0, 0.1, 10,true);

//  analyzer->addMonitorPlot("nJPsivsVtx", "jets_secvtxmass[csvd_jetid[3]]", "Secondary Vertex Mass;Secondary Vertex Mass (GeV);Events", 10, 0.0, 5.0, 0.1, 10,true);
  analyzer->addMonitorPlot("nJPsiCand", "nJPsiCand", "N of JPsi1;N;Events", 11, 0.0, 11.0, 0.1, 10,true);
  analyzer->addMonitorPlot("nLepJPsiCand1", "nLepJPsiCand1", "N of LepJPsi1;N;Events", 11, 0.0, 11.0, 0.1, 10,true);
  analyzer->addMonitorPlot("nLepJPsiCand2", "nLepJPsiCand2", "N of LepJPsi2;N;Events", 11, 0.0, 11.0, 0.1, 10,true);

}
