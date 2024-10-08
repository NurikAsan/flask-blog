from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from config import config
from flask_moment import Moment
from flask_pagedown import PageDown

db = SQLAlchemy()
login_manager = LoginManager()
boostrap = Bootstrap()
moment = Moment()
mail = Mail()
pagedown = PageDown()
login_manager.login_view = 'auth.login'


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    login_manager.init_app(app)
    boostrap.init_app(app)
    moment.init_app(app)
    pagedown.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    return app
