import requests
import os
import json
from flask import Flask
from requests_oauthlib import OAuth1

app = Flask(__name__)
@app.route('/')

def ApiCalls():
    url = "https://api.twitter.com/1.1/search/tweets.json"
    querystring = {"q":"@HERMusicx"}
    s3 = os.getenv("TWITTER_BEARER")
    headers = {
    'Authorization': "Bearer " + str(s3)
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_body = response.json()
    return(json.dumps(json_body, indent=2))
    #return (json_body["statuses"][0]["text"])
    #print(response.text)
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug=True)