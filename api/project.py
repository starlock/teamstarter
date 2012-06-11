import flask

page = flask.Blueprint("project", __name__)

@page.route("/create", methods=["POST"])
def login():
   return "CREATE PROJECT!"

@page.route("/<int:project_id>", methods=["GET"])
def login(project_id):
   return "Get: %d" % project_id

@page.route("/<int:project_id>", methods=["PUT"])
def login(project_id):
   return "Modify project: %d" % project_id
