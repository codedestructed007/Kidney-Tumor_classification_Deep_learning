from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.data_ingestion_pipeline import STAGE_NAME, DataIngestionTrainingPipeline

try:
    logger.info(f" >> Stage - {STAGE_NAME} started >>")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">> Stage - {STAGE_NAME} completed successfully>>")        
except Exception as e:
    raise e