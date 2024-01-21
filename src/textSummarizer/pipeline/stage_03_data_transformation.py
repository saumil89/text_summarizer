from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransfomation
from textSummarizer.logging import logger

class DataTransformationPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation = DataTransfomation(config.get_data_transformation_config())
        data_transformation.convert()