#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *
from parser import *


json_data = read_json(sys.argv[1])
base_url = 'https://github.com'
search_url = 'https://github.com/search?q='

json_keywords = json_data['keywords']
json_proxies = json_data['proxies']
json_type = json_data['type']


# Building search URL from keywords
for keyword in range(len(json_keywords)):
	search_url = search_url + '+' + json_keywords[keyword]


# Create proxy parameters list
proxy_list = []
for proxy in range(len(json_proxies)):
	proxy_list += ['http://' + json_proxies[proxy]]


# Connecting to GitHub trough a proxy and getting the content
response_content = connect_url_proxy(search_url, proxy_list)


# Creating a finder object to parse the HTML
try:
	finder = Parser(response_content, base_url, json_type)
	for element in range(len(finder.link_finder())):
		logger.debug(finder.link_finder()[element])

	if finder.link_finder() == []:
		logger.info("Sorry, we couldn't find any matches for that search.")
except:
	logger.error('Failed to create Finder')