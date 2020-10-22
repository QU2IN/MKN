from flask_login import UserMixin
from src.main import db
from src.apps.blog import models


class User(UserMixin, db.Model):

    # __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    post = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return '<User %r>' % self.id
