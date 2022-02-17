from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Hello World'
    return render_template('index.html',message = message)

def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to Our News Website'
    return render_template('index.html', title = title)

    ...
from .request import get_news

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    popular_news = get_news('popular')
    print(popular_news)
    title = 'Home - Welcome to The best News Website Online'
    return render_template('index.html', title = title,popular = popular_news)


# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     # Getting popular movie
#     popular_movies = get_movies('popular')
#     upcoming_movie = get_movies('upcoming')
#     now_showing_movie = get_movies('now_playing')
#     title = 'Home - Welcome to The best Movie Review Website Online'
#     return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )