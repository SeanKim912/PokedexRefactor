from app.models.db import db, Pokemon, Item
from app import app

with app.app_context():

    db.drop_all()
    print("All tables dropped!")

    pokemon1 = Pokemon(
        number = 1,
        imageUrl = '/images/pokemon_snaps/1.svg',
        name = 'Bulbasaur',
        attack = 49,
        defense = 49,
        type = 'grass',
        moves = [
            'tackle',
            'vine whip'
        ],
        captured = True)

    pokemon2 = Pokemon(
        number = 2,
        imageUrl = '/images/pokemon_snaps/2.svg',
        name = 'Ivysaur',
        attack = 62,
        defense = 63,
        type = 'grass',
        moves = [
            'tackle',
            'vine whip',
            'razor leaf'
        ],
        captured = True)

    pokemon3 = Pokemon(
        number = 3,
        imageUrl = '/images/pokemon_snaps/3.svg',
        name = 'Venusaur',
        attack = 82,
        defense = 83,
        type = 'grass',
        moves = [
            'tackle',
            'vine whip',
            'razor leaf'
        ],
        captured = True)

    pokemon4 = Pokemon(
        number = 4,
        imageUrl = '/images/pokemon_snaps/4.svg',
        name = 'Charmander',
        attack = 52,
        defense = 43,
        type = 'fire',
        moves = [
            'scratch',
            'ember',
            'metal claw'
        ],
        captured = True)

    pokemon5 = Pokemon(
        number = 5,
        imageUrl = '/images/pokemon_snaps/5.svg',
        name = 'Charmeleon',
        attack = 64,
        defense = 58,
        type = 'fire',
        moves = [
            'scratch',
            'ember',
            'metal claw',
            'flamethrower'
        ],
        captured = True)

    pokemon6 = Pokemon(
        number = 6,
        imageUrl = '/images/pokemon_snaps/6.svg',
        name = 'Charizard',
        attack = 84,
        defense = 78,
        type = 'fire',
        moves = [
            'flamethrower',
            'wing attack',
            'slash',
            'metal claw'
        ],
        captured = True)

    pokemon7 = Pokemon(
        number = 7,
        imageUrl = '/images/pokemon_snaps/7.svg',
        name = 'Squirtle',
        attack = 48,
        defense = 65,
        type = 'water',
        moves = [
            'tackle',
            'bubble',
            'water gun'
        ],
        captured = True)

    pokemon8 = Pokemon(
        number = 8,
        imageUrl = '/images/pokemon_snaps/8.svg',
        name = 'Wartortle',
        attack = 63,
        defense = 80,
        type = 'water',
        moves = [
            'tackle',
            'bubble',
            'water gun',
            'bite'
        ],
        captured = True)

    pokemon9 = Pokemon(
        number = 9,
        imageUrl = '/images/pokemon_snaps/9.svg',
        name = 'Blastoise',
        attack = 83,
        defense = 100,
        type = 'water',
        moves = [
            'hydro pump',
            'bubble',
            'water gun',
            'bite'
        ],
        captured = True)

    pokemon10 = Pokemon(
        number = 10,
        imageUrl = '/images/pokemon_snaps/10.svg',
        name = 'Caterpie',
        attack = 30,
        defense = 35,
        type = 'bug',
        moves = [
            'tackle'
        ],
        captured = True)

    all_pokemon = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6, pokemon7, pokemon8, pokemon9, pokemon10]
    add_pokemon = [db.session.add(pokemon) for pokemon in all_pokemon]
    db.session.commit()
    print("Pokemon table seeded!")
