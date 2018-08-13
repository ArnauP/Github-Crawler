#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from utils import *
from parser import Parser


class Crawler:

	proxy_list = ''
	json_type = ''
	search_url = ''
	base_url = ''
	queue_file = ''
	crawled_file = ''
	queue = set()
	crawled = set()

	def __init__(self, base_url, search_url, json_type, proxy_list):
		Crawler.proxy_list = proxy_list
		Crawler.search_url = search_url
		Crawler.json_type = json_type
		Crawler.base_url = base_url
		Crawler.queue_file = 'data_files/queue.txt'
		Crawler.crawled_file = 'data_files/crawled.txt'
		Crawler.main_links = []
		Crawler.main_stats = []
		self.boot()
		self.crawl_page('First Crawler', Crawler.search_url, headed = True)

	# Creates the files needed on first run and starts the Crawler
	@staticmethod
	def boot():
		create_data_files(Crawler.search_url)
		Crawler.queue = file_to_set(Crawler.queue_file)
		Crawler.crawled = file_to_set(Crawler.crawled_file)


	# Updates user display, fills queue and updates files
	@staticmethod
	def crawl_page(thread_name, page_url, headed):
		if headed:
			if page_url not in Crawler.crawled:
				logger.info(thread_name + ' now crawling ' + page_url)
				logger.info('Queue ' + str(len(Crawler.queue)) + ' | Crawled  ' + str(len(Crawler.crawled)))
				Crawler.main_links = Crawler.gather_links(page_url)
				Crawler.add_links_to_queue(Crawler.main_links)
				Crawler.queue.remove(page_url)
				Crawler.crawled.add(page_url)
				Crawler.update_files()
		else:
			if page_url not in Crawler.crawled:
				logger.info(thread_name + ' now crawling ' + page_url)
				logger.info('Queue ' + str(len(Crawler.queue)) + ' | Crawled  ' + str(len(Crawler.crawled)))
				Crawler.main_stats += [Crawler.gather_langstats(page_url)]
				Crawler.queue.remove(page_url)
				Crawler.crawled.add(page_url)
				Crawler.update_files()

	# Connects via proxy to the URL and parses the links of repositories
	@staticmethod
	def gather_links(page_url):
		try:
			response_content = connect_url_proxy(page_url, Crawler.proxy_list)
			finder = Parser(response_content, Crawler.base_url, Crawler.json_type)
			return finder.link_finder()
		except:
			logger.error('Thread Error: Failed to operate Finder')


	# Connects via proxy to the URL and parses the language statistics of the repository
	@staticmethod
	def gather_langstats(page_url):
		try:
			response_content = connect_url_proxy(page_url, Crawler.proxy_list)
			finder = Parser(response_content, Crawler.base_url, Crawler.json_type)
			return finder.stats_finder()
		except:
			logger.error('Thread Error: Failed to operate Finder')

	# Saves queue data to project files
	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			if (url in Crawler.queue) or (url in Crawler.crawled):
				continue
			Crawler.queue.add(url)


	# Updates data files
	@staticmethod
	def update_files():
		set_to_file(Crawler.queue, Crawler.queue_file)
		set_to_file(Crawler.crawled, Crawler.crawled_file)


	# Returns all language statistics gathered
	@staticmethod
	def get_stats():
		return Crawler.main_stats


	# Returns all searched repositories gathered
	@staticmethod
	def get_links():
		return Crawler.main_links