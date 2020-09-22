import logging
import typing as t
import joblib

import pandas as pd

try:
    from remain_time_pred.config import core
    from remain_time_pred.preprocessing.data_management import load_dataset,load_pipeline



except:
    from config import core
    from preprocessing.data_management import load_dataset,load_pipeline

_logger = logging.getLogger(__name__)
trc=core.trc

pipe_model=load_pipeline(trained_model_path=core.TRAINED_MODEL_PATH,
                         model_name=f"pipe_{trc.model_name}_{trc.model_version}")

ml_model=load_pipeline(trained_model_path=core.TRAINED_MODEL_PATH,
                         model_name=f"ml_{trc.model_name}_{trc.model_version}")

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
        
   



if __name__ == "__main__":
    
   


    test_data=load_dataset(core.DATASET_PATH,"test.csv")

    # Split train data
    X_ts=test_data.drop(columns=trc.target_name)
    y_ts=test_data[trc.target_name]
    """
    pipe_model=load_pipeline(trained_model_path=core.TRAINED_MODEL_PATH,
                             model_name=f"{trc.model_name}_{trc.model_version}")


    pred_ts=pipe_model.predict(X_ts)
    """
    path="/home/omer/Desktop/Works/remain_time_prediction/asas_mh_remain_time_pred_0.1.pkl"
    joblib.load(filename=path)
    #print(pred_ts)

