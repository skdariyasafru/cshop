from flask import Blueprint, redirect, flash
from flask_login import login_required, current_user
from models.models import Cart, Product, Order
from db import db
from datetime import datetime

order_bp = Blueprint("orders", __name__)

@order_bp.route("/checkout")
@login_required
def checkout():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()

    if not cart_items:
        flash("Cart is empty")
        return redirect("/")

    order_number = "ORD-" + datetime.now().strftime("%Y%m%d%H%M%S")

    for item in cart_items:
        product = Product.query.get(item.product_id)

        db.session.add(Order(
            order_number=order_number,
            username=current_user.username,
            product_name=product.name,
            quantity=item.quantity,
            price=product.price,
            total=product.price * item.quantity,
            status="Pending"
        ))

    Cart.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()

    flash("Order placed successfully")
    return redirect("/my_orders")
