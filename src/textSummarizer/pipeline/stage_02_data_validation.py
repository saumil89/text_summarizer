from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger

class DataValidationPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation = DataValidation(config.downloaded_data_validation_config())
        data_validation.validate_all_files_exist()


