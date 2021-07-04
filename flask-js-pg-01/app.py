
import os
from flask import Flask, render_template


app = Flask(__name__)
app.config['ENV'] = os.getenv('FLASK_ENV')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
