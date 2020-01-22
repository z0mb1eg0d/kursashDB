from flask_login import UserMixin
from app import login

class User(UserMixin):
  id = str()
  username = str
  email = str
  pass_hash = str

@login.user_loader
def load_user(id):
 return User.query.get(int(id))