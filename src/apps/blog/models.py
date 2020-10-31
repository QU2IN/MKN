from app import db
# from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    user = db.relationship('User', backref='post')


    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    body = db.Column(db.Text)
    #posts = db.Column(db.Integer, db.ForeignKey('Post.id'), nullable=False)
    comments = db.relationship(Post)

    def __repr__(self):
        return '<{}, 4elik : {}>'.format(self.id, self.name)

