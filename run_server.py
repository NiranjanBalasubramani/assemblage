"""
Entry point for the application.
@author Niranjan Balasubramani
@email niranjany5070@gmail.com
@date 03-04-2019
"""

from assemblage import app

if __name__ == '__main__':
    app.run(host=app.config.get('APP_HOST'),
            port=app.config.get('APP_PORT'),
            debug=app.config.get('APP_DEBUG'))
