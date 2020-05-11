from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from mongoengine import *
import os
import datetime

load_dotenv()


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r'/*': {'origins': '*'}})

connect(os.getenv('MONGODB_URI'))


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify('Hello World')


if __name__ == '__main__':
    app.run()
