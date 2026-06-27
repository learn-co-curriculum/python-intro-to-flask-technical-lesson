#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'


@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'


#write it in code (for running flask)
#We set up at the bottom of our app app.run and this can let us control useful features such as an auto rerun. By using the debug line we can set our app up so that it will cause the server to restart when we save, whereas previously when testing if we wanted to see a change we make apply to our server we would need to restart the server by exiting and rerunning flask.
if __name__=='__main__':
    app.run(port=5555, debug=True)