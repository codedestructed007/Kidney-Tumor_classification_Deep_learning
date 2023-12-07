import sys
sys.path.append(r'c:\\Users\\Dell\\OneDrive\\Desktop\\Real_projects\\Kidney-Tumor_classification_Deep_learning')

from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_evaluation import ModelEvaluation

Stage_evaluation = 'Model Evaluation'


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            evaluation_config = config.get_model_evaluation_config()
            evaluation = ModelEvaluation(evaluation_config)
            evaluation.evaluation()
            evaluation.log_into_mlflow()
            
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    pipeline = ModelEvaluationPipeline()
    pipeline.main()
            