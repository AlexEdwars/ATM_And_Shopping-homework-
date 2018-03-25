from Shopping.core import shopping_list
from Shopping.login import auth
from Shopping.core import logger
from ATM.core import pay_port


user_status_shopping = {
'status': False,
'userid': None,
'username': None
}
money = 0


def run(status, id_path):
    global money
    times = 0
    while times < 3 and status is False:
        user_status = auth.auth(status, id_path)
        if user_status:
            shopping_list.shopping()
            break
        else:
            times += 1
    else:
        print('账号已被锁定!')
        exit()
    while True:
        commodity_number = input('请输入您要购买的物品:').strip()
        if commodity_number in shopping_list.shopping_list:
            shopping_list.shopping_car.append(commodity_number)
            money += shopping_list.shopping_list[commodity_number]
            logger.log('buy', 'commodity', commodity_number)
            print(commodity_number,'已加入您的购物车!')
            shopping_list.show_shopping_car()
        elif commodity_number == '购物车':
            shopping_list.show_shopping_car()
        elif commodity_number == 'e':
            exit()
        elif commodity_number == '结账':
            pay_port.pay()
        else:
            print('无该项!')
