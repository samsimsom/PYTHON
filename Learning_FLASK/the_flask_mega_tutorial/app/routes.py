
from flask import render_template
from app import app		# app package (directory) import app variable

@app.route('/')			# decorator from flask - URL
@app.route('/index')	# more URL
def index():

	title = 'Home'
	
	# FAKE DATA
	user = {'username': 'Firat'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Ankara!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The X-Man movie was so cool!'
		},
		{
			'author': {'username': 'Jessica'},
			'body': 'I\'m so Hot!'
		}
	]

	return render_template('index.html', 
							title=title, 
							user=user,
							posts=posts)


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/contact')
def contact():
	return 'Contact'