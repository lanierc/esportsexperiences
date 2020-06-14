from flask import Blueprint, jsonify, request
from blueprints.user_routes import User
from blueprints.event_routes import Event
import mongoengine as me

response_routes = Blueprint('response_routes', __name__)