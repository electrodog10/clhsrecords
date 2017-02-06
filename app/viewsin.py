from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Me"
    name = "RandomName"
    return render_template('index.html', author=author, name=name)

@app.route('/signup', methods = ['POST'])
def signup():    
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/')

if __name__ == '__main__':
    app.run()
