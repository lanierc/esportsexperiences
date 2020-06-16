from flask import Blueprint, jsonify, request
from blueprints.user_routes import User
import mongoengine as me
from datetime import datetime

response_routes = Blueprint('response_routes', __name__)

class Response(me.Document):
    user = me.ReferenceField(User, required=True)
    response_data = me.DateTimeField(required=True, default=datetime.now())
    body = me.StringField(required=True)


@response_routes.route('', methods=["POST"])
def create_response():
    # deferred import of models to avoid circular import error
    from blueprints.review_routes import Review
    from blueprints.event_routes import Event
    # get request body
    post_data = request.get_json()
    # get user id
    user_id = post_data.get('user')
    # get review id
    review_id = post_data.get('review')
    # get event id
    event_id = post_data.get('event')
    # get review, user and event
    user = User.objects.get(pk=user_id)
    event = Event.objects.get(pk=event_id)
    review = Event.objects.get(pk=event_id)
    # if the user is either an admin, the owner of the event, or the OP of the review, post response.
    if user.role == 'Admin' or user_id == event.owner or user_id == event.user:
        response = Response(
            user=user_id,
            response_data=post_data.get('response_data'),
            body=post_data.get('body')
        )
        response.save()
        # link to review
        review.update(push__responses=response.id)
        return jsonify({
            'status': 'success',
            'message': 'response posted',
            data: response
        })


@response_routes.route('', methods=['GET'])
def get_all_responses():
    responses = Response.objects()
    return jsonify({
        'status': 'success',
        'data': responses
    })