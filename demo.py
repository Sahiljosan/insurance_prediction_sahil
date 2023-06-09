# we have created this file for :
# batch_prediction
# training_pipeline

from Insurance_sahil.pipeline.Batch_Prediction import start_batch_prediction
from Insurance_sahil.pipeline.Training_pipeline import start_training_pipeline

# file_path = r"G:\Udemy\DATA SCIENCE ineuron\VS Code\ML_Project_insurance_prediction_sahil\data\insurance.csv"

if __name__ == "__main__":
    try:
        # output_file = start_batch_prediction(input_file_path= file_path)
        output = start_training_pipeline()
        print(output)

    except Exception as e:
        print(e)