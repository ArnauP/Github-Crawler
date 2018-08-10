from utils import *

json_data = read_json(sys.argv[1])
base_url = 'https://github.com/search?q='

json_keywords = json_data['keywords']
json_proxies = json_data['proxies']
json_type = json_data['type']

# Building search URL from keywords
for keyword in range(len(json_keywords)):
	base_url = base_url + '+' + json_keywords[keyword]

# Create proxy parameters
proxy_list = []
for proxy in range(len(json_proxies)):
	proxy_list += ['http://' + json_proxies[proxy]]

# Connecting to GitHub trough a proxy and getting the content
response_content = connect_url_proxy(base_url, proxy_list)