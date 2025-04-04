import os
import urllib.request as request
import zipfile
import sys
from cnnClassifier import logger
from cnnClassifier.utils.common import read_yaml,get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
                url= self.config.source_URL, 
                filename= self.config.local_data_file)
            logger.info(f"Downloaded {filename} with size {get_size(Path(self.config.local_data_file))}")
        else:
                logger.info(f"{self.config.local_data_file} already exists")

    def unzip_data(self):
        """
        zip_file_path: str
        Extracts the zip file into the specified directory
        function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)