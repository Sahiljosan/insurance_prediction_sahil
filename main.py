from Insurance_sahil.logger import logging
from Insurance_sahil.exception import InsuranceException
import os,sys

from Insurance_sahil.utils import get_collection_as_dataframe
from Insurance_sahil.entity.config_entity import TrainingPipelineConfig
from Insurance_sahil.entity import config_entity
from Insurance_sahil.components.data_ingestion import DataIngestion
from Insurance_sahil.components.data_valdiation import DataValidation


# def test_logger_and_exception():
#     try:
#         logging.info("Starting the test logger and exception")
#         result = 3/0
#         print(result)

#         logging.info("Ending point of the logger and exception class")

#     except Exception as e:
#         logging.debug(str(e))
#         raise InsuranceException(e,sys)
    
# if __name__ == "__main__":
#     try:
#         test_logger_and_exception()
#     except Exception as e:
#         print(e)


if __name__ == "__main__":
    try:
        #get_collection_as_dataframe(database_name= "INSURANCE", collection_name = "INSURANCE_PROJECT")

        training_pipeline_config = config_entity.TrainingPipelineConfig()

        # data_ingestion
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config= training_pipeline_config)
        print(data_ingestion_config.to_dict())

        data_ingestion = DataIngestion(data_ingestion_config= data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()


        # data_validation
        data_validation_config = config_entity.DataValidatonConfig(training_pipeline_config= training_pipeline_config)
        data_validation = DataValidation(data_validation_config= data_validation_config,
                                         data_ingestion_artifact = data_ingestion_artifact)
        
        data_validation_artifact = data_validation.initiate_data_valiation()

    except Exception as e:
        print(e) 
        