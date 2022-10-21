import logging
from utils.config import config, log_config
from logging import config as log_conf
log_conf.dictConfig(log_config)

from utils.filehandler import FileHandler
from model.preprocessing import Preprocessing
from model.regressior import RegressionModel
from model.postprocessing import Postprocessing
from utils.evaluate import evaluate


logging.basicConfig(filename=config["log_file"], filemode='W')
logging.basicConfig(level=logging.DEBUG)

logging.error('This is test error')

fh = FileHandler()
df = fh.read_data()

preprocess = Preprocessing()
df = preprocess.run(df)

reg = RegressionModel()
model = reg.train(df)
predictions = reg.predict(model=model, df=df)
reg.save_model()
model = reg.load_model()

postprocess = Postprocessing()
predictions = postprocess.run(predictions)

results = df[config['TARGET']]
evaluate(predictions, results)
