from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.data_ingestion_pipeline import STAGE_NAME, DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.prepare_model_pipeline import STAGE_MODEL_PREPARATION , BaseModelPreparationPipeline


try:
    logger.info(f" >> Stage - {STAGE_NAME} started >>")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">> Stage - {STAGE_NAME} completed successfully>>")        
except Exception as e:
    raise e


try:
    logger.info(f">> Stage - {STAGE_MODEL_PREPARATION} started >>")
    obj = BaseModelPreparationPipeline()
    obj.main()
    logger.info(f" >> Stage - {STAGE_MODEL_PREPARATION} completed successfully >>")
except Exception as e:
    raise e