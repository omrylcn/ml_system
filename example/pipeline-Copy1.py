import warnings 
warnings.filterwarnings("ignore")

import os 
import logging
import json


from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from lightgbm import LGBMRegressor


try:
    from remain_time_pred.preprocessing import preprocessors as pp
    from remain_time_pred.preprocessing import features as  ft #RoofProcess,GasProcess
    from remain_time_pred.config import core

except:
    from preprocessing import preprocessors as pp
    from preprocessing import features as ft
    from config import core



#from functions_for_revoanalytics import split_dataframe_by_minutes

_logger = logging.getLogger(__name__)


# Load  config files 
pdc=core.pdc
trc=core.trc
ftc=core.ftc

data_prepare_pipe=Pipeline([
    (
        "split_real_cycle",
        pp.SplitRealCycle()
    ),

    (
        "remove_idle",
        pp.RemoveIdleTime()

    ),
    (
        "resample_time",
        pp.ResampleTime(time_period=pdc.resample_time_period)
    ),
    (
        "remain_time",
        pp.AddingRemainTime()

    ),
    (
        "split_data",
        pp.SplitData(train_cycles=pdc.train_cycles,
                     val_cycles=pdc.val_cycles,
                     test_cycles=pdc.test_cycles,
                     target_name=pdc.target_name,
                     save_data=pdc.save_data,
                     save_path=os.path.join(core.PACKAGE_PATH,pdc.save_path))
    )
],verbose=1)



train_pipeline=Pipeline([    
    (
        "roof_process",
        ft.RoofProcess(feature_col=ftc.roof_feature,threshold_temp=ftc.roof_threshold_temp,feature_set=ftc.roof_feature_set)
    ),
    (
        "gas_process",
        ft.GasProcess(feature_col=ftc.gas_feature,feature_set=ftc.gas_feature_set)
    ),
    (
        "select_data",
        ft.SelectData(features=ftc.features)
    ),
    (
        "ml_model",
        LGBMRegressor()
    )
],verbose=1)


predata_for_train_pipeline=Pipeline([    
    (
        "roof_process",
        ft.RoofProcess(feature_col=ftc.roof_feature,threshold_temp=ftc.roof_threshold_temp,feature_set=ftc.roof_feature_set)
    ),
    (
        "gas_process",
        ft.GasProcess(feature_col=ftc.gas_feature,feature_set=ftc.gas_feature_set)
    ),
    (
        "select_data",
        ft.SelectData(features=ftc.features)
    )
],verbose=1)
#print(data_prepare_pipe)



