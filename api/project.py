import flask

page = flask.Blueprint("project", __name__)

@page.route("/create", methods=["POST"])
def create():
   return "CREATE PROJECT!"

@page.route("/<int:project_id>", methods=["GET"])
def fetch(project_id):
   return "Get: %d" % project_id

@page.route("/<int:project_id>", methods=["PUT"])
def modify(project_id):
   return "Modify project: %d" % project_id
