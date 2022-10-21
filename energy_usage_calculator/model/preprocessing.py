from sklearn.preprocessing import LabelEncoder
from utils.config import config
import random
import logging
import os
import numpy as np

class Preprocessing:
    def __init__(self):
        logging.info("Initialized pre-processing")
        random.seed(config['SEED'])
        os.environ['PYTHONHASHSEED'] = str(config['SEED'])
        np.random.seed(config['SEED'])

    def run(self, df):
        str_list = [] 
        num_list = []
        logging.info("Pre-processing Data")
        for colname, colvalue in df.iteritems():
            if type(colvalue[1]) == str:
                str_list.append(colname)
            else:
                num_list.append(colname)
                
        for col in str_list:
            encoder = LabelEncoder()
            encoder.fit(df[col])
            df[col] = encoder.transform(df[col])
        return df
