from Insurance_sahil.logger import logging
from Insurance_sahil.exception import InsuranceException
import os,sys

from Insurance_sahil.utils import get_collection_as_dataframe

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
        get_collection_as_dataframe(database_name= "INSURANCE", collection_name = "INSURANCE_PROJECT")

    except Exception as e:
        print(e)
        