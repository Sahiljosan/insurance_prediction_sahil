import pandas as pd
import numpy as np
import os
import sys
import yaml
import dill

from Insurance_sahil.logger import logging
from Insurance_sahil.exception import InsuranceException
from Insurance_sahil.config import mongo_client

def get_collection_as_dataframe(database_name:str, collection_name:str) -> pd.DataFrame:
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: "INSURANCE"
    collection_name: "INSURANCE_PROJECT"
    =========================================================
    return Pandas dataframe of a collection 
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(mongo_client[database_name][collection_name].find())
        logging.info(f"Find Columns:{df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping columns:_id")
            df = df.drop("_id", axis= 1)

        logging.info(f"Rows and columns in df: {df.shape}")
        return df
    
    except Exception as e:
        raise InsuranceException(e,sys)
    

