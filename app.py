import json

import requests
from flask import Flask, redirect, render_template, request, url_for
from flask_login import LoginManager, login_required, login_user, logout_user
from oauthlib.oauth2 import WebApplicationClient

import config
from models import User

app = Flask(__name__)
app.secret_key = config.secret_key
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.unauthorized_handler
def unauthorized_handler():
    return "Unauthorized", 403


@login_manager.user_loader
def load_user(user_id):
    return User(id_=user_id)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    openid_configuration = requests.get(config.google_openid_configuration).json()
    authorization_endpoint = openid_configuration["authorization_endpoint"]

    client = WebApplicationClient(config.google_client_id)
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"])

    return redirect(request_uri)


@app.route("/login/callback")
def callback():
    code = request.args.get("code")
    openid_configuration = requests.get(config.google_openid_configuration).json()
    token_endpoint = openid_configuration["token_endpoint"]
    userinfo_endpoint = openid_configuration["userinfo_endpoint"]

    client = WebApplicationClient(config.google_client_id)
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code)
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(config.google_client_id, config.google_client_secret))

    client.parse_request_body_response(json.dumps(token_response.json()))
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    userinfo = userinfo_response.json()

    if userinfo.get("email_verified"):
        _ = userinfo["sub"], userinfo["email"], userinfo["picture"], userinfo["given_name"]
    else:
        return "not verified", 400

    user = User(id_=310)
    login_user(user)

    return redirect(url_for("index"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


if __name__ == "__main__":
    ssl_context = ("openssl/server.crt", "openssl/private.key")
    app.run(debug=True, ssl_context=ssl_context)
