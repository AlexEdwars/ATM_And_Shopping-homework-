import pickle
import os
from ATM.core import atm_main
from ATM.Config import Config
from ATM.core import logger


id_path = Config.BASE_DIR + '\\ATM\\UserData'


def file_read():
    with open(id_path + '\\' + atm_main.user_status['cardid'], 'rb') as file:
        userdata = pickle.loads(file.read())
    return userdata


def file_write(content):
    with open(id_path + '\\' + atm_main.user_status['cardid'], 'wb') as file:
        pickle.dump(content, file)


def draw():
    user_input =  input('请输入数额:').strip()
    if not user_input.isdigit():
        print('请输入一个正确的数字!')
    elif int(user_input) % 100 != 0:
        print('请输入一个整百的数字!')
    else:
        interest = int(user_input) * Config.draw['interest']
        all_money = int(user_input) + interest
        userdata = file_read()
        if userdata['balance'] < all_money:
            print('余额不足')
        else:
            userdata['balance'] -= all_money
            file_write(userdata)
            logger.log('draw', all_money)
            print('取款完成')
            print('手续费: %s' %(interest))


def deposit():
    user_input = input('请输入数额:').strip()
    if not user_input.isdigit():
        print('请输入一个正确的数字!')
    elif int(user_input) % 100 != 0:
        print('请输入一个整百的数字!')
    else:
        interest = int(user_input) * Config.deposit['interest']
        all_money = int(user_input) + interest
        userdata = file_read()
        userdata['balance'] += all_money
        file_write(userdata)
        logger.log('deposit', all_money)
        print('存款完成')
        print('手续费: %s' % (interest))


def pay():
    userdata = file_read()
    money = Config.limit - userdata['limit']
    interest = money * Config.pay['interest']
    all_money = money + interest
    if userdata['balance'] < all_money:
        print('余额不足')
    else:
        userdata['balance'] -= all_money
        file_write(userdata)
        logger.log('repay', all_money)
        print('还款成功')
        print('手续费: %s' %(interest))


def transfer():
    user_input = input('请输入目标账户:').strip()
    if not user_input.isdigit():
        print('请输入一个正确的数字!')
    elif len(user_input) != 10:
        print('请输入一个10位数')
    else:
        if os.path.isfile(id_path + '\\' + user_input):
            userdata_old = file_read()
            with open(id_path + '\\' + user_input, 'rb') as file:
                userdata_new = pickle.loads(file.read())
            money = input('请输入数额:').strip()
            if not money.isdigit():
                print('请输入一个正确的数字!')
            elif int(money) % 100 != 0:
                print('请输入一个整百的数字!')
            else:
                interest = int(money) * Config.transfer['interest']
                all_money = int(money) + interest
                if userdata_old['balance'] < all_money:
                    print('余额不足')
                else:
                    userdata_old['balance'] -= all_money
                    userdata_new['balance'] += int(money)
                    file_write(userdata_old)
                    with open(id_path + '\\' + user_input, 'wb') as file:
                        pickle.dump(userdata_new, file)
                    logger.log('transfer', all_money, userdata_new['cardid'])
                    print('转账成功')
                    print('手续费: %s' % (interest))
        else:
            print('ID错误!')


def show_info():
    userdata = file_read()
    for i in userdata:
        print(i, ':', userdata[i])
