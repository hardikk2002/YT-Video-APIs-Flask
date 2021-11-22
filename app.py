import requests
import json
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
    search_query, nextPageToken, prevPageToken = "", "", ""
    if request.method =='POST': 
        search_query = request.form['search_query']
        search_url = "https://www.googleapis.com/youtube/v3/search"
        params = {
          'key': f'{SECRET_KEY}',
          'q': f'{search_query}',
          'part': 'snippet',
          'type': 'video',
          'maxResults': 9,
          'order': 'date',
        }

        response = requests.get(search_url, params=params).json()
        
        try:
            nextPageToken = response['nextPageToken']
        except:
            nextPageToken = None

        try:
            prevPageToken = response['prevPageToken']
        except:
            prevPageToken = None

        
        for res in response['items']:
            videos.append({
              'url':'https://youtu.be/' + res['id']['videoId'],
              'title': res['snippet']['title'],
              'desc': res['snippet']['description'],
              'thumbnail': res['snippet']['thumbnails']['default']['url'],
              'publishTime': res['snippet']['publishedAt']
            })

        
    if request.method =='GET': 
        if(request.args):
            search_query = request.args.get('q')
            pageToken = request.args.get('pageToken')
       
            search_url = "https://www.googleapis.com/youtube/v3/search"
            params = {
              'key': f'{SECRET_KEY}',
              'q': f'{search_query}',
              'part': 'snippet',
              'type': 'video',
              'maxResults': 9,
              'order': 'date',
              'pageToken':f'{pageToken}',
            }
            
            response = requests.get(search_url, params=params).json()
            
            try:
                nextPageToken = response['nextPageToken']
            except:
                nextPageToken = None

            try:
                prevPageToken = response['prevPageToken']
            except:
                prevPageToken = None

            for res in response['items']:
                videos.append({
                  'url':'https://youtu.be/' + res['id']['videoId'],
                  'title': res['snippet']['title'],
                  'desc': res['snippet']['description'],
                  'thumbnail': res['snippet']['thumbnails']['default']['url'],
                  'publishTime': res['snippet']['publishedAt']
                })     
        
   
    return render_template('index.html', videos=videos,nextPageToken=nextPageToken,prevPageToken=prevPageToken,search_query=search_query)

if __name__ == "__main__":
    app.run(debug=True)
