import os

class BaseConfig(object):
    """
    Generic configuration file.
    @author Niranjan Balasubramani
    @email  niranjany5070@gmail.com
    @date   03-04-2019
    """
    APP_NAME = 'ASSEMBLAGE'
    APP_VERSION = '0.1'
    APP_HOST = os.environ.get('CONFIG_SYNC_HOST','0.0.0.0')
    APP_PORT = int(os.environ.get('CONFIG_SYNC_PORT',5025))
    APP_DEBUG = True
    DATABASE_FILE = '/var/www/apps/github/assemblage/LibraryData.db'
    LOG_FILE = '/var/log/apps/assemblage/application.log'

    # Queries
    ADMIN_TABLE = "admin"
    ADMINS = "SELECT * FROM {}"
    BOOKS_TABLE = "booksinfo"
    BOOKS_INFO = "SELECT * FROM {} WHERE availability=1"
    BOOKS_UPDATE = "UPDATE booksinfo SET availability = 0 WHERE book_isbn = '{}'";
    BOOKS_UPDATE_1 = "UPDATE booksinfo SET availability = 1 WHERE book_isbn = '{}'";
    BOOKS_DATA = "SELECT * FROM booksinfo WHERE book_isbn = '{}'"
    ADD_BOOK = "INSERT INTO booksinfo (book_isbn,book_title,book_author) values (?,?,?)"
    DELETE_BOOK = "DELETE FROM booksinfo WHERE book_isbn='{}'"
    USERS_TABLE = "users"    
    USERS_INFO = "SELECT * FROM {}"
    ADD_USER = "INSERT INTO users (first_name,last_name,email_id,phone) values (?,?,?,?)"
    DELETE_USER = "DELETE FROM users WHERE uid={}"
    BORROW_TABLE = "borrowinfo"
    BORROW_DATA = "INSERT INTO borrowinfo (b_id,b_isbn,b_title,u_id,u_name,issue_date,expiry_date) values(?,?,?,?,?,?,?)"
    BORROW_HISTORY = "SELECT b_isbn,b_title,issue_date,expiry_date FROM borrowinfo where u_id={}"
    BORROW_HISTORY_1 = "SELECT b_isbn,u_id,u_name,issue_date FROM borrowinfo where b_isbn='{}'"
    RETURN_BOOK = "INSERT INTO returninfo (r_id,b_isbn,u_id,u_name,issue_date,return_date) values (?,?,?,?,?,?)"

    # Info 
    NO_OF_DAYS = 7


class ProductionConfig(BaseConfig):
    """
    Production specific configurations.
    """

class StagingConfig(BaseConfig):    
    """
    Staging specific configurations.
    """

class DeveloperConfig(BaseConfig):
    """
    Developer specific configurations.
    """