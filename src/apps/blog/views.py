from flask import Blueprint

post_app = Blueprint('posts', __name__, template_folder='templates')


@post_app.route('/')
def home():
    return '<h1>posts</h1>'