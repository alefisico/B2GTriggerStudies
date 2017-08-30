import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing

###############################
####### Parameters ############
###############################

options = VarParsing ('python')

options.register('RUN', 
		'SingleMuon_Run2017',
		VarParsing.multiplicity.singleton,
		VarParsing.varType.string,
		"name"
		)


options.parseArguments()

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

NAME = options.RUN
#NAME = 'SingleMuon-Run2017A'

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
	   #'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/BC889561-926B-E711-BF4D-02163E01A709.root',
	   #'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/FEA53FE3-936B-E711-986D-02163E01A57E.root',
	   #'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/6A4F47D7-966B-E711-9AB0-02163E01A5BB.root',
	   #'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/46E0CFD9-996B-E711-9E37-02163E014106.root',
	   #'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/B22EA15A-9C6B-E711-9145-02163E01A450.root',
	   #'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/8C29353E-AA6B-E711-A0F2-02163E01A6B4.root',

	   '/store/data/Run2017B/SingleMuon/MINIAOD/PromptReco-v2/000/299/149/00000/0C040CA9-866B-E711-894F-02163E019BE1.root',
	   '/store/data/Run2017B/SingleMuon/MINIAOD/PromptReco-v2/000/299/149/00000/4A43D1F5-886B-E711-8964-02163E01A6AD.root'

    ),
   #lumisToProcess = cms.untracked.VLuminosityBlockRange('275657:1-275657:max'),
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( options.maxEvents ) )

process.TFileService=cms.Service("TFileService",fileName=cms.string( 'TriggerValAndEff.root' ) )

process.PFHTAK4jetsTriggerEfficiency = cms.EDAnalyzer('TriggerValidationAndEfficiencies',
		#baseTrigger = cms.string("HLT_PFJet40_v"),
		baseTrigger = cms.string("HLT_IsoMu27_v"),
		triggerPass = cms.vstring([ "HLT_PFHT1050_v" ] ), 
		recoJets = cms.InputTag("slimmedJets"),
		AK8jets = cms.bool( False )
)

process.PFHTAK8jetsTriggerEfficiency = cms.EDAnalyzer('TriggerValidationAndEfficiencies',
		#baseTrigger = cms.string("HLT_PFJet40_v"),
		baseTrigger = cms.string("HLT_IsoMu27_v"),
		triggerPass = cms.vstring([ "HLT_PFHT1050_v" ] ), 
		recoJets = cms.InputTag("slimmedJetsAK8"),
		AK8jets = cms.bool( True )
)

process.AK4jetsAK8PFJet360TrimMass30TriggerEfficiency = process.PFHTAK4jetsTriggerEfficiency.clone( 
		triggerPass = cms.vstring(["HLT_AK8PFJet360_TrimMass30_v"]),
		)

process.AK4jetsAK8PFHT750TrimMass50TriggerEfficiency = process.PFHTAK4jetsTriggerEfficiency.clone( 
		triggerPass = cms.vstring(["HLT_AK8PFHT750_TrimMass50_v"]),
		)

process.AK4jetsAK8PFHT800TrimMass50TriggerEfficiency = process.PFHTAK4jetsTriggerEfficiency.clone( 
		triggerPass = cms.vstring(["HLT_AK8PFHT800_TrimMass50_v"]),
		)

process.AK8jetsAK8PFJet360TrimMass30TriggerEfficiency = process.PFHTAK8jetsTriggerEfficiency.clone( 
		triggerPass = cms.vstring(["HLT_AK8PFJet360_TrimMass30_v"]),
		)

process.AK8jetsAK8PFHT750TrimMass50TriggerEfficiency = process.PFHTAK8jetsTriggerEfficiency.clone( 
		triggerPass = cms.vstring(["HLT_AK8PFHT750_TrimMass50_v"]),
		)

process.AK8jetsAK8PFHT800TrimMass50TriggerEfficiency = process.PFHTAK8jetsTriggerEfficiency.clone( 
		triggerPass = cms.vstring(["HLT_AK8PFHT800_TrimMass50_v"]),
		)

process.SubstrucutreTriggerEfficiency = process.PFHTAK8jetsTriggerEfficiency.clone( 
		triggerPass = cms.vstring(["HLT_AK8PFHT750_TrimMass50_v", "HLT_AK8PFJet360_TrimMass30_v"]),
		)

process.AK8jetsAK8PFJet360TrimMass30PFHT1050TriggerEfficiency = process.PFHTAK8jetsTriggerEfficiency.clone( 
		triggerPass = cms.vstring(["HLT_PFHT1050_v", "HLT_AK8PFJet360_TrimMass30_v"]),
		)

process.AK8jetsAK8PFHT750TrimMass50PFHT1050TriggerEfficiency = process.PFHTAK8jetsTriggerEfficiency.clone( 
		triggerPass = cms.vstring(["HLT_PFHT1050_v", "HLT_AK8PFHT750_TrimMass50_v"]),
		)

process.AllTriggerEfficiency = process.PFHTAK8jetsTriggerEfficiency.clone( 
		triggerPass = cms.vstring(["HLT_PFHT1050_v", "HLT_AK8PFHT750_TrimMass50_v", "HLT_AK8PFJet360_TrimMass30_v"]),
		)

process.p = cms.Path(
		process.PFHTAK4jetsTriggerEfficiency
		* process.PFHTAK8jetsTriggerEfficiency
		* process.AK4jetsAK8PFJet360TrimMass30TriggerEfficiency
		* process.AK4jetsAK8PFHT750TrimMass50TriggerEfficiency
		* process.AK4jetsAK8PFHT800TrimMass50TriggerEfficiency
		* process.AK8jetsAK8PFJet360TrimMass30TriggerEfficiency
		* process.AK8jetsAK8PFHT750TrimMass50TriggerEfficiency
		* process.AK8jetsAK8PFHT800TrimMass50TriggerEfficiency
		* process.SubstrucutreTriggerEfficiency
		* process.AK8jetsAK8PFJet360TrimMass30PFHT1050TriggerEfficiency
		* process.AK8jetsAK8PFHT750TrimMass50PFHT1050TriggerEfficiency
		* process.AllTriggerEfficiency
		)

process.MessageLogger.cerr.FwkReport.reportEvery = 10000
