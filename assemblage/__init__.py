"""
The application context file. 
@author Niranjan Balasubramani
@email niranjany5070@gmail.com
@date 03-04-2019
"""

from flask import Flask
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# create the app object
app = Flask(__name__)

env=environ.get("ENV")

if env == "PROD":
    app.config.from_object('config.ProductionConfig')
    log_level = logging.INFO
elif env == "STAG":
    app.config.from_object("config.StagingConfig")
    log_level = logging.DEBUG
else:
    app.config.from_object("config.DeveloperConfig")
    log_level = logging.DEBUG


handler = RotatingFileHandler(app.config.get("LOG_FILE"), maxBytes=10000000, backupCount=5)
app.logger.addHandler(handler)
app.logger.setLevel(log_level)

from assemblage import views