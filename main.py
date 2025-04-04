import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_02_Prepare_base_model import PrepareBaseModelTrainingPipeline

from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_04_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_05_evaluation import EvaluationPipeline

STAGE_NAME= "Data Ingestion Stage"
STAGE_NAME1= "Preparing Base Model"
STAGE_NAME2="Model Training"
STAGE_NAME3="Model Evaluation"

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

try:
    logger.info(f">>>>>>>stage {STAGE_NAME2} started <<<<<<<<")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME2} completed<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f">>>>>>>stage {STAGE_NAME3} started <<<<<<<<")
    obj=EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME3} completed<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

