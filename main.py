from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

stage = 'Data Ingestion stage'
try:
    logger.info(f'>>>>>>> Starting {stage} <<<<<<<<')
    DataIngestionTrainingPipeline().main()
    logger.info(f'>>>>>>> Finished {stage} <<<<<<<<')
except Exception as e:
    logger.error(f'Error in {stage}: {e}')
    raise e
