"""
Routes and views for the flask application.
"""
import os
from os import walk
import random
from datetime import datetime
from flask import render_template
from dogpics_web import app
from flask import request

@app.route('/')
@app.route('/home')
def home():
	"""Renders the home page."""
	pic = getpics()
	return render_template(
		'index.html',
		title='DOGPICS',
		#dog='static/content/img/placeholder.jpg',
		dog=pic,
		srclink=getImgurLink(pic),
		#debug=getpics(),
		year=datetime.now().year,
	)

@app.route('/debug')
def debug():
	"""Renders inventory page for debugging and admin purposes"""
	allDogs = getAllDogs()
	allNotDogs = getAllNotDogs()
	allDiscarded = getAllDiscarded()
	print_inventory = ""
	print_notdogs = ""
	print_discarded = ""
	for i in allDogs:
		print_inventory += "<form action=\"/report\" method='post'><img src=\"/static/content/img/" + i + "\" width=150px><button type='submit' class='btn btn-danger'>Not a dog</button><input type='hidden' name='reportimg' value='/static/content/img/" + i + "'><input type='hidden' name='reporturl' value='https://imgur.com/" + i + "'></form><br><hr><br>"
	for i in allNotDogs:
		print_notdogs += "<img src='https://imgur.com/" + i + "' width=150px><br>"
	for i in allDiscarded:
		print_discarded += "<img src='https://imgur.com/" + i + "' width=150px><br>"
	return render_template(
		'overview.html',
		title='DOGPICS',
		year=datetime.now().year,
		inventory = print_inventory,
		dogcount = len(allDogs),
		discarded = print_discarded,
		discardcount = len(allDiscarded),
		notdog = print_notdogs,
		notdogcount = len(allNotDogs)
	)

def moveToDogs():
	#todo
	print("todo")

@app.route('/report', methods=['POST'])
def report():
	return render_template(
		'report.html',
		title='NOT A DOG?',
		dog=request.form['reportimg'],
		srclink=request.form['reporturl'],
		year=datetime.now().year
	)

@app.route('/reportConfirm', methods=['POST'])
def reportConfirm():
	# move to discard
	f = '/dogpics/web/dogpics/dogpics_web'+ request.form['reportimg']
	cutstr = '/img/'
	cutext = '.jpg'
	name = request.form['reportimg']
	name = name[name.index(cutstr)+len(cutstr):]
	os.rename(f, '/dogpics/backend/notdogs/'+name)
	"""Renders the home page."""
	pic = getpics()
	return render_template(
		'index.html',
		title='DOGPICS',
		dog=pic,
		srclink=getImgurLink(pic),
		year=datetime.now().year,
	)

def getpics():
	""" Return a picture """
	# temporarily return random picture from static/content/img/
	path = '/dogpics/web/dogpics/dogpics_web/static/content/img/'
	webpath = '/static/content/img/'
	# debug = os.listdir(path)
	items = os.listdir(path)
	picked = random.choice(items)
	return webpath+picked;

def getAllDogs():
	""" Return array of all items in dog folder """
	path = '/dogpics/web/dogpics/dogpics_web/static/content/img/'
	webpath = '/static/content/img/'
	dogs = []
	for(dirpath, dirnames, filenames) in walk(path):
		dogs.extend(filenames)
		break
	return dogs

def getAllNotDogs():
	""" Return array of items in user submitted 'not dogs' folder """
	path = '/dogpics/backend/notdogs/'
	notDogs = []
	for(dirpath, dirnames, filenames) in walk(path):
		notDogs.extend(filenames)
	return notDogs

def getAllDiscarded():
	""" return array of items in discard folder """
	path = '/dogpics/backend/discard/'
	discarded = []
	for(dirpath, dirnames, filenames) in walk(path):
		discarded.extend(filenames)
	return discarded

def getImgurLink(filename):
	# get imgur link
	print('DEBUG:' + filename)
	cutstr = '/img/'
	cutext = '.jpg'
	imgurlink = filename[filename.index(cutstr)+len(cutstr):] #filename.index(cutext)]
	return 'https://imgur.com/' + imgurlink
