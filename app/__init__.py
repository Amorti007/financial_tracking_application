from flask import Flask             # To create flask app
from flask_pymongo import PyMongo   # To connect Flask and MongoDB
from flask_cors import CORS         # To activate CORS for frontend
import os                           # To read environment variables

#Defining the central object for Flask and MongoDB connection
mongo = PyMongo()

#Defining the Flask App Factory
def create_app():
    app = Flask(__name__)

    #Getting the connection address from environment variables
    app.config["MONGO_URI"] = os.getenv("MONGO_URI","mongodb://localhost:27017/finance")

    #Integration of MongoDB connection into application and frontend
    mongo.init_app(app)
    CORS(app)

    #Adding blueprints (modular route structures)
    from app.routes import transactions, users
    app.register_blueprint(transactions.bp)
    app.register_blueprint(users.bp)

    return app
