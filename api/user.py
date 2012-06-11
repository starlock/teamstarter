from flask import request, Blueprint
import bcrypt
from datetime import datetime

import db

page = Blueprint("user", __name__)

@page.route("/create", methods=["POST"])
def create():
    # request.form["email"]
    # request.form["password"]

    hashed = bcrypt.hashpw(request.form["password"], bcrypt.gensalt())
    try:
        data = db.users.insert().execute(
            email = request.form["email"],
            password = hashed,
            created_at = datetime.now()
        )
    except db.IntegrityError:
        return "Email has already been used", 400

    [user_id] = data.inserted_primary_key

    return "Created user: %s" % user_id, 201

@page.route("/<int:user_id>", methods=["GET"])
def fetch(user_id):
    data = db.users.select().where(
        db.users.c.id == user_id).execute()

    if data.rowcount == 0:
        return "No such user!", 404

    return db.json_encode(data.fetchone())

@page.route("/<int:user_id>", methods=["PUT"])
def modify(user_id):
    # request.form["bio"]
    # request.form["password"]

    data = db.users.update().where(
            db.users.c.id == user_id
        ).values(
            bio = request.form['bio']
        ).execute()

    if data.rowcount == 0:
        return "No such user!", 404

    return "Modify: %d" % user_id

@page.route("/<int:user_id>/projects", methods=["GET"])
def users(user_id):
    return "LIST PROJECTS: %d" % user_id

@page.route("/list", methods=["GET"])
def list():
    return "USER LIST"
