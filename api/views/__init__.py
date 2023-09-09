from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix='/api/')

from api.views.vegetable_manager import *
from api.views.garden_area import *
from api.views.sensors import *