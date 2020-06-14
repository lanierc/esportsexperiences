from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_mongoengine import MongoEngine
import os

# import blueprints
from blueprints.user_routes import user_routes
from blueprints.event_routes import event_routes
from blueprints.review_routes import review_routes
from blueprints.request_routes import request_routes
from blueprints.response_routes import response_routes

# Loading environmentals
load_dotenv()
mongodb_uri = os.getenv('MONGODB_URI')

# TODO: Set to false in production
DEBUG = True

# Creating flask instance for routing
app = Flask(__name__)
app.config.from_object(__name__)

# setting up cors
CORS(app, resources={r'/*': {'origins': '*'}})

# Connecting to MongoDB Atlas
app.config['MONGODB_SETTINGS'] = {
    'host': mongodb_uri
}
db = MongoEngine()
db.init_app(app)

# register routes
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(event_routes, url_prefix='/api/events')
app.register_blueprint(review_routes, url_prefix='/api/reviews')
app.register_blueprint(request_routes, url_prefix='/api/requests')
app.register_blueprint(response_routes, url_prefix='/api/responses')


# start the server
if __name__ == '__main__':
    app.run()
