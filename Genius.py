import requests
import os
import json
from flask import Flask
from requests_oauthlib import OAuth1

app = Flask(__name__)
@app.route('/')

def Genius():
    url = "https://api.genius.com//artists/1000403/songs"

    headers = {
    'Authorization': "Bearer " + str(os.getenv("GENIUS_BEARER"))
    }

    response = requests.request("GET", url, headers=headers)
    json_body = response.json()
    return(json_body["response"]["songs"][0]["header_image_url"])
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
