import warnings 
warnings.filterwarnings("ignore")


import pandas
import logging
from sklearn.pipeline import make_pipeline,Pipeline
from sklearn.model_selection import cross_val_score,cross_validate,cross_val_predict

from reg_model import pipeline
from reg_model.config import config
from reg_model.preprocessing.data_management import load_dataset,save_pipeline

# set logger
_logger=logging.getLogger(__name__)

# load config file
trc=config.trc


def run_train()->None:

   # load data 
    train_data=load_dataset(config.DATASET_PATH,trc.training_data_name)

    # Split train data 
    X_tr=train_data.drop(columns=trc.target_name)
    y_tr=train_data[trc.target_name]

    # load ml model pipeline 
    m_pipe=pipeline.full_pipeline

    # train data with cross validation
    results=cross_validate(m_pipe,X_tr,y_tr,scoring=trc.model_metrics)

    # val score 
    #print(f"Test data {trc.model_metrics[0]}: results",results["test_"+trc.model_metrics[0]])
    _logger.info(f"Test data {trc.model_metrics[0]}: results",results["test_"+trc.model_metrics[0]])

    # save model pipeline
    save_pipeline(pipeline_to_persist=m_pipe,
                      trained_model_path=config.TRAINED_MODEL_PATH,
                      model_name=f"pipe_{trc.model_name}_{trc.model_version}")