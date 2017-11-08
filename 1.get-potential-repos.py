#!/usr/bin/env python3

import json
import requests
from time import sleep
import math

query_url = 'https://api.github.com/search/repositories?q=language:TypeScript&sort=stars&order=desc&per_page=%d&page=%d'

pages = 1
current_page = 1
max_page = 20
per_page = 100

repos = []
while current_page <= min(pages, max_page):
	r = requests.get(query_url % (per_page, current_page))
	r_json = r.json()
	pages = math.ceil(min(r_json['total_count'], 1000) / per_page) # 1000 is the limit of GitHub
	max_page = min(max_page, pages)
	for item in r_json['items']:
		repo = {}
		repo['name'] = item['name']
		repo['full_name'] = item['full_name']
		repo['html_url'] = item['html_url']
		repo['star'] = item['stargazers_count']
		repos.append(repo)
	print(len(repos))
	sleep(5) # Github API has 10r/min limit
	with open('1.potential-repos.json', 'w') as f:
		f.write(json.dumps(repos))
	current_page = current_page + 1