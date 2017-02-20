from flask import Flask, render_template, request
from wtforms import Form, StringField, validators, SelectField
from app import compute
from app import app
DEBUG = True
#app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f37567d441f2b6176a'

# Model
class Form(Form):
    r = StringField(validators=[validators.InputRequired()])
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
        s = compute.compute(r,option)
        return render_template("view_output.html", form=form, s=s)
    else:
        return render_template("view_input.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)


