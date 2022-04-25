from flask import Flask, redirect, render_template, flash
from models import connect_db, db, User
from forms import UserForm
from sqlalchemy import exc 
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bud' 
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'shh')

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "SECRET!"

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm()
    users = User.query.all()

    email = form.email.data
    smoker = form.smoker.data
    started = form.started.data
    frequency = form.frequency.data
    reason = form.reason.data
    condition = form.condition.data
    type = form.type.data

    if form.validate_on_submit():
        survey_taker = User(email=email, smoker=smoker, started=started, frequency=frequency, reason=reason,
        condition=condition, type=type)
        try:  
            db.session.add(survey_taker)
            db.session.commit()
            return redirect('/complete')
        except exc.IntegrityError:
            flash('You have already taken this survey.')
            return redirect('/complete')

    else:
        return render_template('index.html', form=form, users=users)

@app.route('/complete')
def complete():
    users = User.query.all()
    return render_template('complete.html', users=users)
