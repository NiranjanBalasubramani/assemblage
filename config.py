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