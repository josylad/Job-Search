from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import TextField
from wtforms.validators import DataRequired


class HotelForm(FlaskForm):
    city = TextField("City", validators=[DataRequired()])
