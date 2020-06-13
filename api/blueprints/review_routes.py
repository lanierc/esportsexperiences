from blueprints.user_routes import User
from blueprints.event_routes import Event
from flask import Blueprint, jsonify, request
import mongoengine as me
from datetime import datetime

review_routes = Blueprint('review_routes', __name__)

class Review(me.Document):
    user = me.ReferenceField(User)
    review_date = me.DateTimeField(required=True, default=datetime.now())
    rating = me.IntField(required=True, min_value=0, max_value=10)
    title = me.StringField(required=True)
    body = me.StringField(required=True)