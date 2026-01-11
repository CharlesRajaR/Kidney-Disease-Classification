from cnnClassifier import logger
from cnnClassifier.pipeline.stage_1_data_ingestion_pipeline import DataIngestionPipeline
from cnnClassifier.pipeline.stage_2_prepare_base_model_pipeline import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_3_model_training_pipeline import ModelTrainingPipeline


# logger.info("hi")

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f"=======Stage {STAGE_NAME} started=======")
    pipe = DataIngestionPipeline()
    pipe.main()
    logger.info(f"======== STAGE : {STAGE_NAME} is completed=======")
except Exception as e:
    logger.info(e)
    raise(e)


STAGE_NAME = "PREPARE BASE MODEL STAGE"

try:
    logger.info(f"========Stage {STAGE_NAME} started ==========")
    pipe = PrepareBaseModelPipeline()
    pipe.main()
    logger.info(f"========== STAGE : {STAGE_NAME} is completed ============")
except Exception as e:
    logger.info(e)
    raise e


STAGE_NAME = "MODEL TRAINING STAGE"

try:
    logger.info(f"========Stage {STAGE_NAME} started ==========")
    pipe = ModelTrainingPipeline()
    pipe.main()
    logger.info(f"========== STAGE : {STAGE_NAME} is completed ============")
except Exception as e:
    logger.info(e)
    raise e

