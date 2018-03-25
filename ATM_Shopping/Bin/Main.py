import os
import sys


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)


from Shopping.core import shopping_main
from ATM.core import atm_main


order_list = {
    '1': atm_main.run,
    '2': shopping_main.run
}


print('帮助列表'.center(20, '-'))
print('''
1: ATM
2: Shopping
''')
print('帮助列表'.center(20, '-'))
user_input = input('>>>:').strip()
if user_input == '1':
    order_list[user_input](atm_main.user_status['status'], base_dir)
elif user_input == '2':
    order_list[user_input](shopping_main.user_status_shopping['status'], base_dir)
else:
    print('无此项!')
