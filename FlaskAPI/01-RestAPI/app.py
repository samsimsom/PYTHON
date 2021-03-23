

from flask import (Flask,
                   render_template)
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Student(Resource):
    def get(self, name):
        return {'student': name}


api.add_resource(Student, '/student/<string:name>')


@app.route('/', methods=['GET', 'POST'])
def index():
    title = 'Index'

    return render_template('index.html',
                           title=title)
