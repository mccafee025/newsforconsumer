from flask import Flask, render_template
from newsapi import NewsApiClient
app = Flask(__name__)
@app.route('/')
def home():
    newsapi = NewsApiClient(api_key="a953af35750f44a29beae0b8c83e6d5e")
    top_headlines = newsapi.get_top_headlines(sources = 'cnn')
    t_articles = top_headlines['articles']
    news = []
    dets = []
    img = []
    p_date = []
    url = []
    for i in range(len(t_articles)):
        main_article = t_articles[i]
        news.append(main_article['title'])
        dets.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])
        contents = zip(news,dets,img,p_date,url)
    return render_template('home.html',contents=contents)

if __name__='__main__':
    app.run(debug=True)
