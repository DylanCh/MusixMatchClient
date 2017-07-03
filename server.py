import flask
import requests
from musixmatch import API_KEY
app=flask.Flask(__name__)

@app.route('/musixmatch',methods=["GET"])
def musixmatch():
    url = "http://api.musixmatch.com/ws/1.1/matcher.lyrics.get"
    title = flask.request.args.get('title')
    artist = flask.request.args.get('artist')
    querystring = {
        "q_track":title,
        "q_artist":artist,
        "apikey":API_KEY
    }

    headers = {
        'content-type' : 'application/json'
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return (response.text)
    

if __name__=='__main__':
  HOST='127.0.0.1'
  PORT='4000'

  app.run(HOST,PORT)
