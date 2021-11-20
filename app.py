import requests
from os import getenv
from flask import Flask, render_template, request
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

SECRET_KEY = getenv('YOUTUBE_API_KEY', None)
assert SECRET_KEY

@app.route("/", methods=["GET", "POST"])
def hello_world():
    videos = []
    if request.method =='POST': 
        search_query = request.form['search_query']
        search_url = "https://www.googleapis.com/youtube/v3/search"
        
        params = {
          'key': f'{SECRET_KEY}',
          'q': f'{search_query}',
          'part': 'snippet',
          'type': 'video',
          'maxResults': 20,
          'order': 'date'
        }
        # print (app.config['YOUTUBE_API_KEY'])

        response = requests.get(search_url, params=params).json()['items']

        
        for res in response:
            videos.append({
              'url':'https://youtu.be/' + res['id']['videoId'],
              'title': res['snippet']['title'],
              'desc': res['snippet']['description'],
              'thumbnail': res['snippet']['thumbnails']['default']['url'],
              'publishTime': res['snippet']['publishedAt']
            })
        
    return render_template('index.html', videos=videos)

if __name__ == "__main__":
    app.run(debug=True)
