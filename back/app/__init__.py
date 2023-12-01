from flask import Flask

from config import Config
from app.extensions import db


def create_app(config_class=Config, config_overrides=None):
    app = Flask(__name__)
    
    app.config.from_object(config_class)
    if config_overrides:
        app.config.update(config_overrides)
    
    db.init_app(app)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
