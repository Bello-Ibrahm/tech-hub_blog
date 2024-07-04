#!/usr/bin/python3
""" Flask Application """
from models import storage
from os import getenv
from api.v1.views import app_views
#from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
import sys
from os.path import abspath, dirname


app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 
    404 Error
    """
    return make_response(jsonify({'error': "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'Tech-Hub Blog Restful API',
    'uiversion': 3
}

Swagger(app)


if __name__ == "__main__":
    """ Main Function """
    host = getenv('TECH_HUB_API_HOST', '0.0.0.0')
    port = getenv('TECH_HUB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
