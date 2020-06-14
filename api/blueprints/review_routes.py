from blueprints.user_routes import User
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
    years_attended = me.ListField(me.IntField(min_value=4, max_value=4), required=True)


# create review
@review_routes.route('', methods=["POST"])
def create_route():
    # get request data
    post_data = request.get_json()
    # get user id
    user_id = post_data.get('user')
    # grab user by id, and check role
    user = User.objects.get(pk=user_id)
    role = user.role
    # if user is not banned, create the document
    if role != 'Banned':
        review = Review(
            user=user_id,
            rating=post_data.get('rating'),
            title=post_data.get('title'),
            body=post_data.get('body'),
            years_attended=post_data.get('years_attended')
        )
        # save to db
        review.save()
        # return to user
        return jsonify({
            'status': 'success',
            'data': review
        })

# get review by id
@review_routes.route('/<id>', methods=["GET"])
def get_single_review(id):
    review = Review.objects.get(pk=id)
    return jsonify({
        'status': 'success',
        'data': review
    })