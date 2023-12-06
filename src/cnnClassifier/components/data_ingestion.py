import os
import zipfile
import gdown
from src.cnnClassifier import logger
from src.cnnClassifier.utils.common import get_size

from src.cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config : DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        """
        fetch the data from url 
        """
        try:
            dataset_url = self.config.source_URL
            zip_downloaded_url = self.config.local_data_file
            os.makedirs(self.config.root_dir,exist_ok=True)
            logger.info(f'Downloading data from {dataset_url} into file {zip_downloaded_url}')
            
            prefix = 'https://drive.google.com/uc?/export=download&id='
            file_id = dataset_url.split('/')[-2]
            full_url =  prefix + file_id
            gdown.download(full_url, zip_downloaded_url)
            
            logger.info(f'Downloaded data from {dataset_url} into file {zip_downloaded_url}')
            
        except Exception as e:
            raise e
        
        
    def extract_zip_file(self):
        """
        zip_file_path : str
        Extracts the zip file into the data directory
            """
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path,exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                # It will dump the extracted file into unzip directory
                
        except Exception as e:
            raise e