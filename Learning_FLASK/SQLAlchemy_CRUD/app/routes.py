

from flask import render_template, redirect, url_for
from app import app, db
from app.forms import TweetForm
from app.models import Tweet


@app.route('/', methods=['GET', 'POST'])
def index():

    title = 'index'

    form = TweetForm()
    if form.validate_on_submit():
        tweet = Tweet(tweet=form.tweet.data)
        db.session.add(tweet)
        db.session.commit()
        return redirect(url_for('index'))

    tweets = Tweet.query.order_by(Tweet.timestamp.desc()).all()

    return render_template('index.html',
                           title=title,
                           form=form,
                           tweets=tweets)
