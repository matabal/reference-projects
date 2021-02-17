import os

from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

def create_app(config_mode):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    
    app.config.from_object(config[config_mode])
    config[config_mode].init_app(app)

    
    from .web import register_web_blueprints
    register_web_blueprints(app)
    
    from .api import register_api_blueprints
    register_api_blueprints(app)

    # Initialize database
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    return app