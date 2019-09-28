from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired


class JobSearchForm(FlaskForm):
    city = TextField("City")
    keyword = TextField('Keyword', validators=[DataRequired()])
    submit = SubmitField('Search')
