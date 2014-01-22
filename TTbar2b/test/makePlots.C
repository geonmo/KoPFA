#ifndef __CINT__
#include "RooGlobalFunc.h"
#endif
#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooGaussian.h"
#include "RooChebychev.h"
#include "RooAddPdf.h"
#include "TCanvas.h"
#include "TAxis.h"
#include "RooPlot.h"
#include "RooFitResult.h"

using namespace RooFit ;

void cutStepPlots(const char* cutStep, const char* histName, const char* histTitle,
                  double minY, double maxY, bool doLogY);
TLegend* buildLegend();
TPaveText* getHeader(double lumi, TString channelName = "");

void makePlots(TString noteNumber = "Plots")
{
  //setTDRStyle();

  TString path = "TopMass_noLcut_PYMG";
  //TString path = "TopMass_Lcut002_PYMG";

 //jkim
    TFile *f1 =  new TFile("./All.root");
    TH1F *hmFit = (TH1F*)f1->Get("Step_5/hData_Step_5_JPsiMassFit");
    

    RooRealVar mass("mass","mass_{#mu^{+}#mu^{-}}(GeV/c^{2})",2.8,3.4) ;

    RooRealVar mean("mean","Gaussian mean",3.096,3.0,3.2) ;
    RooRealVar sigma1("sigma1","sigma1",0.017,0.01,0.024) ;
    RooRealVar sigma2("sigma2","width of gaussians",0.04) ;

    RooGaussian sig("sig","signal",mass,mean,sigma1);
    RooGaussian sig2("sig2","signal2",mass,mean,sigma2);

	//RooRealVar sig1frac("sig1frac","fraction of component 1 in signal",0.5,0.,1.) ;
	//RooAddPdf sig("sig","Signal",RooArgList(sig1,sig2),sig1frac) ;
    RooRealVar nsig("nsig","yield signal peak",100,0,1000);

    RooRealVar pol_c1("pol_c1", "slope of background", 0., -10., 10.);
    RooPolynomial pol("pol","polynomial",mass,RooArgList(pol_c1));
    RooRealVar nbkg("nbkg","yield of background",10,0,1000);
   
    //RooRealVar sigfrac("sigfrac","fraction of signal",0.5,0.,1.) ;
    //RooAddPdf sig("sig","Double Gaussian for signal",RooArgList(gauss1,gauss2),sigfrac);
    //RooRealVar bkgfrac("bkgfrac","fraction of background",0.9,0.,1.) ;

    //RooAddPdf  model("model","g+l",RooArgList(gauss,landau),sigfrac);
    //RooAddPdf  model("model","g1+g2",RooArgList(gauss1,gauss2),sigfrac);

    RooArgList shapes;
    RooArgList yields;
    shapes.add(pol);
    yields.add(nbkg);
    shapes.add(sig);
    yields.add(nsig);

    RooAddPdf model("model","g1+g2+pol",shapes,yields);
    RooDataHist dhdata("dhdata","dhdata",mass,Import(*hmFit)) ;

    RooFitResult* fitres = model.fitTo(dhdata,Extended()) ;

    RooPlot* frame = mass.frame(Title("J/#psi Mass")) ;
	frame->SetTitle("");
	frame->GetYaxis()->SetTitle("Events / 0.01 (GeV/c^{2} )"); 
    //RooPlot* frame = mass.frame(1.5,7) ;
    //frame->addTH1(hSigLLMG);
    //frame->addTH1(hSigLLPY);
    dhdata.plotOn(frame,DataError(RooAbsData::SumW2),XErrorSize(0)) ;
    //sig.plotOn(frame);
    model.plotOn(frame,LineColor(kRed)) ;
    model.plotOn(frame,Components(pol),LineColor(kBlue),LineStyle(kDashed)) ;
    model.plotOn(frame,Components(sig),LineColor(kBlue)) ;
    //model.paramOn(frame,dhdata);
    //dhdata.statOn(frame);

    TCanvas* c1 = new TCanvas("c1","Fitting of JPsi Mass",800,600) ;
    //TLegend* leg = buildLegend();
	//frame->addObject(leg);
    frame->addObject(getHeader(19.6, "ee/#mu#mu/e#mu"));
    frame->Draw();
    c1->Print("cLL_fitJpsi.pdf");
    c1->Print("cLL_fitJpsi.eps");
    c1->Print("cLL_fitJpsi.png");

    TFile *f2 =  new TFile("./ALL_noLcut/dimuonmass-2l1jpsi1jet.root");
    TCanvas* c2 = new TCanvas("c2","Dimuon mass in [0,10] GeV/c^{2}",1000,600) ;
    TH1F *hmassfull =  (TH1F*)f2->Get("hData_Step_4_JPsiMassFull");
    TH1F *h = new TH1F("h","",1000,0,10);
    for(int i=0;i<1000;i++) {
	//cout<<i<<" : "<<hmassfull->GetBinContent(i+1)<<endl;
	h->SetBinContent(i+1, hmassfull->GetBinContent(i+1));
    }
	gStyle->SetOptStat(0);
	h->GetXaxis()->SetTitle("mass_{#mu^{+}#mu^{-}}(GeV/c^{2})");
	h->GetYaxis()->SetTitle("Events / 0.04 (GeV/c^{2})");
    h->SetLineWidth(2);
   	h->Rebin(4);
	h->Draw();
	getHeader(19.6, "ee/#mu#mu/e#mu")->Draw();

	pt1 = new TPaveText(3.27478,28.1593,4.015056,29.62976,"br");
	pt1->SetBorderSize(0);
	pt1->SetFillColor(0);
	pt1->SetFillStyle(0);
	pt1->SetTextSize(0.035);
	pt1->AddText("J/#psi");
	pt1->Draw();

/*	pt2 = new TPaveText(3.493976,2.059615,4.083835,3.190843,"br");
	pt2->SetBorderSize(0);
	pt2->SetFillColor(0);
	pt2->SetFillStyle(0);
	pt2->SetTextSize(0.035);
	pt2->AddText("#psi'");
	pt2->Draw();*/

	c2->Modified();
	c2->Print("dimuonmass.pdf");
	c2->Print("dimuonmass.png");
	c2->Print("dimuonmass.eps");
	
}


TLegend* buildLegend()
{
  TLegend* leg = new TLegend(0.67,0.52,0.85,0.85,NULL,"brNDC");

  leg->SetBorderSize(1);
  leg->SetTextFont(62);
  leg->SetTextSize(0.04);
  leg->SetLineColor(0);
  leg->SetLineStyle(1);
  leg->SetLineWidth(1);
  leg->SetFillColor(0);
  leg->SetFillStyle(1001);

  return leg;
}

TPaveText* getHeader(double lumi, TString channelName)
{
  TPaveText* pt = new TPaveText(0.6,0.72,0.8,0.88,"brNDC");

  pt->SetBorderSize(1);
  pt->SetTextFont(42);
  pt->SetTextSize(0.04);
  pt->SetLineColor(0);
  pt->SetLineStyle(1);
  pt->SetLineWidth(1);
  pt->SetFillColor(0);
  pt->SetFillStyle(1001);
  pt->SetTextAlign(12);
  pt->AddText("CMS Preliminary");
  pt->AddText(Form("%.1f fb^{-1}, #sqrt{s} = 8 TeV", lumi));
  if ( channelName != "" ) pt->AddText(channelName);

  return pt;
}
