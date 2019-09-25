from datetime import datetime
from app import db, login_manager
from . import db
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(225), unique=True, nullable=False)
    fullname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(255), unique= True, nullable= False, index = True)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'User {self.username}'


class Flight:
    '''
    Flight class to define Flight Objects
    '''

    def __init__(self, price, airline, flight_number, departure_at, return_at, 
                 expires_at):
        self.price = price
        self.airline = airline
        self.flight_number = flight_number
        self.departure_at = departure_at
        self.return_at = return_at
        self.expires_at = expires_at


class Hotel:
    '''
    Hotel class to define Hotel Objects
    '''

    def __init__(self, label, locationName, fullName):
        self.label = label
        self.locationName = locationName
        self.fullName = fullName