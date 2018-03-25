import pickle
from Shopping.Config import Config


def shopping():
    print('购物列表'.center(20, '-'))
    for i in shopping_list:
        print(i,':',shopping_list[i])
    print('购物列表'.center(20, '-'))


def show_shopping_car():
    print('您的购物车:')
    for i in shopping_car:
        print(i)


def shopping_list_add():
    global shopping_list
    commodity = input('请输入要增加的商品名称:').strip()
    if commodity in shopping_list:
        print('已有此商品!')
        return None
    else:
        price = input('请输入要增加的商品的价格:').strip()
        if price.isdigit():
            price = int(price)
            shopping_list[commodity] = price
            with open(Config.shopping_list_path, 'wb') as f:
                pickle.dump(shopping_list, f)
        else:
            print('价格错误!')


def shopping_list_del():
    global shopping_list
    commodity = input('请输入要删除的商品名称:').strip()
    if commodity in shopping_list:
        shopping_list.pop(commodity)
        with open(Config.shopping_list_path, 'wb') as f:
            pickle.dump(shopping_list, f)
    else:
        print('无此项!')


def shopping_list_change():
    global shopping_change
    print('帮助列表'.center(20,'-'))
    print('''
    1: 修改商品名称
    2: 修改商品价格
    ''')
    print('帮助列表'.center(20, '-'))
    user_input = input('>>>:').strip()
    if user_input in shopping_change:
        shopping_change[user_input]()


def commodity_name_change():
    global shopping_list
    old_name = input('请输入要修改的商品名字:').strip()
    new_name = input('请输入修改后的名字:').strip()
    if old_name in shopping_list:
        content = shopping_list[old_name]
        shopping_list.pop(old_name)
        shopping_list[new_name] = content
        with open(Config.shopping_list_path, 'wb') as f:
            pickle.dump(shopping_list, f)
    else:
        print('无此项!')


def commodity_price_change():
    global shopping_list
    commodity_name = input('请输入要修改的商品名字:').strip()
    new_price = input('请输入修改后的价格:').strip()
    if commodity_name in shopping_list and new_price.isdigit():
        shopping_list[commodity_name] = int(new_price)
        with open(Config.shopping_list_path, 'wb') as f:
            pickle.dump(shopping_list, f)
    else:
        print('无此项!')

with open(Config.shopping_list_path, 'rb') as f:
    shopping_list = pickle.loads(f.read())
shopping_change = {
'1': commodity_name_change,
'2': commodity_price_change
}


shopping_car = []


if __name__ == '__main__':
    shopping()
