import json
import os
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

url = 'https://gateway-a.watsonplatform.net/visual-recognition/api'
api_key = 'f8c0c68b5a97fd9c15f3c4a4f4561511782689d5'

visual_recognition = VisualRecognitionV3('2018-04-08', api_key=api_key)
classifier_id = 'DOGSDOGSDOGSDOGS'

with open('placeholder.jpg') as file:
	possibleDoggo = file.read()

result = visual_recognition.classify(images_file=possibleDoggo,threshold='0.1',classifier_ids=[classifier_id,'default'])
print(json.dumps(result, indent=2))
