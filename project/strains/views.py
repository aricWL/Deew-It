from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, jsonify
from project import db
from scraper import Strain


strains_blueprint = Blueprint(
	'strains',
	__name__,
	template_folder = 'templates')



@strains_blueprint.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('strains/strains.html')


@strains_blueprint.route('/results', methods=['GET', 'POST'])
def results():
	raw = request.args.get('info')
	raw = raw.replace("[", "")
	raw = raw.replace(']', '')
	raw = raw.replace('"', '')
	raw = raw.replace(',', '')
	data = list(raw)
	one = ['f', 't', 't', 't', 't', 't', 't', 't']
	two = ['t', 't', 't', 't', 't', 'f', 't', 't']
	three = ['t', 't', 't', 'f', 't', 't', 't', 't']
	four = ['f', 't', 't', 'f', 't', 'f', 't', 't']
	five = ['t', 't', 't', 'f', 't', 'f', 't', 't']
	six = ['f', 't', 't', 'f', 't', 't', 't', 't']
	seven = ['f', 't', 't', 't', 't', 'f', 't', 't']
	eight = ['t', 't', 't', 't', 't', 't', 't', 't']
	onecount = 0
	twocount = 0
	threecount = 0
	fourcount = 0
	fivecount = 0
	sixcount = 0
	sevencount = 0
	eightcount = 0

	for idx, val in enumerate(data):
		if data[idx] == one[idx]:
			onecount+=1
	for idx, val in enumerate(data):
		if data[idx] == two[idx]:
			twocount+=1
	for idx, val in enumerate(data):
		if data[idx] == three[idx]:
			threecount+=1
	for idx, val in enumerate(data):
		if data[idx] == four[idx]:
			fourcount+=1
	for idx, val in enumerate(data):
		if data[idx] == five[idx]:
			fivecount+=1
	for idx, val in enumerate(data):
		if data[idx] == six[idx]:
			sixcount+=1
	for idx, val in enumerate(data):
		if data[idx] == seven[idx]:
			sevencount+=1
	for idx, val in enumerate(data):
		if data[idx] == eight[idx]:
			eightcount+=1

	
	querytype = max(onecount, twocount, threecount, fourcount, fivecount, sixcount, sevencount, eightcount)

	if onecount == querytype:
		results = Strain.query.filter_by(inflammation=False, headache=True, spasm=True, appetite=True, anxiety=True, depression=True, insomnia=True, pain=True).limit(3).all()
		return render_template('strains/results.html', results=results)

	if twocount == querytype:
		results = Strain.query.filter_by(inflammation=True, headache=True, spasm=True, appetite=True, anxiety=True, depression=False, insomnia=True, pain=True).limit(3).all()
		return render_template('strains/results.html', results=results)

	if threecount == querytype:
		results = Strain.query.filter_by(inflammation=True, headache=True, spasm=True, appetite=False, anxiety=True, depression=True, insomnia=True, pain=True).limit(3).all()
		return render_template('strains/results.html', results=results)

	if fourcount == querytype:
		results = Strain.query.filter_by(inflammation=False, headache=True, spasm=True, appetite=False, anxiety=True, depression=False, insomnia=True, pain=True).limit(3).all()
		return render_template('strains/results.html', results=results)

	if fivecount == querytype:
		results = Strain.query.filter_by(inflammation=True, headache=True, spasm=True, appetite=False, anxiety=True, depression=False, insomnia=True, pain=True).limit(3).all()
		return render_template('strains/results.html', results=results)

	if sixcount == querytype:
		results = Strain.query.filter_by(inflammation=False, headache=True, spasm=True, appetite=False, anxiety=True, depression=True, insomnia=True, pain=True).limit(3).all()
		return render_template('strains/results.html', results=results)

	if sevencount == querytype:
		results = Strain.query.filter_by(inflammation=False, headache=True, spasm=True, appetite=True, anxiety=True, depression=False, insomnia=True, pain=True).limit(3).all()
		return render_template('strains/results.html', results=results)

	if eightcount == querytype:
		results = Strain.query.filter_by(inflammation=True, headache=True, spasm=True, appetite=True, anxiety=True, depression=True, insomnia=True, pain=True).limit(3).all()
		return render_template('strains/results.html', results=results)


	from IPython import embed; embed()
	pass

@strains_blueprint.route('/show')
def show():
	strains = Strain.query.all()
	return render_template('strains/show.html', strains=strains)

@strains_blueprint.route('/about')
def about():
	return render_template('strains/about.html')

@strains_blueprint.route('/contact')
def contact():
	return render_template('strains/contact.html')



