# This "client" is just a utility function for quickly
# and easily making a request to the http interface

import config
import json
import requests
import urllib


def make_request(request, altsecret = None):
    baseurl = config.config['web_baseurl']

    secret  = config.config['secret']
    if altsecret:
        secret = altsecret

    command = urllib.quote(request, '')
    uri = command.replace(urllib.quote(' '), '/', 2)
    url = baseurl + 'api/' + uri

    response = requests.get(url, headers={'secret': secret})
    return json.loads(response.text)
