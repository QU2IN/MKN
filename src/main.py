from flask import Flask, request, redirect, render_template, url_for, make_response
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from config import DevConfig
from config import DB
from flask_sqlalchemy import SQLAlchemy

from apps.admin.views import admin_app
from apps.auth.views import auth_app
from apps.blog.views import post_app


app = Flask(__name__)
app.config.from_object(DevConfig)
app.register_blueprint(admin_app, url_prefix='/admin')
app.register_blueprint(auth_app, url_prefix='/auth')
app.register_blueprint(post_app, url_prefix='/blog')
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('/mainlink.html')


@app.route('/error')
def error():
    return '<h1>I am Error!</h1>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    from src.apps.auth.models import User
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    return render_template('/login.html')


@app.route('/signup', methods=['GET','POST'])
def signup_post():

    from src.apps.auth.models import User
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    return render_template('/signup.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
