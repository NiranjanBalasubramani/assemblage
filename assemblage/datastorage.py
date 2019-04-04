import sqlite3
from assemblage import app

def create_connection(database_file):
    """
    Creates a database connection to the specified database file.
    @param_in[database_file]: name of the database to connect to
    @return: connection_object
    """
    try:        
        connection = sqlite3.connect(database_file, isolation_level=None)
        app.logger.debug("DEBUG: Database connection successful")
        return connection
    except Exception as ex:        
        app.logger.debug("ERROR: Database connection failed: {}".format(ex))
        return None

def query_admin(db_object, admin_query):
    """
    Returns the list of admins.
    """
    admin_details = dict()
    pointer = db_object.cursor()
    pointer.execute(admin_query)
    rows = pointer.fetchall()
    for row in rows:
        row = list(row)
        admin_details[row[0]] = row[1]
    return admin_details

def query(db_object, query):
    """
    Returns the list of books.
    """    
    pointer = db_object.cursor()    
    pointer.execute(query)    
    rows = pointer.fetchall()    
    return rows

def add(db_object, add_query,items):
    """
    Inserts the list of books to the db.
    """    
    pointer = db_object.cursor()    
    pointer.execute(add_query,items)
    rows = pointer.fetchall()    
    return rows

def delete(db_object, delete_query):
    """
    Deletes the list of books from the db.
    """    
    pointer = db_object.cursor()    
    pointer.execute(delete_query)
    rows = pointer.fetchall()
    return rows

def query_user(db_object, user_query):
    """
    Returns the list of admins.
    """
    print("inside quering")
    user_details = dict()
    pointer = db_object.cursor()
    pointer.execute(user_query)
    rows = pointer.fetchall()
    for row in rows:
        row = list(row)
        user_details[row[0]] = row[1]
    return user_details

def update_book(db_object, query):
    """
    Returns the list of books.
    """    
    pointer = db_object.cursor()    
    pointer.execute(query)    
    rows = pointer.fetchall()    
    return rows