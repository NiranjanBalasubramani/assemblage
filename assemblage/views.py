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

@app.route('/')
@app.route('/health')
@app.route('/v1/health')
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

@app.route('/v1/book_info')
def book_info():
    """
    API that returns library info.
    @return: json value of all the available and unavailable books in the library. 
    """
    try:        
        db_object = datastorage.create_connection(db_file)
        request_data = request.json
        admin_details = check_admin()
        admin_name = request_data.get('user_name')
        admin_id = request_data.get('user_id')
        if admin_details.get(admin_id):
            books_table = app.config.get('BOOKS_TABLE')
            books_query = app.config.get('BOOKS_INFO').format(books_table)            
            books_details = datastorage.query_books(db_object,books_query)
            data = []
            for books in books_details:                
                books = list(books)
                book_data = {
                    "book_isbn" : books[0],
                    "book_name" : books[1],
                    "book_author" : books[2]
                }
                data.append(book_data)
            response = {
                "http_status": 200,
                "success": True,
                "data": data
            }
            return jsonify(response),200
        else: 
            response = {
                "message" : "User doesn't have access to check available books.",
                "http_status": 403,
                "success": False                
            }
            return jsonify(response),403
                
    except Exception as ex: 
        app.logger.debug("Server threw an exception: {}".format(ex))
        return 500
  
@app.route('/v1/add_book', methods=["POST"])
def add_book():
    """
    API that adds books to the library.
    @return: 201 created if books have been successfully added to the library.  
    """

@app.route('/v1/delete_book', methods=["DELETE"])
def delete_book():
    """
    API that removes a book from the library.
    @return: 204 No Content. 
    """

@app.route('/v1/manage_users')
def manage_users():
    """
    API that returns user info.
    @return: json value of all the users who can access the library of books. 
    """

@app.route('/v1/add_user', methods=["POST"])
def add_user():
    """
    API that adds users to the library.
    @return: 201 created if users have been successfully added to the library.  
    """

@app.route('/v1/delete_user', methods=["DELETE"])
def delete_user():
    """
    API that removes a user from library access.
    @return: 204 No Content. 
    """

@app.route('/v1/borrow_book', methods=["POST"])
def borrow_book():
    """
    API that allows users to borrow books from the library.
    @return: json value consisting of issue_date and expiry_date of the book along with its info. 
    """
@app.route('/v1/return_book', methods=["PUT"])
def return_book():
    """
    API that allows users to return books to the library.
    @return: json value with return_id.
    """

@app.route('/v1/book_history')
def book_history():
    """
    API that returns book history of the user.
    @return: json value of all the books borrowed and returned by the user. 
    """
def check_admin():
    db_object = datastorage.create_connection(db_file)
    # pointer = db_object.cursor()
    admin_table = app.config.get('ADMIN_TABLE')
    admin_query = app.config.get('ADMINS').format(admin_table)
    admin_details = datastorage.query_admin(db_object,admin_query)
    return admin_details