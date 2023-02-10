
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from .config import Configuration
from .forms.item_form import ItemForm
from .forms.pokemon_form import NewPokemonForm
from .models import db, Pokemon, PokemonType, Item
import os

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app,db)

# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response

@app.route("/api/pokemon")
def home():
    pokemon = Pokemon.query.all()
    return [poke.to_dict() for poke in pokemon]

@app.route("/api/pokemon/<int:id>")
def get_one_pokemon(id):
    pokemon = Pokemon.query.get(id)
    return pokemon.to_dict()

@app.route("/api/pokemon", methods=["POST"])
def create_pokemon():
   pass
