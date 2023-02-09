from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, DecimalField, BooleanField, URLField
from wtforms.validators import DataRequired, NumberRange, Length
import json

types = ["fire",
  "electric",
  "normal",
  "ghost",
  "psychic",
  "water",
  "bug",
  "dragon",
  "grass",
  "fighting",
  "ice",
  "flying",
  "poison",
  "ground",
  "rock",
  "steel"]

UNKNOWN_IMG_URL = "/images/unknown.png"

def get_image(self):
    captured = self.captured
    if(captured):
        return self.imageUrl
    return UNKNOWN_IMG_URL

@property
def get_moves(self):
    rawValue = self.moves
    if(rawValue):
        json.loads(rawValue)
    return None

@get_moves.setter
def get_moves(self, value):
    self.moves = json.loads(value)



class NewPokemonForm(FlaskForm):
    number = IntegerField("Number", validators=[DataRequired(), NumberRange(min=1, max=None, message="Number must be greater than 0.")])
    attack = IntegerField("Attack", validators=[DataRequired(), NumberRange(min=0, max=100, message="Number must in between 0 and 100")])
    defense = IntegerField("Defense", validators=[DataRequired(), NumberRange(min=0, max=100, message="Number must in between 0 and 100")])
    imageUrl = URLField("Image", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=255, message="must be between 3 and 255 characters")])
    type = SelectField("Type", choices=types)
    moves = StringField("Moves", validators=[DataRequired()])
    encounterRate = DecimalField("Encounter Rate", validators=[NumberRange(min=0, max=100, message=None)])
    catchRate = DecimalField("Catch Rate", validators=[NumberRange(min=0, max=100, message=None)])
    captured = BooleanField("Captured?")
    
