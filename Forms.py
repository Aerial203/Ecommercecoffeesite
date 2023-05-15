from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Length(min=6, max=35)])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField("LogIn")
