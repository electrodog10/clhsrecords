from flask import Flask, render_template, request, render_template, redirect, url_for, request
from wtforms import Form, StringField, validators, SelectField
from app import compute
from app import app
from flask_table import Table, Col
DEBUG = True
#app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f37567d441f2b6176a'

# Send form
class Form(Form):
    viewingForm = StringField(validators=[validators.InputRequired()])
    option = SelectField('Options', choices=[('1','Name'),('2','Activity'),('3','Year'), ('4','Records')])



# View

@app.route("/", methods=['GET', 'POST'])
@app.route('/index')
def index():
    form = Form(request.form)

    if request.method == 'POST' and form.validate():
        r = form.r.data
        option = form.option.data
        print(option)
        table = compute.compute(viewingForm,option)

        return render_template("view_output.html", form=form, table=table)
    else:
        return render_template("view_input.html", form=form)

#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

#editing


if __name__ == '__main__':
    app.run(debug=True)


