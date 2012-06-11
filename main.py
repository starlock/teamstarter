from flask import Flask, render_template
from sqlalchemy import create_engine, MetaData, Table

import api

app = Flask(__name__, static_folder="static")


foo = { "DEBUG": True }
app.config.from_object(foo)

app.register_blueprint(api.user.page, url_prefix="/api/user")
app.register_blueprint(api.project.page, url_prefix="/api/project")

DATABASE_URI = 'postgresql://webadmin@/teamstarter'

engine = create_engine(DATABASE_URI, convert_unicode=True)
metadata = MetaData(bind=engine)

users = Table('users', metadata, autoload=True)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
