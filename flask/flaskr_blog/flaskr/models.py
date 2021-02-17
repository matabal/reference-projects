import os
import sys
import datetime

from . import db 
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):

    __tablename__    = "user"
    id               = db.Column(db.Integer, primary_key=True)
    username         = db.Column(db.String(60), unique=True)
    password_hash    = db.Column(db.String(128))

    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    
    __tablename__    = "post"
    id               = db.Column(db.Integer, primary_key=True)
    created          = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    title            = db.Column(db.String(80), nullable=False)
    body             = db.Column(db.Text, nullable=False)
    author_id        = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author           = db.relationship('User', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title






