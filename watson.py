#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException
import sys

url = 'https://gateway-a.watsonplatform.net/visual-recognition/api'
api_key = 'f8c0c68b5a97fd9c15f3c4a4f4561511782689d5' #old
# api_key = 'b8d54b615a0ddc77f5091dc0a0d6ec0469e9d8f5'

visual_recognition = VisualRecognitionV3('2018-04-08', api_key=api_key)
classifier_id = 'DOGSDOGSDOGSDOGS'

confidence_threshold = 0.84 # default

def isADog(urlToImg):
	result = visual_recognition.classify(parameters=json.dumps({'url': urlToImg}))

	data = result

	confidentDog = False

	for i in range(0,2):
		if('dog' in data["images"][0]['classifiers'][0]['classes'][i]['class']) and (data["images"][0]['classifiers'][0]['classes'][i]['score']>=confidence_threshold):
			confidentDog = True

	return confidentDog

