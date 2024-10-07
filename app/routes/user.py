from flask import Blueprint, render_template, redirect
from ..extensions import db
from app.models.user import User
from ..forms import RegistrationForm
user = Blueprint('user', __name__)


@user.route('/user/register')
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print(form.name.data)
        print(form.password.data)
        print(form.avatar.data)
        return redirect('/')
    else:
        print('Error of registration!')
    return render_template('user/register.html', form=form)