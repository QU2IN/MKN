from flask import Blueprint, render_template

post_app = Blueprint('posts', __name__, template_folder='templates')


@post_app.route('/')
def home():
    return render_template('/blog.html')