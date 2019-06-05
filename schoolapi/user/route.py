from flask import Blueprint
from . import *

user_blueprint = Blueprint('user', __name__, url_prefix='/user')

user_blueprint.add_url_rule('/register', "register_user", register, methods=["POST"])