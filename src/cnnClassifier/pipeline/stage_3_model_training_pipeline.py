from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.training import Training

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
       