from crypt import methods

from flask import Blueprint, render_template, request, redirect
from ..extensions import db
from app.models.post import Post

post = Blueprint('post', __name__)

@post.route('/')
def index():
    return render_template('post/all.html')

@post.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        teacher = request.form['teacher']
        subject = request.form.get('subject')
        student = request.form.get('student')
        date = request.form.get('date')

        new_post = Post(teacher=teacher, subject=subject, student=student, date=date)
        try:
            db.session.add(new_post)
            db.session.commit()
            print('post created')

            return redirect('/')
        except Exception as e:
            print(str(e))
    else:
        return render_template('post/create.html')




