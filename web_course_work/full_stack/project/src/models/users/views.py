from flask import Blueprint, request, session, url_for, render_template, flash
from werkzeug.utils import redirect

import src.models.users.errors as error
from src.models.users.user import User

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        #  Check login if valid
        email = request.form['email']
        password = request.form['password']

        if User.is_login_valid(email, password):
            session['email'] = email
            return redirect(url_for(".user_alerts"))

    if error.UserNotExistsError:
        flash("{} does not exist.".format(request.form['email']))
        return render_template("user/login.html")
    elif error.IncorrectPasswordError:
        flash("Incorrect password")
        return render_template("user/login.html")
    else:
        return render_template("user/login.html")


@user_blueprint.route('/register')
def register_user():
    pass


@user_blueprint.route('/alerts')
def user_alerts():
    pass


@user_blueprint.route('/logout')
def user_logout():
    pass


@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts():
    pass
