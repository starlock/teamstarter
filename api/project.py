from flask import request, Blueprint, session
from datetime import datetime

import db
import utils

page = Blueprint("project", __name__)

@page.route("/create", methods=["POST"])
def create():
    # request.form["name"]
    # request.form["description"]
    # request.form["role"]

    role = 'ADMIN'
    if 'role' in request.form:
        role = request.form['role'].upper()

    if 'user_id' not in session:
        return "Unauthorized", 403 # TODO: use decorator instead

    conn = db.engine.connect()
    trans = conn.begin()
    try:
        data = conn.execute(db.projects.insert(),
            name = request.form["name"],
            description = request.form["description"]
        )

        [project_id] = data.inserted_primary_key

        data = conn.execute(db.user_projects.insert(),
            user_id = session['user_id'],
            project_id = project_id,
            role = role,
            created_at = datetime.now(),
            modified_at = datetime.now()
        )

        trans.commit()
    except:
        trans.rollback()
        return "Could not create project", 500

    return "Created project: %d" % project_id, 201

@page.route("/<int:project_id>", methods=["GET"])
def fetch(project_id):
    return "Get: %d" % project_id

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
    return "PROJECT LIST"
