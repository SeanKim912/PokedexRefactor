from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pokemon(db.Model):
    __tablename__ = "pokemon"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False, unique=True)
    type = db.Column(db.Enum, nullable=False)
    moves = db.Column(db.String, nullable=False)
    encounterRate = db.Column(db.Decimal)
    catchRate = db.Column(db.Decimal)
    captured = db.Column(db.Boolean)

    pokemontypes = db.relationship("PokemonType", back_populates="pokemon")

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer)
    imageUrl = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    pokemonId = db.Column(db.Integer, nullable=False)

class PokemonType(db.Model):
    __tablename__ = "pokemontypes"
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.id"))
    type = db.Column(db.String, nullable=False)

    pokemon = db.relationship("Pokemon", back_populates="pokemontypes")
