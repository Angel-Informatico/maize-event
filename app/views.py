# by Marcus Huderle, 2015

from flask import render_template, flash
from app import app
from app.forms import TrainerIdForm
import pymongo

import datetime
import random

# uriString = app.config['MONGOSOUP_URL']
# client = pymongo.MongoClient(uriString)
# db = client.get_default_database()

# Event configurations for each Pokémon
POKEMON_EVENTS = {
	'pikablue': {
		'name': 'Flying/Surfing Pikablue',
		'description': 'This Pikachu will either know Fly or Surf. Plus, it\'s shiny, so it\'s a Pikablue!',
		'image': 'pikablue.png',
		'mon_id': 0x54,  # Pikachu
		'moves': [[0x13, 0x39], 0x54, 0x2d, 0],  # Random Fly/Surf, Thundershock, Growl, None
		'spdspc_iv': 0xaa,  # shiny DVs
		'atkdef_iv': 0xaa,  # shiny DVs
		'level': 0x5,
		'level_display': 5,
		'alt_sprite': 0x0,
		'moves_text': 'Fly or Surf, Thundershock, Growl'
	},
	'squirtle': {
		'name': 'Sunglasses Squirtle',
		'description': 'A special Squirtle wearing sunglasses. It\'s shiny!',
		'image': 'sunglasses-squirtle.png',
		'mon_id': 0xB1,  # Squirtle - internal index (Red/Blue)
		'moves': [0x3D, 0x39, 0x82, 0],  # Bubblebeam, Surf, Skull Bash, None
		'spdspc_iv': 0xaa,  # shiny DVs
		'atkdef_iv': 0xaa,  # shiny DVs
		'level': 0x5,
		'level_display': 5,
		'alt_sprite': 0x1,  # Alternate sunglasses sprite
		'moves_text': 'Bubblebeam, Surf, Skull Bash'
	},
	'wartortle': {
		'name': 'Sunglasses Wartortle',
		'description': 'A special Wartortle wearing sunglasses. It\'s shiny!',
		'image': 'sunglasses-wartortle.png',
		'mon_id': 0xB3,  # Wartortle - internal index (Red/Blue)
		'moves': [0x39, 0x82, 0x38, 0],  # Surf, Skull Bash, Hydro Pump, None
		'spdspc_iv': 0xaa,  # shiny DVs
		'atkdef_iv': 0xaa,  # shiny DVs
		'level': 0x10,  # Level 16
		'level_display': 16,
		'alt_sprite': 0x1,  # Alternate sunglasses sprite
		'moves_text': 'Surf, Skull Bash, Hydro Pump'
	},
	'blastoise': {
		'name': 'Sunglasses Blastoise',
		'description': 'A special Blastoise wearing sunglasses. It\'s shiny!',
		'image': 'sunglasses-blastoise.png',
		'mon_id': 0x1C,  # Blastoise - internal index (Red/Blue)
		'moves': [0x39, 0x38, 0x82, 0],  # Surf, Hydro Pump, Skull Bash, None
		'spdspc_iv': 0xaa,  # shiny DVs
		'atkdef_iv': 0xaa,  # shiny DVs
		'level': 0x24,  # Level 36
		'level_display': 36,
		'alt_sprite': 0x1,  # Alternate sunglasses sprite
		'moves_text': 'Surf, Hydro Pump, Skull Bash'
	},
	'electrode': {
		'name': 'Headband Electrode',
		'description': 'A special Electrode wearing a headband. It\'s shiny!',
		'image': 'headband-electrode.png',  # Specific headband sprite
		'mon_id': 0x8D,  # Electrode - internal index (Red/Blue)
		'moves': [0x57, 0x99, 0x78, 0],  # Thunder, Explosion, Self-Destruct, None
		'spdspc_iv': 0xaa,  # shiny DVs
		'atkdef_iv': 0xaa,  # shiny DVs
		'level': 0x1e,  # Level 30
		'level_display': 30,
		'alt_sprite': 0x1,  # Alternate headband sprite
		'moves_text': 'Thunder, Explosion, Self-Destruct'
	}
}

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = TrainerIdForm()
	selected_pokemon = 'pikablue'  # Default selection
	
	if form.validate_on_submit():
		selected_pokemon = form.pokemon.data
		if form.trainer_id.data.isdigit():
			trainer_id = int(form.trainer_id.data)
			if trainer_id < 0 or trainer_id > 65535:
				flash('You entered an invalid Trainer ID "%s". The Trainer ID must be a number between 0-65535.' % (form.trainer_id.data))
			else:
				try:
					code = get_code(int(trainer_id), selected_pokemon)
					pokemon_info = POKEMON_EVENTS[selected_pokemon]
				except Exception as e:
					flash('Something went wrong. :(  Contact shantytownred@gmail.com so he can fix it!')
					return render_template("index.html", form=form, pokemon_info=POKEMON_EVENTS[selected_pokemon])

				html = render_template("index.html", form=form, code=code, pokemon_info=POKEMON_EVENTS[selected_pokemon])
				try:
					code = {
						'date': datetime.datetime.utcnow(),
						'trainer_id': trainer_id,
						'numbers': code,
					}
					# db.codes.insert(code)
				except:
					pass
				return html
		else:
			flash('You entered an invalid Trainer ID "%s". The Trainer ID must be a number between 0-65535.' % (form.trainer_id.data))

	return render_template("index.html", form=form, pokemon_info=POKEMON_EVENTS[selected_pokemon])

def get_code(trainer_id, pokemon_type='pikablue'):
	"""Generate the code for the selected Pokémon"""
	event = POKEMON_EVENTS.get(pokemon_type, POKEMON_EVENTS['pikablue'])
	
	# For Pikablue, the first move is random
	if pokemon_type == 'pikablue' and isinstance(event['moves'][0], list):
		move_1 = random.choice(event['moves'][0])  # Fly / Surf
	else:
		move_1 = event['moves'][0]
	
	move_2 = event['moves'][1]
	move_3 = event['moves'][2]
	move_4 = event['moves'][3]
	
	return gen_code(
		event['mon_id'],
		move_1,
		move_2,
		move_3,
		move_4,
		event['spdspc_iv'],
		event['atkdef_iv'],
		event['level'],
		event['alt_sprite'],
		trainer_id
	)


def gen_code(mon_id, move_1, move_2, move_3, move_4, spdspc_iv, atkdef_iv, level, alt_sprite, trainer_id):
	trainer_id_hi = trainer_id >> 8
	trainer_id_lo = trainer_id & 0xff

	# xor the first four bytes with the high byte of trainer id
	new_mon_id = mon_id ^ trainer_id_hi
	new_move_1 = move_1 ^ trainer_id_hi
	new_move_2 = move_2 ^ trainer_id_hi
	new_move_3 = move_3 ^ trainer_id_hi

	# xor the next 5 bytes with the low byte of trainer id
	new_move_4     = move_4    	^ trainer_id_lo
	new_spdspc_iv  = spdspc_iv 	^ trainer_id_lo
	new_atkdef_iv  = atkdef_iv 	^ trainer_id_lo
	new_level      = level     	^ trainer_id_lo
	new_alt_sprite = alt_sprite ^ trainer_id_lo

	# generate two checksum bytes
	checksum_1 =  (new_mon_id    & 0x01) << 7
	checksum_1 += (new_move_1    & 0x02) << 5
	checksum_1 += (new_move_2    & 0x04) << 3
	checksum_1 += (new_move_3    & 0x08) << 1
	checksum_1 += (new_move_4    & 0x10) >> 1
	checksum_1 += (new_spdspc_iv & 0x20) >> 3
	checksum_1 += (new_atkdef_iv & 0x40) >> 5
	checksum_1 += (new_level     & 0x80) >> 7

	checksum_2 =  (new_alt_sprite & 0x08) << 4
	checksum_2 += (new_mon_id     & 0x10) << 2
	checksum_2 += (new_move_1     & 0x20)
	checksum_2 += (new_move_2     & 0x40) >> 2 
	checksum_2 += (new_move_3     & 0x80) >> 4
	checksum_2 += (new_move_4     & 0x01) << 2
	checksum_2 += (new_spdspc_iv  & 0x02)
	checksum_2 += (new_atkdef_iv  & 0x04) >> 2 

	checksum_3 = (new_mon_id + new_move_1 + new_move_2 + new_move_3 + new_move_4 + new_spdspc_iv \
					+ new_atkdef_iv + new_level + new_alt_sprite + trainer_id_hi) & 0xff

	checksum_4 = (new_mon_id + new_move_1 + new_move_2 + new_move_3 + new_move_4 + new_spdspc_iv \
					+ new_atkdef_iv + new_level + new_alt_sprite + trainer_id_lo) & 0xff

	return [
		new_mon_id,
		new_move_1,
		new_move_2,
		new_move_3,
		new_move_4,
		new_spdspc_iv,
		new_atkdef_iv,
		new_level,
		new_alt_sprite,
		checksum_1,
		checksum_2,
		checksum_3,
		checksum_4
	]
