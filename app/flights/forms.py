from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField


class FlightForm(FlaskForm):
    origin = StringField("Origin", validators=[DataRequired()])
    destination = StringField("Destination", validators=[DataRequired()])
    depart_date = DateField('Departure Date', format='%Y-%m-%d')
    return_date = DateField('Return Date', format='%Y-%m-%d')
    submit = SubmitField('Buy Now')