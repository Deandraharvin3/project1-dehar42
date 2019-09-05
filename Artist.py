#Artist.py
import requests, os, json, random, flask
import Twitter, Genius
from flask import Flask

app = Flask(__name__)
@app.route('/')

def GetData():
    random_num = random.randint(1, 10)
    genius_response = Genius.ApiCall()
    genius_path = genius_response["response"]["songs"][random_num]

    twitter_response = Twitter.ApiCall()
    twitter_path = twitter_response["statuses"][random_num]["text"]
    
    
    f = flask.render_template("index.html", song_title=genius_path["full_title"], image=genius_path["song_art_image_url"], url=genius_path["url"], tweet=twitter_path)
    return (f)

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug=True)