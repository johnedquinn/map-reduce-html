#!/usr/bin/env bash

### Functions

##
# @desc  NA
##
function Hadoop () {
	# Grab Arguments
	files=$1
	inDir=$2
	outDir=$3
	mapper=$4
	reducer=$5
	
	# Run Hadoop
	hadoop \
	jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-files    ${files} \
	-input    ${inDir} \
	-output   ${outDir} \
	-mapper   ${mapper} \
	-reducer  ${reducer}

	return 0
}
	
### Main Execution

# Check Arguments Length
if [ $# -eq 0 ]; then
	echo "USAGE: ./run.py [OPTION]\n"
	exit 1
fi

# Check Which Hadoop to Run
if [ "$1" = "Hosts" ]; then
	Hadoop "htmltohosts.py" "/public/www.2021" "/users/jquinn13/Hosts" "htmltohosts.py" "NONE"

elif [ "$1" = "Words" ]; then
	Hadoop "htmltowords.py" "/public/www.2021" "/users/jquinn13/Words" "htmltowords.py" "NONE"

elif [ "$1" = "HostWords" ]; then
	Hadoop "htmltowords.py" "/public/www.2021" "/users/jquinn13/HostWords" "htmltohosts.py -h" "NONE"

elif [ "$1" = "WordCount" ]; then
	Hadoop "WordCountMap.py,WordCountReduce.py" "/users/jquinn13/Words" "/users/jquinn13/WordCount" "WordCountMap.py" "WordCountReduce.py"

elif [ "$1" = "Bigrams" ]; then
	Hadoop "BigramsMap.py,BigramsReduce.py" "/users/jquinn13/Words" "/users/jquinn13/Bigrams" "BigramsMap.py" "BigramsReduce.py"

elif [ "$1" = "InvertedIndex" ]; then
	Hadoop "InvertedIndexMap.py,InvertedIndexReduce.py" "/users/jquinn13/Words" "/users/jquinn13/InvertedIndex" "InvertedIndexMap.py" "InvertedIndexReduce.py"

elif [ "$1" = "OutLinks" ]; then
	Hadoop "OutLinksMap.py,OutLinksReduce.py" "/users/jquinn13/Hosts" "/users/jquinn13/OutLinks" "OutLinksMap.py" "OutLinksReduce.py"

elif [ "$1" = "InLinks" ]; then
	Hadoop "InLinksMap.py,InLinksReduce.py" "/users/jquinn13/Hosts" "/users/jquinn13/InLinks" "InLinksMap.py" "InLinksReduce.py"

elif [ "$1" = "NDegrees" ]; then
	Hadoop "NDegreesMap.py,NDegreesReduce.py" "/users/jquinn13/Hosts" "/users/jquinn13/NDegrees" "NDegreesMap.py" "NDegreesReduce.py"

else
	echo "Not an option"
	exit 1
fi

exit 0
