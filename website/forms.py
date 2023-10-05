from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, IntegerField, DecimalField, SelectField, DateField
from wtforms.validators import InputRequired, Length, Email, EqualTo, NumberRange

class LoginForm(FlaskForm):
    user_name = StringField('User Name', validators=[InputRequired('User Name is required')])
    password = PasswordField('Password', validators=[InputRequired('Password is required')])
    submit = SubmitField("Login")
class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[InputRequired('Name is required')])
    description = StringField('Description', validators=[InputRequired('Description is required')])
    date = DateField('Date')
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

