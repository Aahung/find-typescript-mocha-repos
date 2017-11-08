#!/usr/bin/env python3

import json
import requests
from time import sleep, strftime
import math
import os

mocha_repos = json.loads(open('2.mocha-repos.json', 'r').read())

table = ['| Repo | Stars | Test Script |', '| --- | --- | --- |']

for repo in mocha_repos:
	table.append('| [%s](%s) | %s | `%s` | ' % (repo['full_name'], repo['html_url'], repo['star'], repo['test_script']))

readme_template = open('README.md.template', 'r').read()
with open('README.md', 'w') as f:
	f.write(readme_template % (strftime('%X %x %Z'), '\n'.join(table)))