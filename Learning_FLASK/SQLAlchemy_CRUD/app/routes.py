

from datetime import datetime
from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms import TweetForm, EmptyForm
from app.models import Tweet


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TweetForm()
    empty_form = EmptyForm()
    if form.validate_on_submit():
        tweet = Tweet(tweet=form.tweet.data)
        db.session.add(tweet)
        db.session.commit()
        flash('Your tweet is live')
        return redirect(url_for('index'))

    tweets = Tweet.query.order_by(Tweet.timestamp).all()

    return render_template('index.html',
                           title='index',
                           form=form,
                           tweets=tweets,
                           now=datetime.utcnow(),
                           empty_form=empty_form)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    tweet = Tweet.query.get(id)
    db.session.delete(tweet)
    db.session.commit()
    flash('Tweet was deleted!', category='danger')
    return redirect(url_for('index'))
