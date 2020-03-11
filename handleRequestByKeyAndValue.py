#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Generate WebServer to handle request and get key and value of link

	http://127.0.0.1:5000/login?username=max&password=pw1
	handle the above request and select two keys (username, password)
	return a array of passed key and values as html 
"""
from flask import request
from flask import Flask

__copyright__ = "Copyright 2020, Mazanec"
__version__ = "1.0"
__email__ = "maxmazanec@gmail.com"
__status__ = "Final"


# generate instence of Flask app
app = Flask(__name__)

@app.route("/login")
def login():
    """Handle request for ip:port/login
    
    Returns:	a list of all passed arguments in link statement 
    			>in this case<: username & password
        TYPE: array of dict
    """

    # read value of key 'username'
    username = request.args.get('username')
    # read value of key 'password'
    password = request.args.get('password')
    # print all passed arguments
    print(request.args)

    # returns the array of dicts as plane text in html
    # this is just to see an output while request in web browser
    return request.args


# run the flask app to handle requests
app.run()
