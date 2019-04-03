"""
Views for the app containing all the routes.
@author Niranjan Balasubramani
@email niranjany5070@gmail.com
@date 03-04-2019
"""

from assemblage import app
from flask import json, jsonify, request
import re
import os
import datetime
from assemblage import datastorage

db_file = app.config.get('DATABASE_FILE')
db_object = datastorage.create_connection(db_file)

@app.route('/')
@app.route('/health')
def index():
    """
    Health URL.
    Returns the json if the flask app is up and running.
    @return: message string
    """
    app.logger.debug("Health URL requested.")
    now = datetime.datetime.utcnow().isoformat()
    return jsonify({
        'alive': True,
        'last_updated': now,
        'version': app.config.get("APP_VERSION"),
        'message': 'Hello SignEasy, your Library Management system is up and running.'}), 200    