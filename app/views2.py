from flask import Flask, render_template, request, render_template, redirect, url_for, request
from wtforms import Form, StringField, validators, SelectField
from app import compute
from app import app
import flask_login
#from flask_table import Table, Col
DEBUG = True
#app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f37567d441f2b6176a'



login_manager = flask_login.LoginManager()

login_manager.init_app(app)
# Send form
class Form(Form):
    viewingForm = StringField(validators=[validators.InputRequired()])
    viewingOption = SelectField('Options', choices=[('1','Name'),('2','Activity'),('3','Year'), ('4','Records')])

users = {'lewis@coloffmedia.com': {'pw': 'admin'}}

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['pw'] == users[email]['pw']

    return user


# View
@app.route("/", methods=['GET', 'POST'])
@app.route('/index')
@flask_login.login_required
def index():
    form = Form(request.form)
    if request.method == 'POST' and form.validate():
        viewingForm = form.viewingForm.data
        viewingOption = form.viewingOption.data
        items = compute.compute(viewingForm,viewingOption)
        return render_template("view_output.html", form=form, items=items)
    else:
        return render_template("view_input.html", form=form)



#login

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'></input>
                <input type='password' name='pw' id='pw' placeholder='password'></input>
                <input type='submit' name='submit'></input>
               </form>
               '''

    email = request.form['email']
    if request.form['pw'] == users[email]['pw']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('index'))

    return 'Bad login'

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'




#editing


if __name__ == '__main__':
    app.run(debug=True)


