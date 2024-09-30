from flask import Blueprint
from ..extensions import db
from app.models.post import Post

post = Blueprint('subject', __name__)

@post.route('/post/<subject>')
def creqte_post(subject):
    subject = Post(subject=subject)
    db.session.add(subject)
    db.session.commit()
    return 'Subject created successfully!'