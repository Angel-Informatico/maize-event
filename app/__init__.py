from flask import Flask
import os

# Get the directory where this file is located
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, 
            static_folder=os.path.join(basedir, 'static'),
            static_url_path='/static',
            template_folder=os.path.join(basedir, 'templates'))
app.config.from_object('config')

from app import views
