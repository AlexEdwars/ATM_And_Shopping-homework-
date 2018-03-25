import logging
import time
from ATM.Config import Config
from ATM.core import atm_main


logger = logging.getLogger()
logger.setLevel(Config.logger_level)


sh = logging.StreamHandler()
fh_day = logging.FileHandler(Config.logger_path + '\\' + time.strftime('%Y-%m-%d', time.localtime()) + '.txt')
fh_mon = logging.FileHandler(Config.logger_path + '\\' + time.strftime('%Y-%m', time.localtime()) + '.txt')


sh.setLevel(Config.logger_level)
fh_day.setLevel(Config.logger_level)
fh_mon.setLevel(Config.logger_level)


logger.addHandler(sh)
logger.addHandler(fh_day)
logger.addHandler(fh_mon)


def log(log_type, money, user = None):
    if log_type == 'transfer':
        logger.info(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ':' + atm_main.user_status['cardid'] + ' ' + 'transfer' + ' ' + str(money) + ' ' + 'to' + user)
    else:
        logger.info(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ':' + atm_main.user_status['cardid'] + ' ' + log_type + ' ' + str(money))
