import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Logger
logger_path = BASE_DIR + '\\Shopping\\logger'
logger_level = logging.INFO


# UserData
user_data_path = BASE_DIR + '\\Shopping\\UserData'

# Shopping
shopping_list_path =BASE_DIR + '\\Shopping\\core\\shopping_list_config'


if __name__ == '__main__':
    print(logger_path)
