from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from mongoengine import *
import os
from datetime import datetime

load_dotenv()


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r'/*': {'origins': '*'}})

connect(os.getenv('MONGODB_URI'))


class User(Document):
    join_date: DateTimeField(required=True, default=datetime.now())
    username: StringField(required=True)
    email: EmailField(required=True)
    password: StringField(required=True)
    location: StringField(required=False)
    role: StringField(required=True, default="User")


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify('Hello World')


if __name__ == '__main__':
    app.run()
