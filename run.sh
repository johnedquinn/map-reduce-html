#!/usr/bin/env python3

import os
import sys

def HtmlToWords():

	WORDS_DIR = '/users/jquinn13/Words'

	print('Running HTML To Words')
	command = f'''
		hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
		-files    htmltowords.py \
		-input    /public/www.2021 \
		-output   {WORDS_DIR} \
		-mapper   htmltowords.py \
		-reducer  NONE
	'''
	os.system(command)

def HtmlToHostWords():

	HOST_WORDS_DIR = '/users/jquinn13/HostWords'

	print('Running HTML To HostWords')
	command = f'''
		hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
		-files    htmltowords.py \
		-input    /public/www.2021 \
		-output   {HOST_WORDS_DIR} \
		-mapper   'htmltowords.py -h' \
		-reducer  NONE
	'''
	os.system(command)

def HtmlToHosts():

	HOSTS_DIR = '/users/jquinn13/Hosts'

	print('Running HTML To Hosts')
	command = f'''
		hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
		-files    htmltohosts.py \
		-input    /public/www.2021 \
		-output   {HOSTS_DIR} \
		-mapper   htmltohosts.py \
		-reducer  NONE
	'''
	os.system(command)


def WordCount():

	WORDS_DIR   = '/users/jquinn13/Words'
	OUT_DIR = '/users/jquinn13/WordCount'

	print('Running WordCount Map-Reduce')
	command = f'''
		hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
		-files    WordCountMap.py,WordCountReduce.py \
		-input    {WORDS_DIR} \
		-output   {OUT_DIR} \
		-mapper   WordCountMap.py \
		-reducer  WordCountReduce.py
	'''
	os.system(command)

def Bigrams():

	WORDS_DIR   = '/users/jquinn13/Words'
	OUT_DIR = '/users/jquinn13/Bigrams'

	print('Running Bigrams Map-Reduce')
	command = f'''
		hadoop \
		jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
		-files    BigramsMap.py,BigramsReduce.py \
		-input    {WORDS_DIR} \
		-output   {OUT_DIR} \
		-mapper   BigramsMap.py \
		-reducer  BigramsReduce.py
	'''
	os.system(command)

def InvertedIndex():

	HOST_WORDS_DIR   = '/users/jquinn13/HostWords'
	OUT_DIR = '/users/jquinn13/InvertedIndex'

	print('Running InvertedIndex Map-Reduce')
	command = f'''
		hadoop \
		jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
		-files    InvertedIndexMap.py,InvertedIndexReduce.py \
		-input    {HOST_WORDS_DIR} \
		-output   {OUT_DIR} \
		-mapper   InvertedIndexMap.py \
		-reducer  InvertedIndexReduce.py
	'''
	os.system(command)

def Hadoop(files, inDir, outDir, mapper, reducer):
	command = f'''
		hadoop \
		jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
		-files    {files} \
		-input    {inDir} \
		-output   {outDir} \
		-mapper   {mapper} \
		-reducer  {reducer}
	'''
	os.system(command)
	
	
if __name__ == '__main__':

	if len(sys.argv) != 2:
		print('USAGE: ./run.py [OPTION]')
		sys.exit(1)

	if sys.argv[1] == 'OutLinks':
		Hadoop('OutLinksMap.py,OutLinksReduce.py', '/users/jquinn13/Hosts', '/users/jquinn13/OutLinks', 'OutLinksMap.py', 'OutLinksReduce.py')
	elif sys.argv[1] == 'Hosts':
		Hadoop('htmltohosts.py', '/public/www.2021', '/users/jquinn13/Hosts', 'htmltohosts.py', 'NONE')
	else:
		print('Not an option')
