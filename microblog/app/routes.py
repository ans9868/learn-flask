from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jesse'}
    posts = [
        {
            'author' : {'username' : 'jesse'},
            'body': 'beautiful day in New Mexico'
        },
        {
            'author': {'username': 'Mr White'},
            'body': 'Indeed jesse, but the day is ripe for cooking'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
