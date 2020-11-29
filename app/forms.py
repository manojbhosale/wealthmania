from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FloatField, FileField, DateTimeField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class EditSecurity (FlaskForm):
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    price =  FloatField('price', validators=[DataRequired()]) 

class UploadPortfolio (FlaskForm):
    uploadedFile = FileField('file', validators=[DataRequired()])
    submit = SubmitField('upload')

class AddNewStock(FlaskForm):
    stockName = StringField('Stock Name',validators=[DataRequired()])
    buyPrice = FloatField('Buy Price', validators=[DataRequired()]) 
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    #date = DateTimeField('Date', validators=[DataRequired()])
    add = SubmitField('Add')





