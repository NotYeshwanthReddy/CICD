import logging
from tkinter import EXCEPTION
from utils.config import config
import pandas as pd
import logging

class FileHandler:
    def __init__(self):
        logging.info("Initializing File Handler")
        self.input_file = config['input_file']
        self.output_file = config['output_file']
    
    def read_data(self):
        logging.info("Reading file")
        try:
            if self.input_file.split(".")[-1] == "csv":
                df = pd.read_csv(self.input_file)
            elif self.input_file.split(".")[-1] == "xlsx":
                df = pd.read_excel(self.input_file)
            return df
        except Exception as e:
            logging.error("Read error")
            logging.error(e)
            print(e)
            return False

    def write_data(self, predictions):
        logging.info("Writing file")
        try:
            with open(self.output_file, "w") as outfile:
                outfile.write("\n".join(predictions))
            return True
        except Exception as e:
            logging.error("Writing error")
            logging.error(e)
            print(e)
            return False
