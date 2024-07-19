from flask import Blueprint, jsonify

inventory_bp = Blueprint('inventory_bp', __name__)

@inventory_bp.route('/inventory', methods=['GET'])
def get_inventory():
    inventory = [{"id": 1, "item": "Laptop", "quantity": 50}, {"id": 2, "item": "Phone", "quantity": 200}]
    return jsonify(inventory)


