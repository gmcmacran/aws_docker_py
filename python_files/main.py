###################################
# Overview
#
# Script to expose endpoints
###################################
import flask
from flask import request, jsonify
from scoring_functions import prediction_function
from joblib import load

clf = load('models/random_forest_model.joblib')

app = flask.Flask(__name__)
# app.config["DEBUG"] = True # Get hints from web page if it endpoint fails.

# os.chdir('S:/Python/projects/aws_docker_py/python_files')
# http://127.0.0.1:5000/scoreHere?json_input=[[0.0, 0.0]]
@app.route('/scoreHere', methods=['GET'])
def calc_scores():
    temp = request.args['json_input']
    out = prediction_function(json_input = temp, skmodel = clf)
    return jsonify(out)

app.run(host = "0.0.0.0", port = 5000)