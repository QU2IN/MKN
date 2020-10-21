from flask import Flask, render_template
from config import DevConfig
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
    return render_template('/blog.html')


if __name__ == '__main__':
    app.run()
