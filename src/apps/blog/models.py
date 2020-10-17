from src.main import db


class Post(db.Model):
    """An blog posts model

    :param str Title: post title
    :param str Content: post body
    :param User Author: post author
    :param created_at: creation data
    """


class Comment(db.Model):
    """An blog posts model
    :param str Content: post body
    :param User Author: post author
    :param created_at: creation data
    """

