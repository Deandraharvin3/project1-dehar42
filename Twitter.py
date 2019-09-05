#Twitter.py
import requests
import os
import json

def ApiCall():
    
    url = "https://api.twitter.com/1.1/search/tweets.json?q=@HERMusicx"

    my_header = {
    'Authorization': "Bearer AAAAAAAAAAAAAAAAAAAAAJka%2FwAAAAAAojV620pev5aGxblqbbMvHMAX85w%3DbSNBhEMnJsYtbvqcmD2NaRACTjKle7100VonCzpos9pMnym8CV"
    # unable to use os.getenv("TWITTER_BEARER")
    }
    response = requests.get(url, headers=my_header)
    return (response.json())