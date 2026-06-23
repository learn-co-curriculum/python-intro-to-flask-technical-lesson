#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')# This is a static route that returns a welcome message
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')# this is a dyanamic route that takes a string parameter called username
def user(username):
    return f'<h1>Profile for {username}!</h1>'
#to bypass the File_APP AND FILE_RUN_PORT to run the app on port 5555 with debug mode enabled
if __name__=='__main__':
    app.run(port=5555,debug=True)