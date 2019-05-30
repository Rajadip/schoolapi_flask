from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    '''
        if instance_relative_config=True then reads
        following configuration file from instance folder.
        This provides the  private nature of the instance folder
    '''
    app.config.from_pyfile("config.py")

    return app
