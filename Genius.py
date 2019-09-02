import requests
import os
import json
from flask import Flask
from requests_oauthlib import OAuth1
from boto.s3.connection import S3Connection


app = Flask(__name__)
@app.route('/')

def Genius():
    url = "https://api.genius.com//artists/1000403/songs"

    headers = {
    'Authorization': "Bearer a8F2EXfoIAGgFbjoM4BIRJOTe4vmsVdfStdENraRr3wjedqKwopXfqCRU3uDSdpd"
    }

    response = requests.request("GET", url, headers=headers)
    json_body = response.json()
    return(json_body["response"]["songs"][0]["header_image_url"])
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
