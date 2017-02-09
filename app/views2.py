from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators
from app import compute
from app import app
DEBUG = True
#app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f37567d441f2b6176a'

# Model
class InputForm(Form):
    r = FloatField(validators=[validators.InputRequired()])

# View

@app.route("/", methods=['GET', 'POST'])
@app.route('/index')
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        r = form.r.data
        s = compute.compute(r)
        return render_template("view_output.html", form=form, s=s)
    else:
        return render_template("view_input.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
