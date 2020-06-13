from flask import Blueprint, jsonify, request
import mongoengine as me
from datetime import datetime

event_routes = Blueprint('event_routes', __name__)

class Event(me.Document):
    name = me.StringField(required=True)
    location = me.StringField(required=False)
    description = me.StringField(required=False)
    website = me.StringField(required=False)
    facebook = me.StringField(required=False)
    twitter = me.StringField(required=False)
    instagram = me.StringField(required=False)
    genre = me.StringField(required=False)


# create event
@event_routes.route('/', methods=['POST'])
def create_event():
    # grab data from frontend
    post_data = request.get_json()
    # create the event document
    new_event = Event(
        name=post_data.get('name'),
        location=post_data.get('location'),
        description=post_data.get('description'),
        website=post_data.get('website'),
        facebook=post_data.get('facebook'),
        twitter=post_data.get('twitter'),
        instagram=post_data.get('instagram'),
        genre=post_data.get('genre')
    )
    # save to db
    new_event.save()
    # return to user
    return jsonify({
        'status': 'success',
        'message': 'Event created',
        'data': new_event
    })