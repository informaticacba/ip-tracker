#!/usr/bin/env python3

import argparse
import requests
import json


base_url = 'https://geo.leadboxer.com/GeoIpEngine/'

ip = '196.188.224.2'

try:
    response = requests.get(base_url + ip + '?jsonp')
    data = response.json()
    print(response)
    print(data)

except requests.exceptions.Timeout as e:
    print(f'request timeout: {e}')
except requests.exceptions.TooManyRedirects as e:
    print(f'bad url: {e}')
except requests.exceptions.RequestException as e:
    print(f'fatal error: {e}')
    raise SystemExit(e)

