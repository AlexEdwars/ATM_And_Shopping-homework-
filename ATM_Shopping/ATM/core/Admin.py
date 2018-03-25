from ATM.core import user_manager


def run():
    order_list = {
        '1': user_manager.add,
        '2': user_manager.change,
        '3': user_manager.sub
    }
    print('帮助列表'.center(20, '-'))
    print('''
    1: 添加用户
    2: 修改用户
    3: 删除用户
    ''')
    print('帮助列表'.center(20, '-'))
    while True:
        user_input = input('>>>:').strip()
        if user_input in order_list:
            order_list[user_input]()
        elif user_input == 'e':
            exit()
        else:
            print('无此项')
