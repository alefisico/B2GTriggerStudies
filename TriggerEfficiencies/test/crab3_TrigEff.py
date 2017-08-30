##################################################################
########   TO RUN THIS: python crab3_QCD.py
########   DO NOT DO: crab submit crab3_QCD.py
##################################################################

from CRABClient.UserUtilities import config
import argparse, sys
from httplib import HTTPException
from CRABAPI.RawCommand import crabCommand
from multiprocessing import Process
import glob


config = config()

config.General.requestName = ''
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'TriggerValidationAndEfficiencies_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = ''
config.Data.outLFNDirBase = '/store/user/algomez/'
config.Data.publication = False
config.Data.ignoreLocality = True
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10

#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = 'T3_US_Rutgers'
config.Data.outLFNDirBase = '/store/user/algomez/myArea/EOS/TriggerEfficiency/'


def submit(config):
	try:
		crabCommand('submit', config = config)
	except HTTPException, hte:
		print 'Cannot execute commend'
		print hte.headers

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--sample', action='store', default='all', dest='sample', help='Sample to process. Example: QCD, RPV, TTJets.' )
	parser.add_argument('-v', '--version', action='store', default='v01p0', dest='version', help='Version: v01, v02.' )

	try: args = parser.parse_args()
	except:
		parser.print_help()
		sys.exit(0)

	Samples = {}
	#Samples[ 'B2GSingleMuonH3' ] = [ '/SingleMuon/vorobiev-Run2016H-PromptReco-v3_B2GAnaFW_80X_v2p4-376a23645e94877b22a7f32873431514/USER', 10, 'Spring16_23Sep2016HV2', '' ]
	#Samples[ 'miniAODSingleMuonH2' ] = [ '/SingleMuon/Run2016H-03Feb2017_ver2-v1/MINIAOD', 10, '80X_dataRun2_Prompt_v16', '' ]
	#Samples[ 'miniAODSingleMuonH3' ] = [ '/SingleMuon/Run2016H-03Feb2017_ver3-v1/MINIAOD', 10, '80X_dataRun2_Prompt_v16', '' ]

	Samples[ 'SingleMuonAv2' ] = [ '/SingleMuon/Run2017A-PromptReco-v2/MINIAOD', 10, '', '' ]
	Samples[ 'SingleMuonAv3' ] = [ '/SingleMuon/Run2017A-PromptReco-v3/MINIAOD', 10, '', '' ]
	Samples[ 'SingleMuonBv1' ] = [ '/SingleMuon/Run2017B-PromptReco-v1/MINIAOD', 10, '', '' ]
	Samples[ 'SingleMuonBv2' ] = [ '/SingleMuon/Run2017B-PromptReco-v2/MINIAOD', 10, '', '' ]
	Samples[ 'SingleMuonCv1' ] = [ '/SingleMuon/Run2017C-PromptReco-v1/MINIAOD', 2, '', '' ]
	Samples[ 'SingleMuonCv2' ] = [ '/SingleMuon/Run2017C-PromptReco-v2/MINIAOD', 2, '', '' ]
	Samples[ 'SingleMuonCv3' ] = [ '/SingleMuon/Run2017C-PromptReco-v3/MINIAOD', 1, '', '' ]
			

	processingSamples = {}
	if 'all' in args.sample: 
		for sam in Samples: processingSamples[ sam ] = Samples[ sam ]
	else:
		for sam in Samples: 
			if sam.startswith( args.sample ): processingSamples[ sam ] = Samples[ sam ]

	if len(processingSamples)==0: print 'No sample found. \n Have a nice day :)'
		
	for sam in processingSamples:
		dataset = processingSamples[sam][0]
		#if not 'miniAOD' in args.sample: procName = dataset.split('/')[1]+dataset.split('/')[2].split('_')[0]+processingSamples[sam][3]+'_'+args.version
		procName = dataset.split('/')[1]+'_'+dataset.split('/')[2].split('_')[0]+processingSamples[sam][3]+'_'+args.version
		#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-300575_13TeV_PromptReco_Collisions17_JSON_MuonPhys.txt'
		config.Data.lumiMask = 'crab_projects/crab_SingleMuon_Run2017C-PromptReco-v2_v02/results/notFinishedLumis.json'
		#config.Data.lumiMask = '/afs/cern.ch/work/a/algomez/RPVStops/CMSSW_8_0_20/src/RUNA/RUNAnalysis/test/supportFiles/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON'+processingSamples[sam][3]+'.txt'

		config.Data.inputDataset = dataset
		config.General.requestName = procName
		#if 'B2G' in args.sample:
		#	config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader'
		#	supportFiles = glob.glob('../../RUNAnalysis/test/supportFiles/'+processingSamples[sam][2]+'*txt')
		#	config.JobType.inputFiles = supportFiles

		#listpyCfgParams = [ 'PROC='+procName, 
		#		( 'miniAOD=True' if 'miniAOD' in args.sample else 'jecVersion='+processingSamples[sam][2]), 
		#		'version=Dijet' ]
		#if 'miniAOD' in args.sample: listpyCfgParams.append( 'globalTag='+processingSamples[sam][2] )
		#config.JobType.pyCfgParams = listpyCfgParams
		p = Process(target=submit, args=(config,))
		p.start()
		p.join()
