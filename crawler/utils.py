#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import json
import urllib
import requests
import random
import traceback
import logging
from bs4 import BeautifulSoup


# Logging configuration
if sys.argv[-1] == '--DEBUG':
	logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s')
elif sys.argv[-1] == '--INFO':
	logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
else:
	logging.basicConfig(filename = 'data_files/info.log', level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
logger = logging.getLogger('Git-Crawler')


# Creates two files for the queued links to crawl and the crawled links.
def create_data_files(base_url):
	queue_path = 'data_files/queue.txt'
	crawled_path = 'data_files/crawled.txt'
	write_data_file(queue_path, base_url)
	write_data_file(crawled_path, '')


# Writes in the file the data desired
def write_data_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()


# Add data onto an existing file
def append_to_file(path, data):
	with open(path, 'a') as file:
		file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
	with open(path, 'w'):
		pass


# Read a file and conver each line to set items
def file_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as f:
		for line in f:
			results.add(line.replace('\n', ''))
	return results


# Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
	try:
		delete_file_contents(file)
		for link in links:
			append_to_file(file, link)
	except:
		pass


# Reads json data from the file
def read_json(jsonf):
	with open(jsonf) as json_file:
		json_data = json.load(json_file)
		return json_data


# Writes json into a file
def write_json(path, jsonf):
	with open('data_files/result.json', 'w') as outfile:
		json.dump(jsonf, outfile)


# Requests the content of a specific URL going trough a random selected proxy from the list
def connect_url_proxy(url, proxy_list):
	target_proxy = random.choice(proxy_list)
	logger.info('Targeting proxy: ' + target_proxy)
	try:
		response = requests.get(url,proxies={"http": target_proxy, "https": target_proxy})
		html_response = response.text
		logger.info('Connection successful!')
		return html_response
	except:
		logger.critical("Connnection error. Try again or check the availability of the proxy.")


def make_final_json(list_url_repositories, list_dic_langstats):
	try:
		RESULT = []
		for link in list_url_repositories:
			owner = link.split('/')[3]
			TEMP_URL = {}
			TEMP_URL['url'] = link
			for langstats in list_dic_langstats:
				if langstats['owner'] == owner:
					TEMP_URL['extra'] = langstats
			RESULT += [TEMP_URL]
		json.dumps(RESULT)
		if sys.argv[-1] == '--INFO':
			logger.info(RESULT)
		else:
			write_json('data_files/result.json', RESULT)		# In case of expecting a file output
			print(RESULT)
	except:
		logger.error("Error. Cound't generate final output")

def make_json(parser):
	try:
		RESULT = []
		link_list = parser.link_finder()
		for link in link_list:
			TEMP_URL = {}
			TEMP_URL['url'] = link
			RESULT += [TEMP_URL]
		if parser.link_finder() == []:
			logger.info("Sorry, we couldn't find any matches for that search.")
		json.dumps(RESULT)
		if sys.argv[-1] == '--INFO':
			logger.info(RESULT)
		else:
			write_json('data_files/result.json', RESULT)		# In case of expecting a file output
			print(RESULT)
	except:
		logger.error('Failed to operate Parser.')
