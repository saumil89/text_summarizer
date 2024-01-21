from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_dir
from textSummarizer.entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_dir([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_dir([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir)
        
        return data_ingestion_config
    
    def downloaded_data_validation_config(self) -> DataValidationConfig:
            config = self.config.data_validation

            create_dir([config.root_dir])

            data_validation_config = DataValidationConfig(
                root_dir = config.root_dir,
                file_status = config.file_status,
                all_files_required = config.all_files_required
            )
            
            return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_dir([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            tokenizer_name = config.tokenizer_name,
            max_input_length = config.max_input_length,
            max_output_length = config.max_output_length
        )
        
        return data_transformation_config