from flask import Blueprint, render_template
from ..extensions import db
from app.models.post import Post

post = Blueprint('subject', __name__)

@post.route('/post/create', method=['POST'])
def create():
    return render_template('post/create.html')




