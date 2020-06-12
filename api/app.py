from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import mongoengine as me
from flask_mongoengine import MongoEngine
import os
import bcrypt
import json
import jwt
from datetime import datetime

# Loading environmentals
load_dotenv()
secret = os.getenv('SECRET')
mongodb_uri = os.getenv('MONGODB_URI')
mongo_username = os.getenv('USERNAME')
mongo_password = os.getenv('PASSWORD')

# TODO: Set to false in production
DEBUG = True

# Creating flask instance for routing
app = Flask(__name__)
app.config.from_object(__name__)

# setting up cors
CORS(app, resources={r'/*': {'origins': '*'}})

# Connecting to MongoDB Atlas
app.config['MONGODB_SETTINGS'] = {
    'host': mongodb_uri
}
db = MongoEngine()
db.init_app(app)


# Creating User Model
# TODO: refactor this into separate file, along with user routes.
# TODO: set 'active' default to False before production.
class User(me.Document):
    join_date = me.DateTimeField(required=True, default=datetime.now())
    username = me.StringField(required=True)
    email = me.EmailField(required=True)
    password = me.StringField(required=True)
    location = me.StringField(required=False)
    role = me.StringField(required=True, default="User")
    active = me.BooleanField(required=True, default=True)


# Creating routes
@app.route('/api/', methods=['GET'])
def hello_world():
    return jsonify('Hello World')


@app.route('/api/users/signup', methods=['POST'])
def create_user():
    # grab data from frontend
    post_data = request.get_json()
    # hash the password
    password = post_data.get('password')
    hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    # create the user document
    new_user = User(
        username=post_data.get('username'),
        email=post_data.get('email'),
        password=hashed_password,
        location=post_data.get('location'),
        role=post_data.get('role')
    )
    # save to db
    new_user.save()
    # return to user
    return jsonify({
        'status': 'success',
        'message': 'User created',
        'data': new_user
    })


@app.route('/api/users/login', methods=['POST'])
def login_user():
    # grab data from frontend
    post_data = request.get_json()
    password = post_data.get('password')
    email = post_data.get('email')
    # grab the user from db based on email address
    user = User.objects.get(email=email)
    # check the password with that in the db, then return login
    if bcrypt.checkpw(password.encode('utf8'), user['password'].encode('utf8')):
        # return jwt to frontend
        json_user = user.to_json()
        token = jwt.encode({"user": json_user}, secret)
        print(type(token))
        return jsonify({
            'status': 'success',
            'message': 'logged in',
            'token': token.decode('utf8'),
            'data': user
        })

@app.route('/api/users/<id>')
def get_single_user(id):
    user = User.objects.get(pk=id)
    return jsonify({
        'status': 'success',
        'data': user
    })


# start the server
if __name__ == '__main__':
    app.run()
