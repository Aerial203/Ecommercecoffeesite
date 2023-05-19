from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Length(min=6, max=35), Email()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField("LogIn")


class RegisterForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [DataRequired(), Length(min=6, max=35), Email()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField("Register")