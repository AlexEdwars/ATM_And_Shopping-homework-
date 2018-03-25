import pickle
import os
from ATM.Config import Config


user_data = {
    'cardid': None,
    'passwd': None,
    'username': None,
    'sex': None,
    'age': None,
    'pay_day': 22,
    'balance': 0,
    'limit': None,
    'status': 'normal'
}


def file_read(id):
    with open(Config.userdata_path + '\\' + id, 'rb') as file:
        userdata = pickle.loads(file.read())
    return userdata


def file_write(id, concent):
    with open(Config.userdata_path + '\\' + id, 'wb') as file:
        pickle.dump(concent, file)


def add():
    global user_data
    cardid = input('请输入用户ID:').strip()
    if len(cardid) != 10:
        print('请输入一个十位数!')
    else:
        user_data['cardid'] = cardid
        user_data['passwd'] = input('请输入用户密码:').strip()
        user_data['username'] = input('请输入用户名称:').strip()
        sex = input('请输入用户性别(Male/Female):').strip()
        if sex != 'Male' and sex != 'Female':
            print('请输入Male/Female')
        else:
            user_data['sex'] = sex
            age = input('请输入用户年龄:').strip()
            if not age.isdigit():
                print('请输入一个正确的数字')
            else:
                user_data['age'] = age
                limit = input('请输入用户额度:').strip()
                if not limit.isdigit():
                    print('请输入一个正确的数字')
                else:
                    user_data['limit'] = int(limit)
                    file_write(user_data['cardid'], user_data)


def change():
    order_list_change = {
        '1': name_change,
        '2': passwd_change,
        '3': sex_change,
        '4': age_change,
        '5': limit_change,
        '6': status_change
    }
    cardid = input('请输入要操作的账户ID:').strip()
    if not cardid.isdigit():
        print('请输入一个正确的数字')
    elif not os.path.isfile(Config.userdata_path + '\\' + cardid):
        print('ID错误')
    else:
        print('帮助列表'.center(20, '-'))
        print('''
        1: 修改用户名称
        2: 修改用户密码
        3: 修改用户性别
        4: 修改用户年龄
        5: 修改用户额度
        6: 修改用户状态
        ''')
        print('帮助列表'.center(20, '-'))
        while True:
            user_input = input('>>>:').strip()
            if user_input in order_list_change:
                order_list_change[user_input](cardid)
            elif user_input == 'e':
                break
            else:
                print('无此项!')


def name_change(cardid):
    name_new = input('请输入新名称:').strip()
    userdata = file_read(cardid)
    userdata['username'] = name_new
    file_write(cardid, userdata)
    print('修改成功')


def passwd_change(cardid):
    passwd_new = input('请输入新密码:').strip()
    userdata = file_read(cardid)
    userdata['passwd'] = passwd_new
    file_write(cardid, userdata)


def sex_change(cardid):
    sex_new = input('请输入新性别:').strip()
    if sex_new != 'Male' and sex_new != 'Female':
        print('请输入一个正确的值')
    else:
        userdata = file_read(cardid)
        userdata['sex'] = sex_new
        file_write(cardid, userdata)
        print('修改成功')


def age_change(cardid):
    age_new = input('请输入新年龄:').strip()
    if not age_new.isdigit():
        print('请输入一个正确的数字')
    else:
        userdata = file_read(cardid)
        userdata['age'] = age_new
        file_write(cardid, userdata)
        print('修改成功')


def limit_change(cardid):
    limit_new = input('请输入新额度:').strip()
    if not limit_new.isdigit():
        print('请输入一个正确的数字')
    else:
        userdata = file_read(cardid)
        userdata['limit'] = int(limit_new)
        file_write(cardid, userdata)
        print('修改成功')


def status_change(cardid):
    status_new = input('请输入新状态(frozen/normal):').strip()
    if status_new != 'frozen' and status_new != 'normal':
        print('请输入一个正确的值')
    else:
        userdata = file_read(cardid)
        userdata['status'] = status_new
        file_write(cardid, userdata)
        print('修改成功')


def sub():
    cardid = input('请输入要删除的用户的id:').strip()
    if not cardid.isdigit():
        print('请输入一个正确的数字')
    elif not os.path.isfile(Config.userdata_path + '\\' + cardid):
        print('ID错误')
    else:
        os.remove(Config.userdata_path + '\\' + cardid)
