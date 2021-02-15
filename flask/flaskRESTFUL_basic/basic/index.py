import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('index', __name__)

@bp.route("/welcome")
def welcome():
    return "Welcome to flaskRESTFUL demo."