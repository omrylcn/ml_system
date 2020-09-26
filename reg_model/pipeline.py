from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder


from reg_model.preprocessing.preprocessors import CombinedAttributesAdder
from reg_model.config import config

import logging
_logger = logging.getLogger(__name__)


from reg_model import pipeline

ftc=config.create_feature_config()

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


full_pipeline = ColumnTransformer(
    [
        (
            "num", num_pipeline,
            ftc.num_attribs),
        (
            "cat",
            OneHotEncoder()
            , ftc.cat_attribs),
    ])

