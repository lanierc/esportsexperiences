from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from mongoengine import *
import os
import bcrypt
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
# TODO: refactor this into separate file, along with user routes.
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


@app.route('/api/users/signup', methods=['POST'])
def create_user():
    post_data = request.get_json()
    password = bcrypt.genpw(post_data.get('password'), bcrypt.gensalt())
    new_user = User(
        username=post_data.get('username'),
        email=post_data.get('email'),
        password=password,
        location=post_data.get('location'),
        role=post_data.get('role')
    )
    new_user.save()
    return jsonify({
        'status': 'success',
        'user': new_user
    })


# start the server
if __name__ == '__main__':
    app.run()
