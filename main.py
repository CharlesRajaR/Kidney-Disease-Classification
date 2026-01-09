from cnnClassifier import logger
from cnnClassifier.pipeline.stage_1_data_ingestion_pipeline import DataIngestionPipeline


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
