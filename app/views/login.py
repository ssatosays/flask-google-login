import json
import os

import requests
from flask import redirect, render_template, request, send_from_directory, url_for
from flask_login import current_user, login_required, login_user, logout_user
from oauthlib.oauth2 import WebApplicationClient

import config
from app import app, db
from models import Log, User
from utils import insert_log


@app.route("/")
def index():
    logs = None
    if current_user.is_authenticated:
        logs = db.session.execute(
            db.select(Log).order_by(Log.created_at.desc()).filter(Log.user_id == current_user.id)
        ).scalars()
    return render_template("index.html", logs=logs)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static/image"), "favicon.png")


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
    # print(userinfo)

    if not userinfo.get("email_verified"):
        return "not verified", 400

    user, = db.session.execute(
        db.select(User).filter(User.sub == userinfo["sub"])).first() or (None,)
    if not user:
        user = User(
            sub=userinfo["sub"],
            email=userinfo["email"],
            picture=userinfo["picture"],
            given_name=userinfo["given_name"]
        )
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        insert_log(db, comment="Created User model and logined.", user_id=user.id)
    else:
        insert_log(db, comment="Logined.", user_id=user.id)
    login_user(user)

    return redirect(url_for("index"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
