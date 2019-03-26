"""
Testing projects that already exist.

Tutorial-testing-existing-project-live-81

Homepage and documentation:


License: GNU GENERAL PUBLIC LICENSE Version 3

"""

from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serealizer import configure as config_ma
from .books import bp_books


def create_app():
    """Create app method - Application Factorie. Return initial state of app"""
    
    # configure app
    app = Flask(__name__)

    # configure SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crudzin.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # configure DB and serealiser
    config_db(app)
    config_ma(app)

    # configure Migrations
    Migrate(app, app.db)

    # Register Blueprint books
    app.register_blueprint(bp_books)
    
    return app
