from flask import Blueprint, jsonify, request
from . import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message":"API is working."})

@main.route('/expenses', methods_['GET'])
def get_expenses():
    expenses = mongo.db.giderler.find()
    return jsonify([{
        'category' : g.get('category'),
        'amount' : g.get('amount')
    } for e in expenses])
