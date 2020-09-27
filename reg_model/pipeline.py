from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from lightgbm import LGBMRegressor


from reg_model.preprocessing.preprocessors import CombinedAttributesAdder
from reg_model.config import config

import logging
_logger = logging.getLogger(__name__)


from reg_model import pipeline

ftc=config.create_feature_config()

# numerical attributes
num_pipeline = Pipeline(
    [
        (
            'imputer',
            SimpleImputer(strategy=ftc.imputer_strategy)
        ),
        (
            'attribs_adder',
            CombinedAttributesAdder()
        ),
        (
            'std_scaler', StandardScaler()
        ),
    ])


# numerical and categorical attributes
processing_pipeline = ColumnTransformer(
    [
        (
            "num", num_pipeline,
            ftc.num_attribs),
        (
            "cat",
            OneHotEncoder()
            , ftc.cat_attribs),
    ])


# full pipeline processing and ml-model
full_pipeline = Pipeline(
    [
        (
            "preprocessing",
            processing_pipeline,
            ),
        (
            "model",
            LGBMRegressor()
        )
    ],verbose=1)
