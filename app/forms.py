from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class TrainerIdForm(FlaskForm):
    trainer_id = StringField('trainer_id', validators=[DataRequired()])
    pokemon = SelectField(
        'pokemon',
        choices=[
            ('pikablue', 'Flying/Surfing Pikablue'),
            ('squirtle', 'Sunglasses Squirtle'),
            ('wartortle', 'Sunglasses Wartortle'),
            ('blastoise', 'Sunglasses Blastoise'),
            ('electrode', 'Headband Electrode'),
        ],
        default='pikablue',
    )

