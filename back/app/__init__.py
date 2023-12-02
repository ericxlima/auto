from flask import Flask

from config import Config
from app.extensions import db

def create_app(config_class=Config, *args, **kwargs):
    app = Flask(__name__)
    
    app.config.from_object(config_class)

    if kwargs:
        app.config.update(kwargs)
    
    db.init_app(app)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/api/v1')

    from app.automations import bp as automations_bp
    app.register_blueprint(automations_bp, url_prefix='/api/v1/automations')

    return app
