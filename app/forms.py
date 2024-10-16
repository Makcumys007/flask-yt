from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, FileField, ValidationError, SelectField
from wtforms.validators import Length, DataRequired, EqualTo
from flask_wtf.file import FileAllowed

from app.models.user import User


class RegistrationForm(FlaskForm):
    avatar = FileField('Avatar' , validators=[FileAllowed(['jpg', 'png'])])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    login = StringField('Login', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError('This login is exist. You should use another login!')
        
class LoginForm(FlaskForm):
    """Form to log in users"""
    login = StringField('Login', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')

class StudentForm(FlaskForm):
    student = SelectField('student', choices=[], render_kw={'class':'form-control'})

        
        