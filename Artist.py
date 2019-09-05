#Artist.py
import requests, os, json, random, flask
import Twitter, Genius
from flask import Flask

app = Flask(__name__)
@app.route('/')

def GetData():
    
    genius_response = Genius.ApiCall()
    random_num = random.randint(0, len(genius_response["response"]["songs"])-1)
    genius_path = genius_response["response"]["songs"][random_num]

    twitter_response = Twitter.ApiCall()
    random_num = random.randint(0, len(twitter_response["statuses"])-1)
    twitter_path = twitter_response["statuses"][random_num]
    
    
    return flask.render_template("index.html", 
    song_title=genius_path["full_title"], 
    image=genius_path["song_art_image_url"], 
    url=genius_path["url"], 
    tweet=twitter_path["text"],
    profile_photo=twitter_path["user"]["profile_image_url"],
    username=twitter_path["user"]["screen_name"],
    name=twitter_path["user"]["name"])

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug=True)