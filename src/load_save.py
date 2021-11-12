from src.utils.logger.appLogger import appLogger as appLogger 
from src.utils.all_utils import read_yaml
import argparse
import pandas as pd
import os



def get_data(config_path):
    
    """
    This function is used to read the data from the config file.
    """

    try:
        config = read_yaml(config_path)
        # print(config)
        
        remote_data_path = config['data_source']
        df = pd.read_csv(remote_data_path)
        # print(df.head())

        # save dataset in the local directory
        # create path to directory

        artifacts_dir = config['artifacts']['artifacts_dir']
        local_data_path = config['artifacts']['input_data_dir']
        data_file = config['artifacts']['data_file']

        raw_local_dir_path = os.path.join(artifacts_dir, local_data_path)
        raw_local_file_path = os.path.join(raw_local_dir_path, data_file)

        df.to_csv(raw_local_file_path, sep=',', index=False)



        
    except Exception as e:
        appLogger.error(e)





if __name__ == '__main__':

    args = argparse.ArgumentParser()

    args.add_argument("--config","-c", default ="config/config.yaml")
    
    parsed_args = args.parse_args()

    get_data(config_path = parsed_args.config)
    