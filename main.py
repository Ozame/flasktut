from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(FlaskForm):
 name = StringField('What is your name?', validators=[Required()])
 submit = SubmitField('Submit')





@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',
    form = form, name = session.get('name'))

@app.route('/user/<name>/')
def hello(name):
    return render_template('user.html', name=name, now=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404


if __name__ == "__main__":
    manager.run()

