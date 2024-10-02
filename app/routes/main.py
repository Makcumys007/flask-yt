from flask import Blueprint, render_template
from ..extensions import db
from app.models.user import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('main/index.html')