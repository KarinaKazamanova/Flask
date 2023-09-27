from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, Email


class LoginForm(FlaskForm):
    user_name = StringField('user_name', validators=[DataRequired()])
    user_password = StringField('user_password', validators=[DataRequired()])
    
    
class RegisterForm(FlaskForm):
    user_name = StringField('Name', validators=[DataRequired()])
    e_mail = StringField('E_mail', validators=[DataRequired(), Email()])
    user_password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    password_confirmation = PasswordField('ConfirmationPassword', validators=[DataRequired(), EqualTo('user_password')])
    