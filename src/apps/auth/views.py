from flask import Blueprint, render_template

auth_app = Blueprint('auth', __name__, template_folder='templates')


@auth_app.route('/')
def home():
    return render_template('/login')