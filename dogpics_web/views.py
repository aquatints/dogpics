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
	return render_template(
		'index.html',
		title='DOGPICS',
		#dog='static/content/img/placeholder.jpg',
		dog=getpics(),
		#debug=getpics(),
		year=datetime.now().year,
	)

@app.route('/contact')
def contact():
	"""Renders the contact page."""
	return render_template(
		'contact.html',
		title='Contact',
		year=datetime.now().year,
		message='Your contact page.'
	)

@app.route('/about')
def about():
	"""Renders the about page."""
	return render_template(
		'about.html',
		title='About',
		year=datetime.now().year,
		message='Your application description page.'
	)

def getpics():
	""" Return a picture """
	# temporarily return random picture from static/content/img/
	path = '/dogpics/web/dogpics/dogpics_web/static/content/img/'
	webpath = '/static/content/img/'
	debug = os.listdir(path)
	items = os.listdir(path)
	picked = random.choice(items)
	return webpath+picked;
