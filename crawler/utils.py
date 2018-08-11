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
	logging.basicConfig(filename = 'info.log', level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
logger = logging.getLogger('Git-Crawler')


# Creates two files for the queued links to crawl and the crawled links.
def create_data_files(base_url):
	queue_path = 'data_files/queue.txt'
	crawled_path = 'data_files/crawled.txt'
	if not os.path.isfile(queue):
		write_data_file(queue_path, base_url)
	if not os.path.isfile(crawled):
		write_data_file(crawled_path, '')


# Writes in the file the data desired
def write_data_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()


# Reads json data from the file
def read_json(jsonf):
	with open(jsonf) as json_file:
		json_data = json.load(json_file)
		return json_data


# Requests the content of a specific URL going trough a random selected proxy from the list
def connect_url_proxy(url, proxy_list):
	# url = 'https://httpbin.org/ip'		DEBUGGING
	target_proxy = random.choice(proxy_list)
	logger.info('Targeting proxy: ' + target_proxy)
	try:
		response = requests.get(url,proxies={"http": target_proxy, "https": target_proxy})
		html_response = response.text
		logger.info('Connection successful!')
		return html_response
	except:
		logger.critical("Connnection error. Try again or check the availability of the proxy.")