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
			link_obj = self.soup.findAll('a', attrs={'class': 'v-align-middle'})
			for a in link_obj:
				self.links += [self.base_url + a['href']]
		elif self.type == 'Wikis':
			link_obj = self.soup.findAll('a', attrs={'class': 'h5'})
			for a in link_obj:
				self.links += [self.base_url + a['href'] + '/wiki']
		elif self.type == 'Issues':
			link_obj = self.soup.findAll('h3', attrs={'class': 'text-normal pb-1'})
			for h in link_obj:
				self.links += [self.base_url + h.find('a')['href']]
		return self.links


	def error_handler(self, message):
		logger.error('Parser error. Unable to finish the task.')