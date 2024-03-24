from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, PasswordField, DateField, TimeField
from wtforms.validators import InputRequired, Length, Email, EqualTo, NumberRange
from flask_ckeditor import CKEditorField

class LoginForm(FlaskForm):
    name = StringField('User Name', validators=[InputRequired('User Name is required')])
    password = PasswordField('Password', validators=[InputRequired('Password is required')])
    submit = SubmitField("Login")

class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[InputRequired('Name is required')])
    description = StringField('Description', validators=[InputRequired('Description is required')])
    date = DateField('Date')
    time = TimeField('Time', validators=[InputRequired('Time is required')])
    location = StringField('Location', default="The New Covenant Baptist Church, Agege")
    submit = SubmitField("Submit")

class RegisterForm(FlaskForm):
    user_name = StringField('User Name', validators=[InputRequired('User Name is required')])
    email = StringField('Email Address', validators=[Email('Email is required'), Email('Email is not valid')])
    #linking two fields - password should be equal to data entered in confirm
    password = PasswordField('Password', validators=[InputRequired(),
                  EqualTo('confirm', message='Passwords should match')])
    confirm = PasswordField('Confirm Password', validators=[InputRequired()])
    #submit button
    submit = SubmitField("Register")

