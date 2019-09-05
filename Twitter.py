import requests
import os
import json

def ApiCall():
    url = "https://api.twitter.com/1.1/search/tweets.json"
    querystring = {"q":"@HERMusicx"}
    s3 = os.getenv("TWITTER_BEARER")
    headers = {
    'Authorization': "Bearer " + str(s3)
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return (response.json())