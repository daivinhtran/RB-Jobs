import os
import subprocess
import requests
import json
from datetime import datetime

import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../tokens'))

import tokens

events_url = "https://api.github.com/users/daivinhtran/events"
response = requests.get(events_url, auth=('daivinhtran', tokens.github_OAuth))

if response.status_code != 200:
	print(response.text)

events = response.json();

commitCount = 0;
start = None
end = None

for event in events:

    if event['type'] == 'PushEvent':
        date_obj = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        if start is None:
            start = date_obj

        if end is None:
            end = date_obj

        if date_obj < end:
            end = date_obj

        if date_obj > start:
            start = date_obj 

        commitCount += len(event['payload']['commits'])

interval = start - end

data = {'commit_count': commitCount, 'interval': interval.days}

with open('../daivinhtran.github.io/_data/github_stats.json', 'w') as f:
  json.dump(data, f, ensure_ascii=False)

path = "../daivinhtran.github.io"
os.chdir(path)
 
output = subprocess.check_output(["git", "status"])

if "nothing to commit" in output:
        return
else:
        subprocess.call(["git", "add", "_data/github_stats.json"])
        subprocess.call(["git", "commit", "-m", "'update github_stats.json'"])
        subprocess.call(["git", "push", "origin", "master"])
