#!/usr/bin/env python3

import os

def WordCount():

	HADOOP_HOME = '/users/jquinn13'
	HTML_DIR = 'WsAdksFskeo18dnc'
	WORD_COUNT_DIR = 'cni29324ifnec23oeinc'

	print('Running htmltowords Map')
	command = f'''
		hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
		-files    htmltowords.py \
		-input    /public/www.2021/zoom.iu.edu \
		-output   {HADOOP_HOME}/{HTML_DIR} \
		-mapper   htmltowords.py \
		-reducer  NONE
	'''
	os.system(command)

	print('Running WordCount Map-Reduce')
	command = f'''
		hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
		-files    WordCountMap.py,WordCountReduce.py \
		-input    {HADOOP_HOME}/{HTML_DIR} \
		-output   {HADOOP_HOME}/{WORD_COUNT_DIR} \
		-mapper   WordCountMap.py \
		-reducer  WordCountReduce.py
	'''
	os.system(command)

	print('Removing Directories')
	os.system(f'hadoop fs -rm -r {HADOOP_HOME}/{HTML_DIR}')
	os.system(f'hadoop fs -rm -r {HADOOP_HOME}/{WORD_COUNT_DIR}')
	
if __name__ == '__main__':

	WordCount()
