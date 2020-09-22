import logging
import pandas as pd 

try:
    from remain_time_pred import pipeline as pi
    from remain_time_pred.preprocessing.data_management import load_dataset
    from remain_time_pred.config import core

except:
    import pipeline as pi
    from preprocessing.data_management import load_dataset
    from config import core

import logging

_logger=logging.getLogger(__name__)

# Load config file
pdc=core.pdc

def run_prepare_data()->None:
    "Run prepare data pipeline for getting train ,val and test data "

    data=load_dataset(core.DATASET_PATH,pdc.raw_data_name)

    pi.data_prepare_pipe.fit_transform(data)



if __name__ == "__main__":
    run_prepare_data()