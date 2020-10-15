import os 
from glob import glob
import pandas as pd 
import joblib 
from sklearn.pipeline import Pipeline
import logging

_logger = logging.getLogger(__name__)


def load_dataset(data_path:str,data_name:str)->pd.DataFrame:
    #paths=glob(data_path+"/*.csv")

    data_path=os.path.join(data_path,data_name)
    assert os.path.isfile(data_path) , f"data_path :{data_path} is not file"    
     
    df=pd.read_csv(data_path)
    #df_dict=[pd.read_csv]
    return df

def save_pipeline(*,pipeline_to_persist:Pipeline,trained_model_path:str,model_name:str)->None:
    
    """Persist the pipeline.

    Saves the versioned model, and overwrites any previous
    saved models. This ensures that when the package is
    published, there is only one trained model that can be
    called, and we know exactly how it was built.
    """
    # Prepare versioned save file name
    save_file_name=f"{model_name}.pkl"
    save_path=trained_model_path/save_file_name
    #save_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
    #save_path = TRAINED_MODEL_DIR / save_file_name

    #remove_old_pipelines(files_to_keep=[save_file_name])
    joblib.dump(pipeline_to_persist, save_path)
    _logger.info(f"saved pipeline: {save_file_name}")

def load_pipeline(*, trained_model_path:str,model_name:str) -> Pipeline:
    
    """
    Load a persisted pipeline.
    """

    file_name=f"{model_name}.pkl"
    file_path=trained_model_path/file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model