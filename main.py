from tumorClassifier import logger
from tumorClassifier.pipeline.stage_01_dataingestion import DataIngestionTrainingPipeline
from tumorClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseTrainingPipeline
from tumorClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    ingest_data = DataIngestionTrainingPipeline()
    ingest_data.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base = PrepareBaseTrainingPipeline()
    prepare_base.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_train = ModelTrainingPipeline()
    model_train.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e