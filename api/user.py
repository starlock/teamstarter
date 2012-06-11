import flask

page = flask.Blueprint("api", __name__)

@page.route("/create", methods=["POST"])
def login():
   return "CREATE!"

@page.route("/<int:user_id>", methods=["GET"])
def login(user_id):
   return "Get: %d" % user_id

@page.route("/<int:user_id>", methods=["PUT"])
def login(user_id):
   return "Modify: %d" % user_id
