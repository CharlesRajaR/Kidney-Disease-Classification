from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == "__main__":
    
    STAGE_NAME = "PREPARE BASE MODEL STAGE"

    try:
       logger.info(f"\n\n\n<======== {STAGE_NAME} started ==========>\n\n\n")
       pipe = PrepareBaseModelPipeline()
       pipe.main()
       logger.info(f"\n\n\n<========== {STAGE_NAME} is completed ============>\n\n\n")
    except Exception as e:
       logger.info(e)
       raise e
       