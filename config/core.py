from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    setup_blueprints(app)
    return app


def setup_blueprints(app):

    from api import health_api
    app.register_blueprint(health_api,url_prefix="/health")
    



def cleanup_app():
    pass