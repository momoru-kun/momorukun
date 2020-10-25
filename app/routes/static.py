from flask import send_from_directory
from app import app

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# FOR Manifest
@app.route('/site.webmanifest')
def send_manifest():
    return send_from_directory('static', 'site.webmanifest')

# FOR favicon
@app.route('/favicon.ico')
def send_favicon():
    return send_from_directory('static', 'favicon.ico')

@app.route('/favicon-32x32.png')
def send_favicon32x32():
    return send_from_directory('static', 'favicon-32x32.png')

@app.route('/favicon-16x16.png')
def send_favicon16x16():
    return send_from_directory('static', 'favicon-16x16.png')

# android-chrome.png
@app.route('/android-chrome-256x256.png')
def send_androidchrome256x256():
    return send_from_directory('static', 'android-chrome-256x256.png')

@app.route('/android-chrome-192x192.png')
def send_androidchrome192x192():
    return send_from_directory('static', 'android-chrome-129x192.png')

# Apple
@app.route('/apple-touch-icon.png')
def send_appletouchicon():
    return send_from_directory('static', 'apple-touch-icon.png')

@app.route('/safari-pinned-tab.svg')
def send_safaripinnedtab():
    return send_from_directory('static', 'safari-pinned-tab.svg')

# Microsoft
@app.route('/browserconfig.xml')
def send_browserconfig():
    return send_from_directory('static', 'browserconfig.xml')

@app.route('/mstile-150x150.png')
def send_mstile150x150():
    return send_from_directory('static', 'mstile-150x150.png')