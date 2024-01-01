from flask import Blueprint, request
from models import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json() or request.form
    username = data["username"]
    password = data["password"]
    users = User.query.all()


@auth.route("/signup", methods=["POST"])
def signup():
    data = request.get_json() or request.form
    username = data["username"]
    email = data["email"]
