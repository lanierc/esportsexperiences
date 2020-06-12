from flask import Blueprint, jsonify, request
import mongoengine as me
import bcrypt
import json
import jwt
from dotenv import load_dotenv
import os
from datetime import datetime

# loading app secret
load_dotenv()
secret = os.getenv('SECRET')

# defining blueprint
user_routes = Blueprint('user_routes', __name__)

# Creating User Model
# TODO: set 'active' default to False before production.
class User(me.Document):
    join_date = me.DateTimeField(required=True, default=datetime.now())
    username = me.StringField(required=True)
    email = me.EmailField(required=True)
    password = me.StringField(required=True)
    location = me.StringField(required=False)
    role = me.StringField(required=True, default="User")
    active = me.BooleanField(required=True, default=True)


# creating user
@user_routes.route('/api/users/signup', methods=['POST'])
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


# sign-in user
@user_routes.route('/api/users/login', methods=['POST'])
def login_user():
    # grab data from frontend
    post_data = request.get_json()
    password = post_data.get('password')
    email = post_data.get('email')
    # grab the user from db based on email address
    user = User.objects.get(email__iexact=email)
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

# get single user by id
@user_routes.route('/api/users/<id>')
def get_single_user(id):
    user = User.objects.get(pk=id)
    return jsonify({
        'status': 'success',
        'data': user
    })