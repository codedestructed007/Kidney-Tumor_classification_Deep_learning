import sys
sys.path.append(r'c:\\Users\\Dell\\OneDrive\\Desktop\\Real_projects\\Kidney-Tumor_classification_Deep_learning')

from src.cnnClassifier import logger
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.base_model_preparation import PrepareBaseModel

STAGE_MODEL_PREPARATION = 'Base model preparation Stage'

class BaseModelPreparationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            prepare_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise e
        

