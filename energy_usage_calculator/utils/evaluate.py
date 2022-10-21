from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import math
import logging


def evaluate(predictions, results):
    logging.info("Evaluating Model Performance")
    try:
        print("mean_absolute_error : {}".format(mean_absolute_error(results, predictions)))
        print("mean_squared_error: {}".format(mean_squared_error(results, predictions)))
        print("mean_error : {}".format(math.sqrt(mean_squared_error(results, predictions))))

        logging.info("mean_absolute_error : {}".format(mean_absolute_error(results, predictions)))
        logging.info("mean_squared_error: {}".format(mean_squared_error(results, predictions)))
        logging.info("mean_error : {}".format(math.sqrt(mean_squared_error(results, predictions))))
    except Exception as e:
        logging.error("Evaluation Failed")
        logging.error(e)
