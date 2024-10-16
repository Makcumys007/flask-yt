from crypt import methods
from flask_login import login_required
from flask import Blueprint, render_template, request, redirect
from ..extensions import db
from app.models.post import Post
from ..models.user import User
from ..forms import StudentForm

post = Blueprint('post', __name__)

@post.route('/')
def all():
    posts = Post.query.order_by(Post.date).all()
    return render_template('post/all.html', posts=posts, user=User)

@post.route('/post/create', methods=['GET', 'POST'])
@login_required
def create():
    form = StudentForm()
    form.student.choices = [(s.id, s.name) for s in User.query.filter_by(status='user')]

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
        return render_template('post/create.html', form=form)


@post.route('/post/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update(id):
    result = Post.query.get(id)
    form = StudentForm()
    
    form.student.choices = [(s.id, s.name) for s in User.query.filter_by(status='user')]
    
    if request.method == 'POST':
        result.subject = request.form.get('subject')
        result.student = request.form.get('student')        
        try:
            db.session.commit()
            print('post updated')

            return redirect('/')
        except Exception as e:
            print(str(e))
    else:
        return render_template('post/update.html', post=result, form=form)
    

@post.route('/post/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete(id):
    result = Post.query.get(id)   
    try:
        db.session.delete(result)
        db.session.commit()
        print('post deleted')

        return redirect('/')
    except Exception as e:
        print(str(e))
    



