import requests, os, json, random
import Twitter, Genius
from flask import Flask

app = Flask(__name__)
@app.route('/')

def GetData():
    json_body = Twitter.ApiCall()
    random_num = random.randint
    return(json_body["statuses"][random_num]["text"])
    
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug=True)