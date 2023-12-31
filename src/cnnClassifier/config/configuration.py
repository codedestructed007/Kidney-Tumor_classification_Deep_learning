import os
from src.cnnClassifier.constants import *
from src.cnnClassifier.utils.common import read_yaml,create_directories
from src.cnnClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig,ModelTrainingConfig, ModelEvaluationConfig



class ConfigurationManager:
    def __init__(self,
                 config_filapath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filapath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        create_directories([self.config.artifacts_root])
        
        
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL= config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config
    
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])
        
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir= Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate= self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )
        return prepare_base_model_config
    
    def get_ṭraining_model_config(self) -> ModelTrainingConfig:
        config = self.config.training
        params = self.params
        prepare_base_model = self.config.prepare_base_model
        create_directories([config.root_dir])
        self.training_data = os.path.join(self.config.data_ingestion.unzip_dir,'kidney_tumor_classificaiton_dataset')
        
        training_model_config = ModelTrainingConfig(
            root_dir=Path(config.root_dir),
            trained_model_path=Path(config.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(self.training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )
        
        return training_model_config
    
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        evaluation_config = ModelEvaluationConfig(
            path_to_model= "artifacts/training/model.h5",
            training_data="artifacts/data_ingestion/kidney_tumor_classificaiton_dataset",
            all_params=self.params,
            mlflow_uri="https://dagshub.com/codedestructed007/Kidney-Tumor_classification_Deep_learning.mlflow",
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
            
        )
        return evaluation_config