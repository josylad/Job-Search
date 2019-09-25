from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import (DataRequired, Length, Email, EqualTo,
                                ValidationError)
from app.models import User
from flask_login import current_user
from flask_datepicker import datepicker


class FlightForm(FlaskForm):
    origin = StringField("Origin", validators=[DataRequired()])
    destination = StringField("Destination", validators=[DataRequired()])
    depart_date = DateField('Departure Date', validators=[DataRequired()])
    return_date = DateField('Return Date', validators=[DataRequired()])
    submit = SubmitField('Buy Now', validators=[DataRequired()])




