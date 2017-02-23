from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from project import db

strains_blueprint = Blueprint(
	'strains',
	__name__,
	template_folder = 'templates')

@strains_blueprint.route('/home', methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		from IPython import embed; embed()
		print(request.data)

	return render_template('strains/strains.html')