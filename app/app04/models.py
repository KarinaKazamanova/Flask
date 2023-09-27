from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()





class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False, unique=True)
    user_password = db.Column(db.Integer, nullable=False)
    


def __repr__(self):
    return f'User ("{self.user_name}", "{self.user_email}")'