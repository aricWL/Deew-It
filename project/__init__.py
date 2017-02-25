from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


if os.environ.get('ENV') == 'production':
    debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
else:
    debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/deewit'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "shhhh"
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)

from project.strains.views import strains_blueprint

app.register_blueprint(strains_blueprint, url_prefix='/strains')

@app.route('/')
def root():
    return redirect('/strains/home')

