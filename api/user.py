import flask
from flask import request, Blueprint

page = Blueprint("api", __name__)

@page.route("/create", methods=["POST"])
def create():
    # request.form["email"]
    # request.form["password"]
    return "CREATE USER"

@page.route("/<int:user_id>", methods=["GET"])
def fetch(user_id):
    return "Get: %d" % user_id

@page.route("/<int:user_id>", methods=["PUT"])
def modify(user_id):
    # request.form["bio"]
    # request.form["password"]
    return "Modify: %d" % user_id
