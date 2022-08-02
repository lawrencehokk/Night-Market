from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import Length,EqualTo,Email, ValidationError,DataRequired
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('User name already exists! Please try a different username!!')

    def validate_email_address(self, email_address_to_check):
        email_address_to_check = User.query.filter_by(email_address = email_address_to_check.data)
        if email_address_to_check:
            raise ValidationError('Email is already in user, please use another email')

    username = StringField(label='User Name:', validators=[Length(min=2,max=30)])
    email_addres = StringField(label='Email Address:', validators=[Email()])
    password1= PasswordField(label='Password:', validators=[Length(min=6)])
    password2= PasswordField(label='Confirm Password:', validators=[EqualTo('password1')])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:' ,validators=[DataRequired()])
    password= PasswordField(label='Password:',validators=[DataRequired()])
    submit = SubmitField(label='Sign In')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')
