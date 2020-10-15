import logging
import typing as t
import joblib

import pandas as pd

from reg_model.config import config
from reg_model.preprocessing.data_management import load_dataset,load_pipeline

_logger = logging.getLogger(__name__)
trc=config.trc

pipe_model=load_pipeline(trained_model_path=config.TRAINED_MODEL_PATH,
                         model_name=f"pipe_{trc.model_name}_{trc.model_version}")

#print(pipe_model)

_version=trc.model_version

def make_prediction(data=None,version=_version):
    """Make a prediction using a saved model pipeline."""



    try:
        #results = _price_pipe.predict(X=data)
        
        #_logger.info(
        #    f"Making predictions with model version: {_version} "
        #    f"Predictions: {results}"
        #)
        
        return pipe_model.predict(X=data)
        
    except Exception as error:
        
        print(error)
        _logger.error(
            f"Making prediction error : {error}"
        )
        
   





