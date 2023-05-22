from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField("LogIn")


class RegisterForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField("Register")