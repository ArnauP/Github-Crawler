#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
from queue import Queue
from utils import *
from parser import Parser
from crawler import Crawler


JSON_DATA = read_json(sys.argv[1])
BASE_URL = 'https://github.com'
SEARCH_URL = 'https://github.com/search?q='

JSON_KEYWORDS = JSON_DATA['keywords']
JSON_PROXIES = JSON_DATA['proxies']
JSON_TYPE = JSON_DATA['type']

QUEUE_FILE = 'data_files/queue.txt'
CRAWLED_FILE = 'data_files/crawled.txt'
NUMBER_OF_THREADS = 6		# Depends on the OS
queue = Queue()


# Create worker threads (will die when main exits)
def create_workers():
	for _ in range(NUMBER_OF_THREADS):
		t = threading.Thread(target=work)
		t.daemon = True
		t.start()


# Do the next job in the queue
def work():
	while True:
		url = queue.get()
		Crawler.crawl_page(threading.current_thread().name, url, headed = False)
		queue.task_done()


# Each queued link is a new job
def create_jobs():
	for link in file_to_set(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
	queued_links = file_to_set(QUEUE_FILE)
	if len(queued_links) > 0:
		logger.info(str(len(queued_links)) + ' links in the queue')
		create_jobs()


# Building search URL from keywords
for keyword in range(len(JSON_KEYWORDS)):
	SEARCH_URL = SEARCH_URL + '+' + JSON_KEYWORDS[keyword]


# Create proxy parameters list
proxy_list = []
for proxy in range(len(JSON_PROXIES)):
	proxy_list += ['http://' + JSON_PROXIES[proxy]]


# Creating the final search url
if JSON_TYPE == "Repositories":
	SEARCH_URL += '&type=Repositories'
elif JSON_TYPE == "Wikis":
	SEARCH_URL += '&type=Wikis'
elif JSON_TYPE == "Issues":
	SEARCH_URL += '&type=Issues'
else:
	logger.error('Type not supported')


# Start threading
if JSON_TYPE == "Repositories":

	# Start threading
	Crawler(BASE_URL, SEARCH_URL, JSON_TYPE, proxy_list)
	create_workers()
	crawl()

	# Build the final json for the output
	make_final_json(Crawler.get_links(), Crawler.get_stats())
else:
	# Crawls the first page
	response_content = connect_url_proxy(SEARCH_URL, proxy_list)
	finder = Parser(response_content, BASE_URL, JSON_TYPE)

	# Build the final json for the output
	make_json(finder)