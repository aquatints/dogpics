import pyimgur
import requests
import os
import urllib.request
import time
import random
import watson

CLIENT_ID = 'd88ae1ac1e85343'

q = pyimgur.Imgur(CLIENT_ID)

sleepTime = 5 # normally 5
maxFilesInDir=30 # normally 100
imgurLink = 'https://imgur.com/new/time' # default is /r/pics
prod = True # if in production mode

def dogdaemon():
	# Loop that gets new images
	pathToWebPics = '/dogpics/web/dogpics/dogpics_web/static/content/img/'
	pathToDogs = '/dogpics/backend/dogs/'
	pathToDiscard = '/dogpics/backend/discard/'
	pathToLimbo = '/dogpics/backend/limbo/'
	while True:
		# get existing
		filesInDogs = os.listdir(pathToDogs)
		numFilesInDogs = len(filesInDogs)
		filesInDiscard = os.listdir(pathToDiscard)
		numFilesInDiscard = len(filesInDiscard)
		filesInProd = os.listdir(pathToWebPics)
		numFilesInProd = len(filesInProd)

		# print debug info
		print('files in dogs dir: ' + str(filesInDogs))
		print('num files in dogs dir: ' + str(numFilesInDogs))
		print('files in discard dir: ' + str(filesInDiscard))
		print('num files in discard dir: ' + str(numFilesInDiscard))
		print('files in prod dogs dir: ' + str(filesInProd))
		print('num files in prod dogs dir: ' + str(numFilesInProd))
		print()

		# check existing number, remove if too much
		if(numFilesInDogs > maxFilesInDir):
			purgePick = random.choice(filesInProd)
			os.remove(pathToWebPics + str(purgePick))
			print('REMOVED: ' + pathToWebPics + str(purgePick))
			print()
		if(numFilesInDogs > maxFilesInDir):
			purgePick = random.choice(filesInDogs)
			os.remove(pathToDogs + str(purgePick))
			print('REMOVED: ' + pathToDogs + str(purgePick))
			print()
		if(numFilesInDiscard > maxFilesInDir):
			purgePick = random.choice(filesInDiscard)
			os.remove(pathToDiscard + str(purgePick))
			print('REMOVED: ' + pathToDiscard + str(purgePick))
			print()

		# get image
		getImgurLatest()

		# if image is dog, save to dog path. If not, save to discard path
		if not (len(os.listdir(pathToLimbo))==0):
			#print('TODO: IMAGE RECOGNITION HERE')
			#print()
			f = str(os.listdir(pathToLimbo)[0])
			isDog = watson.isADog('https://i.imgur.com/'+f+'.jpg')
			
			if(isDog):
				os.rename(pathToLimbo + f, pathToDogs + f)
			else:
				os.rename(pathToLimbo + f, pathToDiscard + f)


		# FIXME - remove 'allow all' when above is implemented
		#if not (len(os.listdir(pathToLimbo))==0):
		#	f = str(os.listdir(pathToLimbo)[0])
		#	os.rename(pathToLimbo + f, pathToDogs + f)
		#	print('MOVED: ' + pathToLimbo + f + '.jpg to ' + pathToDogs + f + '.jpg')
		#	print()

		# move files to web if enabled at top
		if(prod):
			if not (len(filesInDogs)==0):
				f = str(os.listdir(pathToDogs)[0])
				os.rename(pathToDogs + f, pathToWebPics + f)
				print('MOVED: ' + pathToDogs + f + ' to ' + pathToWebPics + f)
				print()

		# wait 5 seconds before doing again
		print('---------------------------------')
		time.sleep(sleepTime)

def getImgurLatest():
	# save new images to limbo directory
	pathToWebPics = '/dogpics/web/dogpics/dogpics_web/static/content/img/'
	pathToDogs = '/dogpics/backend/dogs/'
	pathToDiscard = '/dogpics/backend/discard/'
	limboDir = '/dogpics/backend/limbo/'
	latestPageURL = imgurLink
	# latestPageURL = 'https://imgur.com/new/time' # temporary testing to see if it can handle more images coming in
	page = requests.get(latestPageURL)
	id = getID(page.text)
	if(os.path.isfile(pathToDogs + id + '.jpg')) or (os.path.isfile(pathToDiscard + id + '.jpg')) or (os.path.isfile(pathToWebPics + id + '.jpg')):
		print('Latest Imgur File Existed Already! Skipping!')
	else:
		urllib.request.urlretrieve('https://i.imgur.com/' + id + '.jpg', limboDir + id + '.jpg')
		print('SAVED: https://i.imgur.com/' + id + '.jpg to ' + limboDir + id + '.jpg')
		print()

def getID(page):
	# find imgur image ID
	tmpStartLoc = page.find("src=\"//i.imgur.com")
	startLoc = page.find("/", tmpStartLoc) + 14
	endLoc = page.find(".",startLoc)

	id = page[startLoc:endLoc]

	return id

dogdaemon()
