from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.training import Training
from cnnClassifier import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_training_config()
        model_training = Training(config=model_training_config)
        model_training.get_base_model()
        model_training.train_validation_generator()
        model_training.train()

STAGE_NAME = "MODEL TRAINING STAGE"

try:
    logger.info(f"\n\n\n<=========== {STAGE_NAME} started ============>\n\n\n")
    pipe = ModelTrainingPipeline()
    pipe.main()
    logger.info(f"\n\n\n<========== {STAGE_NAME} is completed ============>\n\n\n")
except Exception as e:
    logger.info(e)
    raise e
       