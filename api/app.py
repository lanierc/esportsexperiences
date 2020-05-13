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
    # grab data from frontend
    post_data = request.get_json()
    # hash the password
    password = bcrypt.genpw(post_data.get('password'), bcrypt.gensalt())
    # create the user document
    new_user = User(
        username=post_data.get('username'),
        email=post_data.get('email'),
        password=password,
        location=post_data.get('location'),
        role=post_data.get('role')
    )
    # save to db
    new_user.save()
    # return to user
    return jsonify({
        'status': 'success',
        'user': new_user
    })


@app.route('/api/users/login', methods=['POST'])
def login_user():
    # grab data from frontend
    post_data = request.get_json()
    # grab the user from db based on email address
    user = User.objects.get(email=post_data.get('email'))
    # check the password with that in the db, then return login
    # TODO: return jwt to frontend
    if bcrypt.checkpw(post_data.get('password'), user['password']):
        return jsonify({
            'status': 'success',
            'message': 'logged in'
        })


# start the server
if __name__ == '__main__':
    app.run()
