from flask import Blueprint, request, redirect, flash
from flask_login import login_user, logout_user
from models.models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or user.password != password:
        flash("Invalid credentials")
        return redirect("/?login=1")

    login_user(user)
    return redirect("/")

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect("/")
