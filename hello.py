from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
from flask_mail import Mail
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from werkzeug.security import generate_password_hash,check_password_hash



app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')
@app.route('/',methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return  render_template('index.html',current_time=datetime.utcnow(),form=form,name=name)

@app.route('/user1/<name>')
def user1(name):
    return render_template('user1.html',name=name)

@app.route('/gis/')
def gis():
    return render_template('gis.html')
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
if __name__ == '__main__':
    app.run(debug=True)
