

from flask import (Flask,
                   render_template,
                   request,
                   make_response,
                   jsonify)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    title = 'Index'
    return render_template('index.html',
                           title=title)


@app.route("/guestbook")
def guestbook():


    return render_template("index.html")


@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():

    req = request.get_json()
    print(req)
    res = make_response(jsonify(req), 200)

    return res
