import requests
import os
import json

def Genius():
    url = "https://api.genius.com//artists/1000403/songs"

    headers = {
    'Authorization': "Bearer " + str(os.getenv("GENIUS_BEARER"))
    }

    response = requests.request("GET", url, headers=headers)
    json_body = response.json()
    return(json_body["response"]["songs"][0]["header_image_url"])
    