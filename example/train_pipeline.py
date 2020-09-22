import warnings 
warnings.filterwarnings("ignore")

import pandas
import logging
from sklearn.metrics import r2_score
from lightgbm import LGBMRegressor

try:
    from remain_time_pred import pipeline as pi
    from remain_time_pred.preprocessing.data_management import load_dataset,save_pipeline,save_model
    from remain_time_pred.config import core
    

except  Exception as import_error:
    print(import_error)
    import pipeline as pi
    from preprocessing.data_management import load_dataset,save_pipeline,save_model
    from config import core

import logging

_logger=logging.getLogger(__name__)

# Load config file
trc=core.trc


def run_train()->None:
    
    """
    It is a  function that is pipeline to train model with prepared data
    
    """
    
    # Get train and validation data
    train_data=load_dataset(core.DATASET_PATH,trc.training_data_name)
    val_data=load_dataset(core.DATASET_PATH,trc.validation_data_name)

    # Split train data
    X_tr=train_data.drop(columns=trc.target_name)
    y_tr=train_data[trc.target_name]
    
    # Split validation data
    X_val=val_data.drop(columns=trc.target_name)
    y_val=val_data[trc.target_name]


    # Train model
    pi.train_pipeline.fit(X_tr,y_tr)

    # Evaluate R2 score for validation data
    pred_val=pi.train_pipeline.predict(X_val)
    print("Validataion R2 score :",r2_score(y_val,pred_val))

    save_pipeline(pipeline_to_persist=pi.train_pipeline,
                  trained_model_path=core.TRAINED_MODEL_PATH,
                  model_name=f"pipe_{trc.model_name}_{trc.model_version}")
    
    print("Training is done :)")
    

def run_train_as_seperate(X_tr=None,y_tr=None,X_val=None,y_val=None,model=None,ret=False):
    
    """
    "prepare data pipeline" and model are seperate
    
    """
    
    # Get train and validation data
    
    if X_tr == None or y_tr ==None:
        
        train_data = load_dataset(core.DATASET_PATH,trc.training_data_name)
        X_tr = pi.predata_for_train_pipeline.fit_transform(train_data)
        y_tr = train_data[trc.target_name]
    
    
    if X_val == None or y_val ==None:
        
        val_data=load_dataset(core.DATASET_PATH,trc.validation_data_name)
        X_val = pi.predata_for_train_pipeline.fit_transform(val_data)
        y_val=val_data[trc.target_name]
        
    if model==None:
        model=LGBMRegressor()
    
    # Train model
    model.fit(X_tr,y_tr)

    # Evaluate R2 score for validation data
    pred_val=model.predict(X_val)
    print("Validataion R2 score :",r2_score(y_val,pred_val))

    save_model(model=model,
               trained_model_path=core.TRAINED_MODEL_PATH,
               model_name=f"ml_{trc.model_name}_{trc.model_version}")
    
    if ret == False:
        
        print("Training is done :)")
        return 
    else:
        print("Training is done :)")
        return X_tr,y_tr,X_val,y_val,model

if __name__ == "__main__":
    run_train()
    