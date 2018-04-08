# DOGPICS

## Inspiration

A couple of us were hanging out prior to HackPSU, discussing what we should try to do for our project.  One of us jokingly suggested making "Tinder for Dogs", but then we realized that a simple application to give users new pictures of dogs to look at would be great too!

## What it does

Welcome to DOGPICS, an app that displays pictures of dogs.  Our goal with this application is to pull recently uploaded images from Imgur, run image recognition on them to tell if they are pictures of dogs, and if so, display them to an end user.  A demo can be found at our website: https://dogpics.aquatints.org.  

WIP: Image Recognition, to know if picture is a dog or not


### Flowchart


![Backend Flowchart](https://raw.githubusercontent.com/aquatints/dogpics/master/img/BackendFlowchart.png)

![Frontend Flowchart](https://raw.githubusercontent.com/aquatints/dogpics/master/img/FrontendFlowchart.png)

## How we built it
### Technologies Used

- Python (3)
- Flask
- Imgur
- IBM Watson Visual Recognition
- Google Cloud Platform (for hosting)
- Github

## Challenges we ran into
- Learning how to do image recognition

## Accomplishments that we're proud of
- Getting a working frontend and mostly working backend

## What we learned
- How to host a Python-drive website in the cloud
- How to scrape Imgur for new images and move them to different directories

## What's next for dogpics
- We want to work more on our image recognition piece. 
