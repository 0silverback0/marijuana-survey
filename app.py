from flask import Flask, request, redirect, render_template, flash
from psycopg2 import IntegrityError
from models import connect_db, db, User
from forms import UserForm
from sqlalchemy import exc 
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ.get('DATABASE_URL'
'postgres:///flask-heroku') # 'postgresql:///bud' # create and change data base
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'shh')

connect_db(app)
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

#from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
#debug = DebugToolbarExtension(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm()
    peeps = User.query.all()
    name = form.name.data
    ans = form.qs.data
    if form.validate_on_submit():
        new_guy = User(name=name, ans=ans)
        try:  
            db.session.add(new_guy)
            db.session.commit()
            return redirect('/')
        except exc.IntegrityError:
            return redirect('/help')

    else:
        return render_template('index.html', form=form, peeps=peeps)

@app.route('/help')
def help():
    return 'hlp me!'