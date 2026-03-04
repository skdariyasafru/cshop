from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models.models import Cart
from db import db

cart_bp = Blueprint("cart", __name__)

@cart_bp.route("/add_to_cart", methods=["POST"])
@login_required
def add_to_cart():
    data = request.get_json()
    product_id = data.get("id")

    item = Cart.query.filter_by(
        user_id=current_user.id,
        product_id=product_id
    ).first()

    if item:
        item.quantity += 1
    else:
        item = Cart(user_id=current_user.id, product_id=product_id, quantity=1)
        db.session.add(item)

    db.session.commit()

    return jsonify({"status": "added", "quantity": item.quantity})
