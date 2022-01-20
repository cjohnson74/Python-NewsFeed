from flask import Blueprint, request
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    newUser = User(
        username = data.username,
        email = data.email,
        password = data.password
    )

    return ''