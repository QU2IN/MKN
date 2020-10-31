from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):

    # __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.id
