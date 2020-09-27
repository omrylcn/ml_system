import os 
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


# column index
rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    
    """
    Definition
    -----------
    This is class for make new features like "rooms_per_houselhold" and "population_per_household"
    
    Parameters
    ----------
    add_bedrooms_per_room : it is a boolen value. Decision is to make "bedrooms_per_room" feature. 


    Returns
    -------
    numpy array with new feature columns
    
    """
    
    def __init__(self, add_bedrooms_per_room = True):
        
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

