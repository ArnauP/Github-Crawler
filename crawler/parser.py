import urllib
from utils import *
from bs4 import BeautifulSoup

class Parser(BeautifulSoup):

	def __init__(self, content, base_url, in_type):
		super().__init__()
		self.base_url = base_url
		self.soup = BeautifulSoup(content)
		self.type = in_type
		self.links = []

	# Depending on the type it gathers all the links that redirect to the main repository
	def link_finder(self):
		if self.type == 'Repositories':
			repo_list = self.soup.findAll('ul',attrs={'class':'repo-list'})
			for div in repo_list:
				links = div.findAll('a')
				for a in links:
					if a['class'] == ['v-align-middle']:
						self.links += [self.base_url + a['href']]
			return self.links

	def error_handler(self, message):
		pass