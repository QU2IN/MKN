from flask import Flask
from config import DevConfig
from apps.admin.apps import admin_page
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
app.register_blueprint(admin_page)
db = SQLAlchemy(app)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run()
