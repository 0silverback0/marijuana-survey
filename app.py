from flask import Flask, redirect, render_template, flash
from models import connect_db, db, User
from forms import UserForm
from sqlalchemy import exc 
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bud' #os.environ.get('DATABASE_URL', 'postgres://pbjakybwgmhddz:75ebe26ecbb1d8139910f0ecacf69390279ddfac2ef975bfa506108b7ffef367@ec2-3-209-124-113.compute-1.amazonaws.com:5432/d4bndeqs143an3').replace("postgres://", "postgresql://", 1) or 'postgresql:///bud' # create and change data base
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
        new_guy = User(email=email, smoker=smoker, started=started, frequency=frequency, reason=reason,
        condition=condition, type=type)
        try:  
            db.session.add(new_guy)
            db.session.commit()
            return redirect('/')
        except exc.IntegrityError:
            return redirect('/help')

    else:
        return render_template('index.html', form=form, users=users)

@app.route('/help')
def help():
    return 'hlp me!'