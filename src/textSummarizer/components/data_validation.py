import os
from pathlib import Path
from textSummarizer.entity import DataValidationConfig
from textSummarizer.logging import logger

class DataValidation:
    def __init__(
        self,
        config: DataValidationConfig
    ):
    
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation = None
            all_files = os.listdir(Path('artifacts\data_ingestion\samsum_dataset'))

            for file in all_files:
                if file not in self.config.all_files_required:
                    validation = False
                    with open(self.config.file_status, 'a') as f:
                        f.write(f'File {file} not found in required files\n')
                    logger.error(f'File {file} not found in required files')
                else:
                    validation = True
                    with open(self.config.file_status, 'a') as f:
                        f.write(f'File {file} found in required files\n')
                    logger.info(f'File {file} found in required files')
            
            return validation
        except Exception as e:
            raise e
