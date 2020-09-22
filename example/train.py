import warnings
warnings.filterwarnings("ignore")

import sys
import os
import tarfile
import urllib

import numpy as np
import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer

from lightgbm import LGBMRegressor

from config import core



# Load and split data

train=pd.read_csv("datasets/train_data.csv")
test=pd.read_csv("datasets/test_data.csv")


X_tr=train.drop("median_house_value",axis=1)
y_tr=train["median_house_value"].copy()

X_ts=test.drop("median_house_value",axis=1)
y_ts=test["median_house_value"].copy()


# Preprocessing

# imputer data 
imputer = SimpleImputer(strategy="median")

# onehot encoder 
cat_encoder = OneHotEncoder()

# New feature
rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6
class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self  # nothing else to do
    def transform(self, X):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,
                         bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]



# Pipeline part

num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()),
    ])


num_attribs = list(X_tr.drop("ocean_proximity",axis=1))
cat_attribs = ["ocean_proximity"]

full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
    ])

X_tr_prepared = full_pipeline.fit_transform(X_tr)

model=LGBMRegressor(max_depth=40,num_leaves=31))
model.fit(X_tr_prepared,y_tr)

print(model.score(X_tr_prepared,y_tr))