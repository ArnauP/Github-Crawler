#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from utils import *
from bs4 import BeautifulSoup

class Parser(BeautifulSoup):

	def __init__(self, content, base_url, in_type):
		super().__init__()
		self.soup = BeautifulSoup(content)
		self.base_url = base_url
		self.type = in_type
		self.links = []
		self.lang = []
		self.percent = []
		self.author = ''
		self.dic = {}
		self.link_queued = set()

	# Depending on the type it gathers all the links that redirect to the main repository
	def link_finder(self):
		if self.type == 'Repositories':
			link_obj = self.soup.findAll('a', attrs={'class': 'v-align-middle'})
			for a in link_obj:
				self.links += [self.base_url + a['href']]
				self.link_queued.add(self.base_url + a['href'])
		elif self.type == 'Wikis':
			link_obj = self.soup.findAll('a', attrs={'class': 'h5'})
			for a in link_obj:
				self.links += [self.base_url + a['href'] + '/wiki']
				self.link_queued.add(self.base_url + a['href'] + '/wiki')
		elif self.type == 'Issues':
			link_obj = self.soup.findAll('h3', attrs={'class': 'text-normal pb-1'})
			for h in link_obj:
				self.links += [self.base_url + h.find('a')['href']]
				self.link_queued.add(self.base_url + h.find('a')['href'])
		return self.links

	# Gathers information about the owner and language stats of a repository
	def stats_finder(self):
		if self.type == 'Repositories':
			lang_stats = {}
			span_lang = self.soup.findAll('span', attrs={'class': 'lang'})
			span_percent = self.soup.findAll('span', attrs={'class': 'percent'})
			for span in span_lang:
				self.lang += [span.text]
			for span in span_percent:
				self.percent += [span.text]
			for lang in range(len(self.lang)):
				lang_stats[self.lang[lang]] = self.percent[lang]
			span_author = self.soup.findAll('span', attrs={'class': 'author'})
			for a in span_author:
				self.dic['owner'] = a.text
				self.dic['language_stats'] = lang_stats
			return self.dic

	# Logs an error if needed
	def error_handler(self, message):
		logger.error('Parser error. Unable to finish the task.')