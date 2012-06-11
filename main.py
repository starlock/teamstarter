from flask import Flask, render_template
import api

app = Flask(__name__, static_folder="static")
app.register_blueprint(api.user.page, url_prefix="/api/user")

@app.route("/")
def index():
   return render_template('index.html')

@app.route("/signup")
def signup():
   return render_template('signup.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0')
