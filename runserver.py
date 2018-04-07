"""
This script runs the dogpics_web application using a development server.
"""

from os import environ
from dogpics_web import app

if __name__ == '__main__':
    # HOST = environ.get('SERVER_HOST', 'localhost')
    HOST = '0.0.0.0'
    try:
        PORT = int(environ.get('SERVER_PORT', '80'))
    except ValueError:
        PORT = 80
    app.run(HOST, PORT)
