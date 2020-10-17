from flask import Blueprint

auth_app = Blueprint('auth', __name__, template_folder='templates')


@auth_app.route('/')
def home():
    return '<h1>Ath</h1>'