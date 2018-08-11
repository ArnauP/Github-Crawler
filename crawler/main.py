#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *
from parser import *


JSON_DATA = read_json(sys.argv[1])
BASE_URL = 'https://github.com'
SEARCH_URL = 'https://github.com/search?q='

JSON_KEYWORDS = JSON_DATA['keywords']
JSON_PROXIES = JSON_DATA['proxies']
JSON_TYPE = JSON_DATA['type']


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


# Connecting to GitHub trough a proxy and getting the content
response_content = connect_url_proxy(SEARCH_URL, proxy_list)



# Creating a finder object to parse the HTML
try:
	RESULT = []
	finder = Parser(response_content, BASE_URL, JSON_TYPE)
	link_list = finder.link_finder()
	for link in link_list:
		TEMP_URL = {}
		TEMP_URL['url'] = link
		RESULT += [TEMP_URL]
	json.dumps(RESULT)
	logger.info(RESULT)
	# print(RESULT)

	if finder.link_finder() == []:
		logger.info("Sorry, we couldn't find any matches for that search.")
except:
	logger.error('Failed to operate Finder')