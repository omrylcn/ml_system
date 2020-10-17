from flask import Blueprint, request, jsonify

import numpy as np
import pandas as pd 
import pickle
#from reg_model.predict import make_prediction
#from reg_model import __version__ as _version


from api.config import get_logger
from api.validation import validate_inputs
from api import __version__ as api_version
print(api_version)



_logger = get_logger(logger_name=__name__)


prediction_app = Blueprint('prediction_app', __name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'

_version="0.1" # dummy version

@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({#'model_version': _version,
                        'api_version': api_version})



@prediction_app.route('/test', methods=['POST'])
def test():
    if request.method == "POST":
        #data=request.get_json()
        #image=np.array(data["image"])
        image = pickle.loads(request.get_data())
        print(image.shape)
    return "ok"


@prediction_app.route('/v1/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Step 1: Extract POST data from request body as JSON
        json_data = request.get_json()
        
        _logger.debug(f'Inputs: {json_data}')

        #Step 2: Validate the input using marshmallow schema
        input_data, errors = validate_inputs(input_data=json_data)
        print(errors)
        
        print(input_data)
        print(type(input_data)) 

        # Step 3: Model prediction
        # convert data to pandas.DataFrame
        data=pd.DataFrame(input_data)
        result=make_prediction(data=data)
        _logger.debug(f'Outputs: {result}')
        
        # Step 4: Return the response as JSON
        return jsonify({"state":"ok",
                        "return":result.tolist(),
                        "errors":errors})

        