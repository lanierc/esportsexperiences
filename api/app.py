from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from mongoengine import *
import os
from datetime import datetime

# Loading environmentals
load_dotenv()


DEBUG = True

# Creating flask instance for routing
app = Flask(__name__)
app.config.from_object(__name__)

# setting up cors
CORS(app, resources={r'/*': {'origins': '*'}})

# Connecting to MongoDB Atlas
connect(os.getenv('MONGODB_URI'))


# Creating User Model
class User(Document):
    join_date: DateTimeField(required=True, default=datetime.now())
    username: StringField(required=True)
    email: EmailField(required=True)
    password: StringField(required=True)
    location: StringField(required=False)
    role: StringField(required=True, default="User")


# Creating routes
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify('Hello World')


# start the server
if __name__ == '__main__':
    app.run()
