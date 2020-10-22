from src.main import db
from src.apps.auth.models import User

user = User(email)
user2 = User()

db.session.add(user)
db.session.commit()

db.session.add(user2)
db.session.commit()

User.query.all()