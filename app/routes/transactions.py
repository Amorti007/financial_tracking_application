from flask import Blueprint, jsonify    #To add modular route structure and return JSON file

#With this blueprint we shall define routes under /transactions
bp = Blueprint("transactions", __name__, url_prefix='/transactions')

#Creating endpoint that will work with a GET request
@bp.route("/", methods=["GET"])
def list_transactions():
    return jsonify({"message": "test message"})