from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


if os.environ.get('ENV') == 'production':
    debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgres://joydqifyvytida:2e7a9221223490dcf6f68c84290720e823167f2e4afd6cdab5c586cd3451662e@ec2-23-21-220-23.compute-1.amazonaws.com:5432/d93iv159s51mpg')
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

