# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 21:12:02 2025

@author: dthtr
"""

from flask import Flask, render_template, request
import requests
from datetime import datetime
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import os

nltk.download('vader_lexicon')

app = Flask(__name__)

API_KEY = os.getenv("AUSSIE_NEWS_KEY")
page_size = 100
top_headlines_endpoint = r"https://newsapi.org/v2/top-headlines"


sia = SentimentIntensityAnalyzer()

@app.route('/', methods=['GET'])
def create_request():
    request_data = request.json
    country = request_data.get("country")
    category = request_data.get("category")
    
    params = {
        'country': country,
        'apiKey': API_KEY,
        'pageSize': page_size,
        'category': category
    }
    response = requests.get(top_headlines_endpoint, params=params)
    return response.json()


def analyse_data(response):
    if response.get('status') != 'ok':
        print('could not fetch')
        return
    
    n_articles = response.get('totalResults')
    articles = response.get('articles')
    print(articles)



if __name__ == '__main__':
    app.run(debug=True)
