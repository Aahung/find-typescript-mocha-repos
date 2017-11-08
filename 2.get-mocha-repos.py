#!/usr/bin/env python3

import json
import requests
from time import sleep
import math
import os

mocha_repos = []

prs = json.loads(open('1.potential-repos.json', 'r').read())
for pr in prs:
	package_json_url = 'https://raw.githubusercontent.com/%s/master/package.json' % pr['full_name']
	cache_path = 'cache/package-json-%s' % pr['name'].replace('/', '--')
	try:
		if os.path.isfile(cache_path):
			r_json = json.loads(open(cache_path, 'r').read())
		else:
			r = requests.get(package_json_url)
			r_json = r.json()
			with open(cache_path, 'w') as f:
				f.write(json.dumps(r_json))
		if 'scripts' not in r_json:
			raise None
		scripts = r_json['scripts']
		if 'test' not in scripts:
			raise None
		test_script = scripts['test']
		if 'mocha' not in test_script:
			raise None
		print('[+] %s %s' % (pr['name'], test_script))
		pr['test_script'] = test_script
		mocha_repos.append(pr)
	except Exception as e:
		print('[-] %s' % pr['full_name'])

with open('2.mocha-repos.json', 'w') as f:
	f.write(json.dumps(mocha_repos))
	
