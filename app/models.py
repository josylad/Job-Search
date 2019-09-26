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

    def __init__(self,value,return_date,origin,duration,distance,destination,depart_date):
        self.value = value
        self.return_date = return_date
        self.origin = origin
        self.duration = duration
        self.distance = distance
        self.destination = destination
        self.depart_date = depart_date



class Flightgroup:
    '''
    Flight class to define Flight Objects
    '''

    def __init__(self,origin,destination,price, airline,flight_number):
        self.origin = origin
        self.destination = destination
        self.price = price
        self.airline = airline
        self.flight_number = flight_number
        


class Hotel:
    '''
    Hotel class to define Hotel Objects
    '''

    def __init__(self, label, locationName, fullName):
        self.label = label
        self.locationName = locationName
        self.fullName = fullName
        