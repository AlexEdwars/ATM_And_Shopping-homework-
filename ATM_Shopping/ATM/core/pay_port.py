import pickle
from ATM.login import auth
from ATM.Config import Config
from ATM.core import atm_main
from Shopping.core import shopping_main
from ATM.core import orders
from ATM.core import logger


def pay():
    if auth.auth(False, Config.BASE_DIR):
        with open(Config.userdata_path + '\\' + atm_main.user_status['cardid'], 'rb') as file:
            userdata = pickle.loads(file.read())
        all_money = userdata['balance'] + userdata['limit']
        if userdata['balance'] < shopping_main.money:
            if all_money < shopping_main.money:
                print('余额不足')
            else:
                userdata['balance'] = 0
                userdata['limit'] = all_money - shopping_main.money
                print('支付成功')
                logger.log('pay', all_money)
                orders.file_write(userdata)
        else:
            userdata['balance'] -= shopping_main.money
            print('支付成功')
            logger.log('pay', all_money)
            orders.file_write(userdata)
