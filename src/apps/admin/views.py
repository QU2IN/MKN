from flask import Blueprint

admin_app = Blueprint('admin', __name__, template_folder='templates')


@admin_app.route('/')
def home():
    return '<h1>Hello Admin</h1>'
