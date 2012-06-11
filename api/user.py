import bcrypt
from datetime import datetime

from flask import request, Blueprint
import db

page = Blueprint("user", __name__)

def is_correct_password(raw, hashed):
    """Check whether given raw password matches given hash."""
    return (hashed == bcrypt.hashpw(raw, hashed))

@page.route("/auth", methods=["POST"])
def auth():
    def invalid():
        return 'Invalid credentials', 403

    email = request.form['email']
    password = request.form['password']
    data = db.users.select().where(db.users.c.email == email).execute()

    if data.rowcount == 0:
        return invalid()

    row = data.fetchone()
    if not is_correct_password(password, row['password']):
        return invalid()

    return db.json_encode(row)

@page.route("/create", methods=["POST"])
def create():
    # request.form["email"]
    # request.form["password"]

    hashed = bcrypt.hashpw(request.form["password"], bcrypt.gensalt())
    try:
        data = db.users.insert().execute(
            email = request.form["email"],
            password = hashed,
            created_at = datetime.now(),
            modified_at = datetime.now()
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
