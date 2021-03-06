from flask import Blueprint
from flask_restplus import Api

from app.main.controller.kwe_controller import api as kwe_namespace

blueprint = Blueprint('sw7-keyword-extraction-api', __name__)

api = Api(blueprint, title='SentiCloud Keyword Extraction', version='1.0',
          authorizations={'key': {'type': 'apiKey', 'in': 'header', 'name': 'Authorization'}})

# Add namespaces to API
api.add_namespace(kwe_namespace, path='/')