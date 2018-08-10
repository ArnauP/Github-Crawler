import sys
import os
import json
import urllib
import requests
import random
import traceback
from utils import *


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
	print('Targeting proxy: ' + target_proxy)
	try:
		response = requests.get(url,proxies={"http": target_proxy, "https": target_proxy})
		html_response = response.text
		print('Connection successful!')
		# print(html_response)
		return response
	except:
		print("Skipping. Connnection error. Try again or check the proxy IP.")
	