from cnnClassifier import logger
from cnnClassifier.pipeline.stage_1_data_ingestion_pipeline import DataIngestionPipeline
from cnnClassifier.pipeline.stage_2_prepare_base_model_pipeline import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_3_model_training_pipeline import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_4_model_evaluation_pipeline import EvaluationPipeline


# logger.info("hi")

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f"=======Stage {STAGE_NAME} started=======\n\n\n")
    pipe = DataIngestionPipeline()
    pipe.main()
    logger.info(f"======== STAGE : {STAGE_NAME} is completed=======\n\n\n")
except Exception as e:
    logger.info(e)
    raise(e)


STAGE_NAME = "PREPARE BASE MODEL STAGE"

try:
    logger.info(f"========Stage {STAGE_NAME} started ==========\n\n\n")
    pipe = PrepareBaseModelPipeline()
    pipe.main()
    logger.info(f"========== STAGE : {STAGE_NAME} is completed ============\n\n\n")
except Exception as e:
    logger.info(e)
    raise e


STAGE_NAME = "MODEL TRAINING STAGE"

try:
    logger.info(f"========Stage {STAGE_NAME} started ==========\n\n\n")
    pipe = ModelTrainingPipeline()
    pipe.main()
    logger.info(f"========== STAGE : {STAGE_NAME} is completed ============\n\n\n")
except Exception as e:
    logger.info(e)
    raise e

STAGE_NAME = "MODEL EVALUATION WITH MLFLOW"

try:
    logger.info(f"========Stage {STAGE_NAME} started ==========\n\n\n")
    pipe = EvaluationPipeline()
    pipe.main()
    logger.info(f"========== STAGE : {STAGE_NAME} is completed ============\n\n\n")
except Exception as e:
    logger.info(e)
    raise e