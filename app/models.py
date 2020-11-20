from datetime import datetime
from app import db
from hashlib import md5

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carname = db.Column(db.String(32), index=True, unique=True)
    carhp = db.Column(db.String(16), index=True)
    cartorque = db.Column(db.String(16), index=True)
    cardescription = db.Column(db.String(128), index=True)
    carprice = db.Column(db.String(32), index=True)
    carbrand = db.Column(db.String(32), index=True)
    carimage = db.Column(db.String(528), index=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Car {}>'.format(self.carname) 

    def avatar(self, size):
        digest = md5(self.carname.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = body = db.Column(db.String(32))
    body = db.Column(db.String(264))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)