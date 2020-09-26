import os 
from pathlib import Path
import typing as t

from pydantic import BaseModel, validator
from strictyaml import load, YAML

# if it import at root directory


CONFIG_MODULE_PATH = Path(__file__).resolve().parent
PACKAGE_PATH = CONFIG_MODULE_PATH.parent
TRAIN_CONFIG_FILE_PATH = PACKAGE_PATH/"train_config.yml"
FEATURE_CONFIG_FILE_PATH = PACKAGE_PATH/"feature_config.yml"
DATASET_PATH = PACKAGE_PATH/"datasets"
TRAINED_MODEL_PATH=PACKAGE_PATH/"trained_model"
ROOT_PATH = PACKAGE_PATH.parent




        
        
class TrainConfig(BaseModel):
    """
    Training configs
    """
    # data info
    data_path:str
    training_data_name:str
    test_data_name:str

    # model info
    target_name:str
    model_name:str
    model_version:str

    
        

class FeatureConfig(BaseModel):
    """
    Feature Engineering configs
    """
    # feature types
    num_attribs:t.Sequence[str]   
    cat_attribs:t.Sequence[str]  
    
    # processing function parameters
    imputer_strategy:str
    
    
    
def fetch_config_from_yaml(cfg_path: Path = None) -> YAML:
    """Parse YAML containing the package configuration."""

    if not cfg_path:
        raise Exception(f"'cfg_path' is not exist")
    
    else :
        if cfg_path.is_file():
            with open(cfg_path, "r") as conf_file:
                parsed_config = load(conf_file.read())
                return parsed_config
        else:
            raise Exception(f"{cfg_path} is not file path")
    
    


def create_train_config(parsed_config: YAML = None):
    """create train on config values."""
    
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml(TRAIN_CONFIG_FILE_PATH)
    
    return TrainConfig(**parsed_config.data)


def create_feature_config(parsed_config: YAML = None):
    """create feature engineering on config values."""
    
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml(FEATURE_CONFIG_FILE_PATH)
    
    return FeatureConfig(**parsed_config.data)



# train config
trc=create_train_config()

# feature config
ftc=create_feature_config()