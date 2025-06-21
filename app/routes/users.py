from flask import Blueprint, jsonify    #To add modular route structure and return JSON file

#With this blueprint we shall define routes under /users
bp = Blueprint("users", __name__, url_prefix='/users')

#Creating endpoint that will work with a GET request
@bp.route("/", methods=["GET"])
def list_users():
    return jsonify({"message": "test message"})