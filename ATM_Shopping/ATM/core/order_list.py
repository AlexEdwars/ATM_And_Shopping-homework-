from ATM.core import orders


def show_order():
    print('帮助列表'.center(20, '-'))
    print('''
    1: 取款
    2: 存款
    3: 还款
    4: 转账
    5: 查看个人信息
    ''')
    print('帮助列表'.center(20, '-'))


order_list = {
    '1': orders.draw,
    '2': orders.deposit,
    '3': orders.pay,
    '4': orders.transfer,
    '5': orders.show_info
}
