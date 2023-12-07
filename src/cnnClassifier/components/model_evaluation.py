

import os
from urllib.parse import urlparse
import mlflow
import mlflow.keras as mlkeras
import tensorflow as tf
from pathlib import Path
from src.cnnClassifier.entity.config_entity import ModelEvaluationConfig
from src.cnnClassifier.utils.common import save_json

class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config
        
    
    def _valid_generator(self):
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.3
        )
    
        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = 'bilinear'
        )
        
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
            
        )
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = 'validation',
            shuffle = False,
            **dataflow_kwargs
        )
        
    @staticmethod
    def load_model(path: Path):
        return tf.keras.models.load_model(path)
    
    
    def evaluation(self):
        self.model = self.load_model(self.config.path_to_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()
    
    def save_score(self):
        score = {'loss' : self.score[0], 'accuracy' : self.score[1]}
        save_json(Path('scores.json'), data= score)
        
    
    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {'loss' : self.score[0], 'accuracy' : self.score[1]}
            )
        
            if tracking_url_type_store != 'file':
                mlkeras.log_model(self.model, 'model',registered_model_name='VGG16Model')
            else:
                mlkeras.log_model(self.model, 'model')