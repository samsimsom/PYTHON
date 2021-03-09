

import os
from flask import Flask
from config import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def index():
    return f"Hello World!-{os.environ['APP_SETTINGS']}"


# if __name__ == "__main__":
#     app.run()
