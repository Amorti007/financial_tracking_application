from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from dotenv import load_dotenv
from config import Config
import os

app.config.from_object(Config)
mongo = PyMongo()

def create_app():
    load_dotenv()
    app = Flask(__name__)

    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    mongo.init_app(app)

    CORS(app)

    from.routes import main
    app.register_blueprint(main)

    return app