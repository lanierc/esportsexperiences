from flask import Blueprint, jsonify, request
from blueprints.user_routes import User
from blueprints.event_routes import Event
import mongoengine as me

request_routes = Blueprint('request_routes', __name__)

class Request(me.Document):
    request_type = me.StringField(required=True)
    user = me.ReferenceField(User, required=True)
    event = me.ReferenceField(Event, required=True)
    name = me.StringField(required=False)
    location = me.StringField(required=False)
    description = me.StringField(required=False)
    website = me.StringField(required=False)
    facebook = me.StringField(required=False)
    twitter = me.StringField(required=False)
    instagram = me.StringField(required=False)
    genre = me.StringField(required=False)
    proof = me.StringField(required=True)


# get all requests
@request_routes.route('', methods=['GET'])
def get_all_requests():
    requests = Request.objects()
    return jsonify({
      'status': 'success',
      'data': requests
    })