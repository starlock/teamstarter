from flask import Flask, render_template

import api

app = Flask(__name__, static_folder="static")
app.config.from_pyfile("config/settings.py")

app.register_blueprint(api.user.page, url_prefix="/api/user")
app.register_blueprint(api.project.page, url_prefix="/api/project")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')
