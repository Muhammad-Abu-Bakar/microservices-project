from flask import Blueprint, jsonify

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = [{"id": 1, "item": "Laptop", "quantity": 1}, {"id": 2, "item": "Phone", "quantity": 2}]
    return jsonify(orders)


