from flask import Blueprint

health_api = Blueprint('health_api', __name__)

from . import views