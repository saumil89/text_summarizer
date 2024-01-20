import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size, create_dir
from textSummarizer.entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(
        self,
        config: DataIngestionConfig):
        self.config = config
    
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            file, headers = request.urlretrieve(
                url = self.config.source_url, 
                filename = self.config.local_data_file)
            logger.info(f'Downloaded {file} to {self.config.local_data_file} using {headers}')
            logger.info(f'Size of {self.config.local_data_file} is {get_size(Path(self.config.local_data_file))}')
        else:
            logger.info(f'{self.config.local_data_file} already exists of size {get_size(self.config.local_data_file)}')
    
    def unzip_data(self):
        unzip_path = Path(self.config.unzip_dir)
        if not os.path.exists(unzip_path):
            create_dir([unzip_path])
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f'Unzipped {self.config.local_data_file} to {unzip_path}')