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
    from blueprints.review_routes import Review
    post_data = request.get_json()
    user_id = post_data.get('user')