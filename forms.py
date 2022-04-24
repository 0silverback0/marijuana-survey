from flask_wtf import FlaskForm
from wtforms import EmailField, RadioField, SelectField, StringField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    smoker = RadioField('Social or Lone smoker', choices=[ ('Social smoker', 'Social smoker'), ('Lone smoker', 'Lone smoker'), ('Either', 'Either')], validators=[DataRequired()])
    started = RadioField('Age you started', choices=[ ('16 or younger', '16 or younger'), ('17 -25', '17 - 25'),
    ('26 - 35', '26 - 35'), ('35 or older', '35 or older')], validators=[DataRequired()])
    frequency = RadioField('How often?', choices=[ ('A few times per year', 'A few times per year'), ('A few times per month', 'A few times per month'),
    ('Afew times per week', 'A few times per week'), ('Daily', 'Daily')], validators=[DataRequired()])
    reason = SelectField('Reason', choices= [ 'Medical', 'Recreational'], validators=[DataRequired()])
    condition = StringField('Condition ie: pain, anxiety etc..')
    type = RadioField('Type', choices=['Indica (invigorating, energizing reduces stress and anxiety)', 'Sativa (full body affects, promotes relaxation)', 'Hybrid (a mix of both)'], validators=[DataRequired()])
