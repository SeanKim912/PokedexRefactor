from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, URLField
from wtforms.validators import DataRequired

class ItemForm(FlaskForm):
    happiness = IntegerField("Happiness")
    imageUrl = URLField("Image", validators=[DataRequired()])
    name = StringField("Name",  validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired()])
