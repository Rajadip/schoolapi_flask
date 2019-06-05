from flask import Flask
from schoolapi.extension import *


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    '''
        if instance_relative_config=True then reads
        following configuration file from instance folder.
        This provides the  private nature of the instance folder
    '''
    app.config.from_pyfile("config.py")

    db.init_app(app)
    migrate.init_app(app=app)

    with app.app_context():
        from schoolapi.user.route import user_blueprint
        app.register_blueprint(user_blueprint)

    return app
