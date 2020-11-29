from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64), index=True, unique=True)
    email=db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    securities = db.relationship('Security', backref='owner',lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))





class Security(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    security_type = db.Column(db.String(50))
    security_name = db.Column(db.String(100))
    country = db.Column(db.String(50))
    buy_price = db.Column(db.Integer)
    buy_time = db.Column(db.DateTime, index = True, default=datetime.utcnow)
    currency = db.Column(db.String(50))
    units = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Security {}>'.format(self.security_name)

    

