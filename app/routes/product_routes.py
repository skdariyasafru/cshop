from flask import Blueprint, render_template, request, jsonify
from models.models import Product

product_bp = Blueprint("products", __name__)

@product_bp.route("/")
def index():
    search = request.args.get("q", "")
    query = Product.query

    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))

    products = query.order_by(Product.id.desc()).all()
    return render_template("index.html", products=products)

@product_bp.route("/search")
def search():
    q = request.args.get("q", "").strip()

    if not q:
        products = Product.query.order_by(Product.id.desc()).limit(20).all()
    else:
        products = Product.query.filter(
            Product.name.ilike(f"%{q}%")
        ).limit(20).all()

    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "image": p.image
        }
        for p in products
    ])
