# DOGPICS

## About

Welcome to DOGPICS! Our app is powered by Python+Flask, Imgur, IBM Watson Visual Recognition, and Google Cloud Platform.

We use IBM Watson to recognize if new pictures uploaded to Imgur feature a dog, and if so, we display them here! Dog lovers are sure to enjoy our good good boys.


## Inspiration

A couple of us were hanging out prior to HackPSU, discussing what we should try to do for our project.  One of us jokingly suggested making "Tinder for Dogs", but then we realized that a simple application to give users new pictures of dogs to look at would be great too!

## What it does

Welcome to DOGPICS, an app that displays pictures of dogs.  Our goal with this application is to pull recently uploaded images from Imgur, run image recognition on them to tell if they are pictures of dogs, and if so, display them to an end user.  A demo can be found at our website: https://dogpics.aquatints.org.  

WIP: Image Recognition, to know if picture is a dog or not


### Flowchart

![Backend Flowchart](https://raw.githubusercontent.com/aquatints/dogpics/master/img/BackendFlowchartNew.png) 

![Frontend Flowchart](https://raw.githubusercontent.com/aquatints/dogpics/master/img/FrontendFlowchart.png)

## How we built it
### Technologies Used

- Python 3
- Flask
- Imgur
- IBM Watson Visual Recognition
- Google Cloud Platform (for hosting)
- Github

## Challenges we ran into
- Learning how to do image recognition
- running out of API calls for Watson

## Accomplishments that we're proud of
- Creating a functioning application!
- Running the whole thing in the cloud
- Using our skills with these technologies to create something that adds a little extra happiness to someone's life

## What we learned
- How to host a Python-driven website in the cloud
- How to scrape Imgur for new images and move them to different directories

## What's next for dogpics
- We want to work more on our image recognition piece; figure out the optimal confidence level needed to pick out what is or isn't a dog (we found that sometimes cats slipped through)
- Pull higher resolution images from Imgur (thumbnails are getting pulled a lot)
