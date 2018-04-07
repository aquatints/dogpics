"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import dogpics_web.views
