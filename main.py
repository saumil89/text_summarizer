from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
'''
stage = 'Data Ingestion stage'
try:
    logger.info(f'>>>>>>> Starting {stage} <<<<<<<<')
    DataIngestionTrainingPipeline().main()
    logger.info(f'>>>>>>> Finished {stage} <<<<<<<<')
except Exception as e:
    logger.error(f'Error in {stage}: {e}')
    raise e
'''
stage = 'Data Validation stage'
try:
    logger.info(f'>>>>>>> Starting {stage} <<<<<<<<')
    DataValidationPipeline().main()
    logger.info(f'>>>>>>> Finished {stage} <<<<<<<<')
except Exception as e:
    logger.error(f'Error in {stage}: {e}')
    raise e

stage = 'Data Transformation stage'
try:
    logger.info(f'>>>>>>> Starting {stage} <<<<<<<<')
    DataTransformationPipeline().main()
    logger.info(f'>>>>>>> Finished {stage} <<<<<<<<')
except Exception as e:
    logger.error(f'Error in {stage}: {e}')
    raise e