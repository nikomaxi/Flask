#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Generate WebServer to handle request and get key and value of link

    http://127.0.0.1:5000/requestFreqKey?timeStampStart=tss&timeStampStopp=tsp&part=100&keywords%5B0%5D=bliblablub&keywords%5B0%5D=bliblablub2	handle the above request and select two keys (username, password)
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

@app.route("/requestFreqKey")
def requestFreqKey():
    """Handle request for ip:port/login
    
    Returns:	a list of all passed arguments in link statement 
    			>in this case<: username & password
        TYPE: array of dict
    """
    timeStampStart = request.args.get('timeStampStart')
    timeStampStop = request.args.get('timeStampStop')
    parts = request.args.get('parts')

    keywords = request.args.get('keywords')



    # http://127.0.0.1:5000/requestFreqKey?timeStampStart=tss&timeStampStopp=tsp&part=100&keywords%5B0%5D=bliblablub&keywords%5B0%5D=bliblablub2
    print("%s, %s, %s, %s" % (timeStampStop, timeStampStop, parts, keywords))
    print(request.args)

    # returns the array of dicts as plane text in html
    # this is just to see an output while request in web browser



    return request.args


# run the flask app to handle requests
app.run(debug=True)
