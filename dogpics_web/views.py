"""
Routes and views for the flask application.
"""
import os
import random
from datetime import datetime
from flask import render_template
from dogpics_web import app

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
