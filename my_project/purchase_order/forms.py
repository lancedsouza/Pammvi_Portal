from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from my_project.models import User

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=StringField('Password',validators=[DataRequired()])
    submit=SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('Username',validators=[DataRequired()])
    password=StringField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must Match!')])
    pass_confirm=StringField('Confirm Password',validators=[DataRequired()])
    submit=SubmitField('Register')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has already been registered!')
        
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is taken!')


