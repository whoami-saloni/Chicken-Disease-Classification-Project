import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_02_Prepare_base_model import PrepareBaseModelTrainingPipeline

from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME= "Data Ingestion Stage"
STAGE_NAME1= "Preparing Base Model"

try:
    logger.info(f">>>>>>>stage {STAGE_NAME} started <<<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f">>>>>>>stage {STAGE_NAME1} started <<<<<<<<")
    obj=PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME1} completed<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

