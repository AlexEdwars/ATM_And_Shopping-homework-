import os
import logging


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# UserData
userdata_path = BASE_DIR + '\\ATM\\UserData'


# operation
draw = {'interest': 0.05}
deposit = {'interest': 0}
pay = {'interest': 0}
transfer = {'interest': 0.05}


# Card
limit = 20000


# logger
logger_path = BASE_DIR + '\\ATM\\logger'
logger_level = logging.INFO
