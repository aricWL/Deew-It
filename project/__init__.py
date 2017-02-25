from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


if os.environ.get('ENV') == 'production':
    debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgres://erxpsqntjrpnof:30f5e1cc2e58a3ebb40d6f5b664e0e5e4854f203fe24d03e8fe7d76508e2110d@ec2-23-21-76-49.compute-1.amazonaws.com:5432/d2juupr3u8h2rs')
else:
    debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/deewit'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "STRING"
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)

from project.strains.views import strains_blueprint

app.register_blueprint(strains_blueprint, url_prefix='/strains')

@app.route('/')
def root():
    return redirect('/strains/home')

