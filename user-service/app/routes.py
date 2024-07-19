from flask import Blueprint, jsonify

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]
    return jsonify(users)

