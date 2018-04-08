"""
Routes and views for the flask application.
"""
import os
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

@app.route('/report', methods=['POST'])
def report():
	# todo report logic
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
	os.rename(f, '/dogpics/backend/discard/notadog.jpg')
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

def getImgurLink(filename):
	# get imgur link
	print('DEBUG:' + filename)
	cutstr = '/img/'
	cutext = '.jpg'
	imgurlink = filename[filename.index(cutstr)+len(cutstr):] #filename.index(cutext)]
	return 'https://imgur.com/' + imgurlink
