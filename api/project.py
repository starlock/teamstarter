from flask import request, Blueprint

page = Blueprint("project", __name__)

@page.route("/create", methods=["POST"])
def create():
    # request.form["name"]
    # request.form["description"]
    return "CREATE PROJECT"

@page.route("/<int:project_id>", methods=["GET"])
def fetch(project_id):
    return "Get: %d" % project_id

@page.route("/<int:project_id>", methods=["PUT"])
def modify(project_id):
    # request.form["name"]
    # request.form["description"]
    return "Modify: %d" % project_id

@page.route("/<int:project_id>/users", methods=["GET"])
def users(project_id):
    # request.form["name"]
    # request.form["description"]
    return "LIST USERS: %d" % project_id

@page.route("/list", methods=["GET"])
def list():
    return "PROJECT LIST"
