from flask import Flask, render_template
from flask_login import LoginManager

import config

app = Flask(__name__)
app.secret_key = config.secret_key
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.unauthorized_handler
def unauthorized_handler():
    return "Unauthorized", 403


@login_manager.user_loader
def load_user(user_id):
    users = config.users
    return users.get(user_id, None)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    ssl_context = ("openssl/server.crt", "openssl/private.key")
    app.run(debug=True, ssl_context=ssl_context)
