from flask import Blueprint, render_template, redirect
from ..extensions import db, bcrypt
from app.models.user import User
from ..forms import RegistrationForm

user = Blueprint('user', __name__)


@user.route('/user/register')
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, login=form.login.data, password=hashed_password)
        return redirect('/')
    else:
        print('Error of registration!')
    return render_template('user/register.html', form=form)