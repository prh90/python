from flask import Flask, render_template, request, session
from src.common.database import Database
from src.models.user import User

app = Flask(__name__)  # __main__
app.secret_key = "pablo"

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')  # 127.0.0.1:5000/login
def login_template():
    return render_template('login.html')


@app.route('/register')  # 127.0.0.1:5000/register
def register_template():
    return render_template('register.html')


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/auth/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = "Guest"

    return render_template("profile.html", email=session['email'])


@app.route('/auth/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    User.register(email, password)

    return render_template("profile.html", email=session['email'])


if __name__ == '__main__':
    app.run()
