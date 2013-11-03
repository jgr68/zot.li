# imports
import sys, os

from flask import Flask, request, render_template, redirect, url_for
from url_key import generate, sanitize

# initializations
app = Flask(__name__)

# configurations
app.debug = True

fakeDB = {}
URL = '127.0.0.1:5000?'

@app.route('/', methods=['POST','GET'])
def index():
    global fakeDB
    if request.method == 'POST':

        longUrl = sanitize(request.form['longUrl'])
        shortUrl = generate(longUrl)
        fakeDB[shortUrl] = longUrl
        return render_template('index.html', shortUrl=URL+shortUrl)

    elif request.method == 'GET':

        shortUrl = request.query_string
        if shortUrl in fakeDB:
            return redirect(fakeDB[shortUrl])
        return render_template('index.html')
    
if __name__ == '__main__':
    app.run()


