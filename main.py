from flask import Flask, render_template, session, redirect

import db
import api
from models.user import User
from session import PsqlSessionInterface

app = Flask(__name__, static_folder="static")
app.session_interface = PsqlSessionInterface()
app.config.from_pyfile("config/settings.py")

app.register_blueprint(api.user.page, url_prefix="/api/user")
app.register_blueprint(api.project.page, url_prefix="/api/project")

@app.route("/logout")
def logout():
    if 'user_id' in session:
        del session['user_id']
    return redirect('/')

@app.route("/")
@app.route("/<path:path>")
def index(path='/'):
    user_session = {}
    if 'user_id' in session:
        user = User.get(session['user_id'])
        if user is not None:
            user_session = db.json_encode(user.to_dict())
    return render_template('index.html', user_session=user_session)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')
