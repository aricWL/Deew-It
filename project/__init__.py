from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
CsrfProtect(app)

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