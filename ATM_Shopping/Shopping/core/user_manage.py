import pickle
import os
from Shopping.Config import Config


def user_add():
    global user_data
    user_id = input('请输入用户id:').strip()
    if user_id.isdigit():
        user_passwd = input('请输入用户密码:').strip()
        username = input('请输入用户名称:').strip()
        user_sex = input('请输入用户性别:(Male/Female)').strip()
        if user_sex != 'Male' and user_sex != 'Female':
            print('请输入一个正确的值!')
            return None
        user_age = input('请输入用户年龄:').strip()
        f = open(Config.user_data_path + '\\' + user_id, 'wb')
        user_data['UserID'] = user_id
        user_data['Username'] = username
        user_data['Passwd'] = user_passwd
        user_data['Sex'] = user_sex
        user_data['Age'] = user_age
        pickle.dump(user_data, f)
        f.close()
    else:
        print('ID必须是一个数字!')
        return None


def user_del():
    userid = input('请输入要删除的用户的ID:').strip()
    if os.path.isfile(Config.user_data_path + '\\' + userid):
        os.remove(Config.user_data_path + '\\' + userid)
    else:
        print('无此用户!')


def user_change():
    userid = input('请输入要修改的用户ID:').strip()
    if os.path.isfile(Config.user_data_path + '\\' + userid):
        with open(Config.user_data_path + '\\' + userid, 'rb') as file:
            userdata = pickle.loads(file.read())
        order_list_change = {
            '1': 'Username',
            '2': 'Passwd',
            '3': 'Age',
            '4': 'Sex'
        }
        print('帮助列表'.center(20, '-'))
        print('''
        1: 修改用户名
        2: 修改用户密码
        3: 修改用户年龄
        4: 修改用户性别
        ''')
        print('帮助列表'.center(20, '-'))
        user_input = input('>>>:').strip()
        if user_input in order_list_change:
            if user_input == '4':
                userdata[order_list_change[user_input]] = input('请输入修改后的内容:').strip()
                if userdata[order_list_change[user_input]] != 'Male' and userdata[order_list_change[user_input]] != 'Female':
                    print('请输入正确的信息!')
                    return None
            elif user_input == '3':
                userdata[order_list_change[user_input]] = input('请输入修改后的内容:').strip()
                if not userdata[order_list_change[user_input]].isdigit():
                    print('请输入数字!')
                    return None
            else:
                userdata[order_list_change[user_input]] = input('请输入修改后的内容:').strip()
            with open(Config.user_data_path + '\\' + userid, 'wb') as file:
                file.write(pickle.dumps(userdata))
        else:
            print('命令错误!')


user_data = {
'UserID': None,
'Username': None,
'Passwd': None,
'Sex': None,
'Age': None
}
