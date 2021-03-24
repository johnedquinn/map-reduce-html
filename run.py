#!/usr/bin/env python3

import os

def HtmlToWords():

	WORDS_DIR = '/users/jquinn13/Words'

	print('Running HTML To Words')
	command = f'''
		hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
		-files    htmltowords.py \
		-input    /public/www.2021 \
		-output   {CLEAN_DIR} \
		-mapper   htmltowords.py \
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

	print('Running WordCount Map-Reduce')
	command = f'''
		hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
		-files    BigramsMap.py,BigramsReduce.py \
		-input    {WORDS_DIR} \
		-output   {OUT_DIR} \
		-mapper   BigramsMap.py \
		-reducer  BigramsReduce.py
	'''
	os.system(command)
	
if __name__ == '__main__':

	Bigrams()
