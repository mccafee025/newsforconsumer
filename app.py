from flask import Flask, render_template
from newsapi import NewsApiClient
app = Flask(__name__)
@app.route('/')
def home():
    newsapi = NewsApiClient(api_key="a953af35750f44a29beae0b8c83e6d5e")
