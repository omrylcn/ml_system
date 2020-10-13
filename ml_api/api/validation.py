from pydantic import BaseModel,ValidationError
import json
from typing import List


class InputData(BaseModel):
 
    # A sample schema for input unit data
    longitude:float
    latitude:float
    housing_median_age:float
    total_rooms:float
    total_bedrooms:float
    population:float
    households:float
    median_income:float
    ocean_proximity:str

class InputList(BaseModel):
    
    # input data schema     
    data: List[InputData]


def validate_inputs(input_data):
    
    # Check input data and remove errors
    
    # check errors
    errors=None
    try:
        InputList(data=input_data,many=True)

    except ValidationError as e:
        errors=e.errors()
        
    # delete error rows
    if errors:
        # find errors index
        indexes=[i["loc"][1] for i in errors]
        #print(indexes)

        for index in sorted(indexes,reverse=True):
            del input_data[index]
            
    return input_data,errors