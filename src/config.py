import sqlite3


class DbConnection:
    def __init__(self):
        self.connection = sqlite3.connect('database.db', check_same_thread=False)
        self.cursor = self.connection.cursor()

    def execute_select_query(self, query):
        return self.cursor.execute(query).fetchall()

    def execute_dml_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()


DB = DbConnection()


class Config(object):
    pass

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dase.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
