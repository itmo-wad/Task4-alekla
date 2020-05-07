from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class SignUpForm(Form):
    login = TextAreaField('User Name', validators= [ DataRequired()])
    email = TextAreaField('User email', validators=[DataRequired()])
    password = PasswordField('Password',validators=[ DataRequired()])
    submit = SubmitField('Sign Up')

class SignInForm(Form):
    login = TextAreaField('Login', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Log In')
