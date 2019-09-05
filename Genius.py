#Genius.py
import requests
import os
import json

def ApiCall():
    url = "https://api.genius.com/artists/1000403/songs"
    my_header = {
    'Authorization': "Bearer dQx41Lpv5wZe0lQgJTdS1TQonqDkmHcX9D0iL2PEEOAO3O6zxD9BFIklPBuRCDAb" 
    # unable to use os.getenv("GENIUS_BEARER")
    }
    response = requests.get(url, headers=my_header)
    json_body = response.json()
    return(json_body)
    