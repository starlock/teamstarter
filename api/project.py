from flask import request, Blueprint, session
import json

import db
import utils
from models.project import Project

page = Blueprint("project", __name__)

@page.route("/create", methods=["POST"])
def create():
    project = Project.create(request.form["name"],
                             request.form["description"],
                             session["user_id"])

    if project is None:
        return "Could not create project", 500

    return db.json_encode(project.to_dict()), 201

@page.route("/<int:project_id>", methods=["GET"])
def fetch(project_id):
    project = Project.get(project_id)
    if not project:
        return "No such project!", 404
    return db.json_encode(project.to_dict())

@page.route("/<int:project_id>", methods=["PUT"])
@utils.require_project_owner
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
    projects = Project.all()
    return json.dumps([ project.to_dict() for project in projects ])
