from flask import Blueprint
from .extensions import db
from app.models.user import User

user = Blueprint('user', __name__)

@user.route('/user/<name>')
def creqte_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return 'User created successfully!'