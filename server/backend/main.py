#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, send_from_directory, jsonify, redirect
from app.decorators import auth
from app.blueprints.ioc import ioc_bp
from app.blueprints.whitelist import whitelist_bp
from app.blueprints.config import config_bp
from app.blueprints.misp import misp_bp
import datetime
import secrets
import jwt
from app.utils import read_config
from sys import path

app = Flask(__name__, template_folder="../../app/backend/dist")
app.config["SECRET_KEY"] = secrets.token_bytes(32)


@app.route("/", methods=["GET"])
@auth.login_required
def main():
    """
        Return the index.html generated by Vue
    """
    return render_template("index.html")


@app.route("/api/get-token", methods=["GET"])
@auth.login_required
def get_token():
    """
        Return the JWT token for API requests.
    """
    token = jwt.encode({"exp": datetime.datetime.now() +
                        datetime.timedelta(hours=24)}, app.config["SECRET_KEY"])
    return jsonify({"token": token})


@app.route("/<p>/<path:path>", methods=["GET"])
@auth.login_required
def get_file(p, path):
    """
        Return the backend assets (css, js files, fonts etc.)
    """
    rp = "../../app/backend/dist/{}".format(p)
    return send_from_directory(rp, path) if p in ["css", "fonts", "js", "img"] else redirect("/")


@app.errorhandler(404)
def page_not_found(e):
    return redirect("/")


# API Blueprints.
app.register_blueprint(ioc_bp, url_prefix='/api/ioc')
app.register_blueprint(whitelist_bp, url_prefix='/api/whitelist')
app.register_blueprint(config_bp, url_prefix='/api/config')
app.register_blueprint(misp_bp, url_prefix='/api/misp')

if __name__ == '__main__':
    ssl_cert = "{}/{}".format(path[0], 'cert.pem')
    ssl_key = "{}/{}".format(path[0], 'key.pem')

    if read_config(("backend", "remote_access")):
        app.run(host="0.0.0.0", port=443, ssl_context=(ssl_cert, ssl_key))
    else:
        app.run(port=443)
