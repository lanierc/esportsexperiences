from flask import Blueprint, jsonify, request
from blueprints.user_routes import User
from blueprints.review_routes import Review
import mongoengine as me

event_routes = Blueprint('event_routes', __name__)

class Event(me.Document):
    name = me.StringField(required=True, unique=True)
    location = me.StringField(required=False)
    event_type = me.StringField(required=False)
    description = me.StringField(required=False)
    website = me.StringField(required=False)
    facebook = me.StringField(required=False)
    twitter = me.StringField(required=False)
    instagram = me.StringField(required=False)
    genre = me.StringField(required=False)
    reviews = me.ListField(me.ReferenceField(Review))
    owner = me.ReferenceField(User)


# create event
@event_routes.route('', methods=['POST'])
def create_event():
    # grab data from frontend
    post_data = request.get_json()
    # grab user id
    user_id = post_data.get('user')
    # query user and check role
    user = User.objects.get(pk=user_id)
    role = user.role
    if role == 'Admin':
        # create the event document
        new_event = Event(
            name=post_data.get('name'),
            location=post_data.get('location'),
            description=post_data.get('description'),
            website=post_data.get('website'),
            facebook=post_data.get('facebook'),
            twitter=post_data.get('twitter'),
            instagram=post_data.get('instagram'),
            genre=post_data.get('genre'),
            event_type=post.data.get('event_type')
        )
        # save to db
        new_event.save()
        # return to user
        return jsonify({
            'status': 'success',
            'message': 'Event created',
            'data': new_event
        })

# get all events
@event_routes.route('', methods=['GET'])
def get_all_events():
    events = Event.objects()
    return jsonify({
        'status': 'success',
        'data': events
    })

# get single event
@event_routes.route('/<id>', methods=['GET'])
def get_single_event(id):
    event = Event.objects.get(pk=id)
    return jsonify({
        'status': 'success',
        'data': event
    })

# delete event
@event_routes.route('/<id>', methods=['DELETE'])
def delete_single_event(id):
    event = Event.objects.get(pk=id)
    post_data = request.get_json()
    user_id = post_data.get('user')
    user = User.objects.get(pk=user_id)
    if user.role == 'Admin':
        event.delete()
        return jsonify({
            'status': 'success',
            'message': 'Event deleted'
        })
