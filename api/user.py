from flask import request, Blueprint, session
from models.user import User

import db
import utils

page = Blueprint("user", __name__)

@page.route("/auth", methods=["POST"])
def auth():
    email = request.form['email']
    password = request.form['password']
    user = User.get_authenticated(email, password)
    if not user:
        return 'Invalid credentials', 403

    session['user_id'] = user.id

    return db.json_encode(user.to_dict())

@page.route("/create", methods=["POST"])
def create():
    email = request.form["email"]
    password = request.form["password"]

    try:
        user = User.create(email, password)
    except db.IntegrityError:
        return "Email has already been used", 400
    return db.json_encode(user.to_dict())

@page.route("/<int:user_id>", methods=["GET"])
def fetch(user_id):
    user = User.get(user_id)
    if not user:
        return "No such user!", 404
    return db.json_encode(user.to_dict())

@page.route("/<int:user_id>", methods=["PUT"])
@utils.require_auth
def modify(user_id):
    bio = request.form["bio"]
    user = User.modify(user_id, bio)
    if not user:
        return "No such user!", 404
    return db.json_encode(user.to_dict())

@page.route("/<int:user_id>/projects", methods=["GET"])
def users(user_id):
    return db.json_encode(User.get(user_id).get_projects())

@page.route("/list", methods=["GET"])
def list():
    return "USER LIST"
