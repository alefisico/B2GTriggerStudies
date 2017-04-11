#nominal=HLT_PFHT900_v6
#nominalRate="12.81"
#listTriggers="HLT_PFHT900_v6 HLT_PFHT900_jet30eta2p4_v1 HLT_PFHT950_v1 HLT_PFHT950_jet30eta2p4_v1 HLT_PFHT1000_v1 HLT_PFHT1000_jet30eta2p4_v1"

#nominal=HLT_AK8PFJet360_TrimMass30_v7
#nominalRate="8.13"
#listTriggers="HLT_AK8PFJet360_TrimMass30_v7 HLT_AK8PFJet380_TrimMass30_v1 HLT_AK8PFJet400_TrimMass30_v1 HLT_AK8PFJet400_TrimMass20_v1 HLT_AK8PFJet400_TrimMass10_v1 HLT_AK8PFJet400_TrimMass40_v1 HLT_AK8PFJet400_TrimMass50_v1 HLT_AK8PFJet420_TrimMass30_v1 HLT_AK8PFJet440_TrimMass30_v1 HLT_AK8PFJet460_TrimMass30_v1 HLT_AK8PFJet360eta2p4_TrimMass30_v1 HLT_AK8PFJet380eta2p4_TrimMass30_v1 HLT_AK8PFJet400eta2p4_TrimMass30_v1 HLT_AK8PFJet420eta2p4_TrimMass30_v1 HLT_AK8PFJet440eta2p4_TrimMass30_v1 HLT_AK8PFJet460eta2p4_TrimMass30_v1"

#nominal=HLT_AK8PFHT750_TrimMass50_v1
#nominalRate="12.09"
#listTriggers="HLT_AK8PFHT750_TrimMass50_v1 HLT_AK8PFHT800_TrimMass50_v1 HLT_AK8PFHT800_TrimMass50eta2p4_v1 HLT_AK8PFHT800_TrimMass50pt150_v1 HLT_AK8PFHT800_TrimMass50pt175_v1 HLT_AK8PFHT800_TrimMass50pt200_v1 HLT_AK8PFHT800_TrimMass40pt150_v1 HLT_AK8PFHT800_TrimMass30pt150_v1 HLT_AK8PFHT800_TrimMass20pt150_v1 HLT_AK8PFHT850_TrimMass50_v1 HLT_AK8PFHT900_TrimMass50_v1 HLT_AK8PFHT950_TrimMass50_v1 HLT_AK8PFHT1000_TrimMass50_v1"

nominal=HLT_PFHT750_4JetPt70_v2
nominalRate="8.93"
listTriggers="HLT_PFHT750_4JetPt70_v2 HLT_PFHT750_4JetPt70eta2p4_v1 HLT_PFHT750_4JetPt60eta2p4_v1 HLT_PFHT800_4JetPt50_v2 HLT_PFHT850_4JetPt50_v1 HLT_PFHT900_4JetPt50_v1 HLT_PFHT950_4JetPt50_v1"


totalEvtNominal=`awk '{ sum+=$4 } END {print sum}' ${1}/${nominal}*`
totalPassNominal=`awk '{ sum+=$5 } END {print sum}' ${1}/${nominal}*`


echo "Trigger	Rate"
for trigger in $listTriggers; do
	
	totalEvtNew=`awk '{ sum+=$4 } END {print sum}' ${1}/${trigger}*`
	totalPassNew=`awk '{ sum+=$5 } END {print sum}' ${1}/${trigger}*`

	#echo ${totalEvtNominal}, ${totalPassNominal}
	#echo ${totalEvtNew}, ${totalPassNew}
	rate=`bc -l <<< $(echo "${nominalRate}"*"${totalPassNew} / ${totalPassNominal}" )`

	#rate=`bc -l <<< $(echo "${totalPassNew} / ((1417*23.31))" )`
	echo ${trigger} ${rate}

done
