from flask import Flask, render_template, request, session
from src.common.database import Database
from src.models.user import User

app = Flask(__name__)  # __main__
app.secret_key = "pablo"


@app.route('/')  # www.mysite.com/api/
def home():
    return render_template('login.html')


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = "Guest"

    return render_template("profile.html", email=session['email'])


if __name__ == '__main__':
    app.run()
