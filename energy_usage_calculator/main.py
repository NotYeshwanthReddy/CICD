import logging
from pstats import Stats
from utils.config import config, log_config
from logging import config as log_conf
log_conf.dictConfig(log_config)

from utils.filehandler import FileHandler
from model.preprocessing import Preprocessing
from model.regressior import RegressionModel
from model.postprocessing import Postprocessing
from utils.evaluate import evaluate


logging.basicConfig(filename=config["log_file"], filemode='W', level=logging.DEBUG)

def check_status(status):
    if type(status)==bool:
        if status == False:
            exit()
    else:
        pass

def main():
    fh = FileHandler()
    df = fh.read_data()

    check_status(df)

    preprocess = Preprocessing()
    df = preprocess.run(df)

    check_status(df)

    reg = RegressionModel()
    model = reg.train(df)
    check_status(model)

    predictions = reg.predict(model=model, df=df)
    check_status(predictions)
    
    reg.save_model()
    model = reg.load_model()
    check_status(model)

    postprocess = Postprocessing()
    predictions = postprocess.run(predictions)
    check_status(predictions)

    results = df[config['TARGET']]
    evaluate(predictions, results)
    return True

if __name__=="__main__":
    main()
