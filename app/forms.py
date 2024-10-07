from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import Length, DataRequired, FileAllowed, EqualTo
class RegistrationForm(FlaskForm):
    avatar = FileField('Avatar' , validators=[FileAllowed(['jpg', 'png'])])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    login = StringField('Login', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')