# coding=utf-8
from flask import Flask, jsonify

app = Flask(__name__)

# Configurations
app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
    # return "Error Message: {0}".format(error)
    response = {
        'success': False,
        'message': "Error Message: {0}".format(error)
    }

    return jsonify(response), 404

# Routes Register

# register post routers
from .blogs import blogs_route
app.register_blueprint(blogs_route)