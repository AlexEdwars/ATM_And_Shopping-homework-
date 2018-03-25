from Shopping.core import shopping_list
from Shopping.core import user_manage


def run():
    global order_list
    while True:
        print('指令列表'.center(20, '-'))
        print('''
        1: 增加商品
        2: 删除商品
        3: 修改商品
        4: 增加用户
        5: 删除用户
        6: 修改用户
        7: 退出
        ''')
        print('指令列表'.center(20, '-'))
        user_input = input('>>>:').strip()
        if user_input in order_list:
            order_list[user_input]()
        elif user_input == '7':
            exit()


order_list = {
'1': shopping_list.shopping_list_add,
'2': shopping_list.shopping_list_del,
'3': shopping_list.shopping_list_change,
'4': user_manage.user_add,
'5': user_manage.user_del,
'6': user_manage.user_change
}
