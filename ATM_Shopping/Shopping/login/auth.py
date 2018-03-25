import pickle
import os
from Shopping.login import login
from Shopping.core import Admin


def auth(status, id_path):
    if not status:
        id, passwd_input = login.login()
        if id == 'Admin' and passwd_input == '123456789':
            Admin.run()
        elif os.path.isfile(r'%s\Shopping\UserData\%s' %(id_path, id)):
            with open(r'%s\Shopping\UserData\%s' %(id_path, id), 'rb') as file:
                passwd = pickle.loads(file.read())['Passwd']
            if passwd_input == passwd:
                status = True
            else:
                print('ID或密码错误!')
            return status
        else:
            print('ID或密码错误!')
    else:
        return True
