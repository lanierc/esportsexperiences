from flask import Blueprint, jsonify, request
from blueprints.user_routes import User
from blueprints.event_routes import Event
import mongoengine as me
from datetime import datetime

response_routes = Blueprint('response_routes', __name__)

class Response(me.Document):
    user = me.ReferenceField(User, required=True)
    response_data = me.DateTimeField(required=True, default=datetime.now())
    body = me.StringField(required=True)