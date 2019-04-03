import sqlite3
from assemblage import app

def create_connection(database_file):
    """
    Creates a database connection to the specified database file.
    @param_in[database_file]: name of the database to connect to
    @return: connection_object
    """
    try:        
        connection = sqlite3.connect(database_file)
        app.logger.debug("DEBUG: Database connection successful")
        return connection
    except Exception as ex:        
        app.logger.debug("ERROR: Database connection failed: {}".format(ex))
        return None
