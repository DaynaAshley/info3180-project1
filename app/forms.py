from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import *
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    desc= TextAreaField('Description',validators=[DataRequired()])
    num_bed = StringField('No. of Rooms', validators=[DataRequired()])
    num_bath = StringField('No. of Bathrooms', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    type=SelectField('Property Type', choices=[('House'),('Apartment')])

    location = StringField('Location', validators=[DataRequired()])
    file= FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])