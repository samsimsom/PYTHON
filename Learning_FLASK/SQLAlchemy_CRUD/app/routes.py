

from datetime import datetime
from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import TweetForm, UpdateForm, SingleButtonForm
from app.models import Tweet


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TweetForm()
    button = SingleButtonForm()
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
                           button=button)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    tweet = Tweet.query.get_or_404(id)
    db.session.delete(tweet)
    db.session.commit()
    flash('Tweet was deleted!', category='danger')
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = UpdateForm()
    tweet = Tweet.query.get_or_404(id)

    if request.method == 'GET':
        form.tweet.data = tweet.tweet

    if request.method == 'POST':
        if form.validate_on_submit():
            tweet.tweet = form.tweet.data
            tweet.timestamp = datetime.utcnow()
            db.session.commit()
            flash('Your tweet was updated.', category='success')
            return redirect(url_for('index'))

    return render_template('update.html', form=form, id=tweet.id)
