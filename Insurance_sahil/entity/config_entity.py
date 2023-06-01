import os,sys
from Insurance_sahil.logger import logging
from Insurance_sahil.exception import InsuranceException
from datetime import datetime


FILE_NAME = "insurance.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
TRANSFORMER_OBJECT_FILE_NAME = "transformer.pkl"
TARGET_ENCODER_OBJECT_FILE_NAME = "target_encoder.pkl"
MODEL_FILE_NAME = "model.pkl"

class TrainingPipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception as e:
            raise InsuranceException(e,sys)
        

class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        try:
            self.database_name = "INSURANCE"
            self.collection_name = "INSURANCE_PROJECT"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion") # we are creating one folder of name "data_ingestion" in artifact directory
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store", FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2

        except Exception as e:
            raise InsuranceException(e,sys)

# Convert data into dict:
    def to_dict(self)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise InsuranceException(e,sys)
        

class DataValidatonConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir,"data_validation")
            self.report_file_path = os.path.join(self.data_validation_dir,"report.yaml") # report can be created in any format yaml, json, csv
            self.missing_threshold:float = 0.2
            self.base_file_path = os.path.join("G:\\Udemy\\DATA SCIENCE ineuron\\VS Code\\ML_Project_insurance_prediction_sahil\\data\\insurance.csv")

        except Exception as e:
            raise InsuranceException(e,sys)
        
