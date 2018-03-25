from ATM.login import auth
from ATM.core import order_list


user_status = {
'status': False,
'cardid': None,
'username': None
}


def run(status, id_path):
    times = 0
    while times < 3 and status is False:
        user_status = auth.auth(status, id_path)
        if user_status:
            order_list.show_order()
            break
        else:
            times += 1
    else:
        print('账号已被锁定!')
        exit()
    while True:
        user_input = input('>>>:').strip()
        if user_input in order_list.order_list:
            order_list.order_list[user_input]()
        elif user_input == 'e':
            exit()
        else:
            print('无此项!')
