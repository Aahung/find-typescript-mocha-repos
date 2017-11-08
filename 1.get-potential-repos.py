#!/usr/bin/env python3

import json
import requests
from time import sleep
import math

query_url = 'https://api.github.com/search/repositories?q=language:TypeScript%s&sort=stars&order=desc&per_page=%d&page=%d'
star_filter = '+stars:>0'

pages = 1
current_page = 1
max_page = 50
per_page = 100

repos = []
while current_page <= min(pages, max_page):
	r = requests.get(query_url % (star_filter, per_page, current_page))
	print(query_url % (star_filter, per_page, current_page))
	r_json = r.json()
	pages = math.ceil(min(r_json['total_count'], 1000) / per_page) # 1000 is the limit of GitHub
	for item in r_json['items']:
		repo = {}
		repo['name'] = item['name']
		repo['full_name'] = item['full_name']
		repo['html_url'] = item['html_url']
		repo['star'] = item['stargazers_count']
		if len(repos) > 0 and repos[-1]['full_name'] == repo['full_name']:
			continue # in case queries with diffirent stars: filter will have overlaps
		repos.append(repo)
	print(len(repos))
	sleep(5) # Github API has 10r/min limit
	with open('1.potential-repos.json', 'w') as f:
		f.write(json.dumps(repos))
	current_page = current_page + 1
	# start another 1000
	if current_page > pages and current_page <= max_page:
		current_page = 1
		max_page = max_page - pages
		pages = 1
		star_filter = '+stars:<%d' % (repos[-1]['star'] + 1)
