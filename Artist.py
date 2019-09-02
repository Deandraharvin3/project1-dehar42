import requests
import os
import json
from flask import Flask
from requests_oauthlib import OAuth1
from boto.s3.connection import S3Connection

app = Flask(__name__)
@app.route('/')

def ApiCalls():
    url = "https://api.twitter.com/1.1/search/tweets.json"
    querystring = {"q":"@HERMusicx"}
    s3 = S3Connection(os.environ["TWITTER_BEARER"])

    headers = {
    'Authorization': "Bearer " + s3
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_body = response.json()
    #print(json.dumps(json_body, indent=2))
    return (json_body["statuses"][0]["text"])
    #print(response.text)
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))