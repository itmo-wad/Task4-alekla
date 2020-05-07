from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from models.db import initialize_db
from flask_restful import Api
from resources.errors import errors

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

from resources.api_routes import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

initialize_db(app)
initialize_routes(api)

# default
from flask import Flask, session, request, redirect, url_for, render_template, flash, jsonify, make_response


@app.route('/')
def index():
    auth_header = request.headers.get('Authorization')

    if auth_header:
        return redirect(url_for('cabinet'))
    else:
        return redirect(url_for('login'))
