import logging
import pickle
from tkinter import EXCEPTION
from utils.config import config
from catboost import CatBoostRegressor

class RegressionModel:
    def __init__(self):
        logging.info("Initializing Model Variables")
        self.ID = config['ID']
        self.TARGET = config['TARGET']
        self.SEED = config["SEED"] 
        self.MODEL_MAX_DEPTH = config["MODEL_MAX_DEPTH"]
        self.MODEL_TASK_TYPE = config["MODEL_TASK_TYPE"]
        self.MODEL_RL = config["MODEL_RL"]
        self.MODEL_EVAL_METRIC = config["MODEL_EVAL_METRIC"]
        self.MODEL_LOSS_FUNCTION = config["MODEL_LOSS_FUNCTION"]
        self.MODEL_ESR = config["MODEL_ESR"]
        self.MODEL_VERBOSE = config["MODEL_VERBOSE"]
        self.MODEL_ITERATIONS = config["MODEL_ITERATIONS"]

        self.model = None

        
    def train(self, df):
        X = df.drop([self.ID, self.TARGET],axis =1)
        y = df[self.TARGET]
        logging.info("Initializing model")

        self.model  = CatBoostRegressor(
            verbose = self.MODEL_VERBOSE,
            early_stopping_rounds = self.MODEL_ESR,
            random_seed = self.SEED,
            max_depth = self.MODEL_MAX_DEPTH,
            task_type = self.MODEL_TASK_TYPE,
            learning_rate = self.MODEL_RL,
            iterations = self.MODEL_ITERATIONS,
            loss_function = self.MODEL_LOSS_FUNCTION,
            eval_metric = self.MODEL_EVAL_METRIC
        )
        logging.info("Training model")
        self.model.fit(X, y)
        return self.model
    
    def predict(self, df, model=None):
        logging.info("Predicting results")
        try:
            X = df.drop([self.ID, self.TARGET],axis =1)
            y = df[self.TARGET]
            if model==None:
                predictions = self.model.predict(X)
            elif model!=None:
                predictions = model.predict(X)
            return predictions
        except EXCEPTION as e:
            return False

    def save_model(self, model=None):
        logging.info("Saving Model")
        try:
            if model==None:
                pickle.dump(self.model, open(config['model_location'], 'wb'))
            elif model!=None:
                pickle.dump(model, open(config['model_location'], 'wb'))
            return True
        except Exception as e:
            logging.error("Coudn't save model")
            logging.error(e)
            return False        

    def load_model(self):
        logging.info("Loading model")
        try:
            loaded_model = pickle.load(open(config['model_location'], 'rb'))
            return loaded_model
        except EXCEPTION as e:
            logging.error("Coudn't load Model")
            logging.error(e)
            return False
