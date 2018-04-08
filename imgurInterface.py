import pyimgur
import requests
import os
import urllib.request

CLIENT_ID = 'd88ae1ac1e85343'

q = pyimgur.Imgur(CLIENT_ID)

# test space 
"""

image = q.get_image('5NR01Pc')

print(image.link)
"""

def dogdaemon():
	# Loop that gets new images
	# TODO LOGIC
	'''
	
	
	'''

def getImgurLatest():
	latestPageURL = 'https://imgur.com/r/pics'
	page = requests.get(latestPageURL)
	id = getID(page.text)
	#with urlopen('https://i.imgur.com/' + id + '.jpg') as url:
	#	i = url.read()
	urllib.request.urlretrieve('https://i.imgur.com/' + id + '.jpg', 'img/' + id + '.jpg')

def getID(page):
	# find imgur image ID
	tmpStartLoc = page.find("src=\"//i.imgur.com")
	startLoc = page.find("/", tmpStartLoc) + 14
	endLoc = page.find(".",startLoc)
	
	id = page[startLoc:endLoc]
	
	return id

getImgurLatest()
