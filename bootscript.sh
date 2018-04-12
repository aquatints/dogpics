#!/bin/sh

screen -dm sudo python3 /dogpics/web/dogpics/runserver.py

sleep 1

screen -dm sudo python3 /dogpics/backend/dogpics/imgurInterface.py
