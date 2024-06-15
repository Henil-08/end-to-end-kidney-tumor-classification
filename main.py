from tumorClassifier import logger
from tumorClassifier.pipeline.stage_01_dataingestion import DataIngestionTrainingPipeline, STAGE_NAME

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e