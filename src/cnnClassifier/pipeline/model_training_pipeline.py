import sys
sys.path.append(r'c:\\Users\\Dell\\OneDrive\\Desktop\\Real_projects\\Kidney-Tumor_classification_Deep_learning')

from src.cnnClassifier import logger
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_training import Training


Stage_training = 'Training'

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            training_model_config =config.get_ṭraining_model_config()
            training = Training(training_model_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
            
        except Exception as e:
            raise e
            
            
