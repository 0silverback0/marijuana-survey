from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    qs = RadioField('smoke?', choices=[ ('smoker', 'smoker'), ('non-smoker', 'non-smoker')])
