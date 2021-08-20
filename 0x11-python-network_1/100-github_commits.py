#!/usr/bin/python3
"""
ist 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
<sha>: <author name>` (one by line)
"""

import requests
from sys import argv


if __name__ == '__main__':
    values = {'owner': argv[1],
              'repo': argv[2]}
    url = "https://api.github.com/repos" + argv[1] + "/" + argv[2] + "/commits"
    res = requests.get(url)
    print(res.json().get('sha'))
