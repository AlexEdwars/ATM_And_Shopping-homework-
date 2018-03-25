import logging
import time
from Shopping.Config import Config


logger_level = Config.logger_level
logger_path_day = Config.logger_path + '\\' + time.strftime('%Y-%m-%d', time.localtime())
logger_path_mon = Config.logger_path + '\\' + time.strftime('%Y-%m', time.localtime())


logger = logging.getLogger()
logger.setLevel(logger_level)


sh = logging.StreamHandler()
fh_day = logging.FileHandler(logger_path_day + '.txt')
fh_mon = logging.FileHandler(logger_path_mon + '.txt')


sh.setLevel(logger_level)
fh_day.setLevel(logger_level)
fh_mon.setLevel(logger_level)


logger.addHandler(sh)
logger.addHandler(fh_day)
logger.addHandler(fh_mon)


def log(log_type, item_type, item_name):
    logger.info('%s : You %s a %s is %s' %(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), log_type, item_type, item_name))
