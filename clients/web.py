# Jarvis http client
# Runs on port 8080

import os

import libs.bottle as bottle

BASEURL = ''
SECRET = ''

rootdir = os.path.dirname(os.path.realpath(__file__))

@bottle.route('/')
def index():
    return '''

<html>
<head>

<title>Jarvis</title>

<script src="/static/jquery-1.5.1.min.js"></script>
<script src="/static/global.js"></script>

<link rel="stylesheet" type="text/css" href="/static/style.css" />

</head>
<body>

<span style="display: none;" class="base_url">'''+BASEURL+'''</span>
<span style="display: none;" class="secret">'''+SECRET+'''</span>


</body>
</html>

    '''

@bottle.route('/static/<filename:path>')
def send_static(filename):
    return bottle.static_file(filename, root=os.path.join(rootdir, 'web', 'static'))

def setBaseUrl(baseurl):
    global BASEURL
    BASEURL = baseurl

def setSecret(secret):
    global SECRET
    SECRET = secret

def init():
    bottle.debug(True)
    bottle.run(host='0.0.0.0', port=8080)
