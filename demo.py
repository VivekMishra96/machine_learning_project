from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger  import logging
from housing.config.configuration import Configuartion 
import os

def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        pipeline.start()
        logging.info("main function execution completed.")
        #pipeline.run_pipeline()
        #data_validation_config= Configuartion().get_data_transformation_config()
        #print(data_validation_config)
    except Exception as e:
        logging.error(f"{e}") 
        print(e)   


if __name__== "__main__":
    main()        