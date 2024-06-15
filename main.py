from tumorClassifier import logger
from tumorClassifier.pipeline.stage_01_dataingestion import DataIngestionTrainingPipeline, STAGE_NAME
from tumorClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseTrainingPipeline, STAGE_NAME

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e