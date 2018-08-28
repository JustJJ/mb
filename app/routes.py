from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'J'}
    posts = [
        {
            'author': {'username': 'J'},
            'body':  'Wassup yo'
        },
        {
            'author': {'username': 'K'},
            'body': 'Yo wassup'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
