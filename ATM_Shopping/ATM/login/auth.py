import pickle
import os
from ATM.login import login
from ATM.core import Admin
from ATM.core import atm_main


def auth(status, id_path):
    if not status:
        id, passwd_input = login.login()
        if id == 'Admin' and passwd_input == '123456789':
            Admin.run()
        elif os.path.isfile('%s\\ATM\\UserData\%s' %(id_path, id)):
            with open('%s\\ATM\\UserData\%s' %(id_path, id), 'rb') as file:
                userdata = pickle.loads(file.read())
            passwd = userdata['passwd']
            atm_main.user_status['cardid'] = userdata['cardid']
            atm_main.user_status['username'] = userdata['username']
            if passwd_input == passwd:
                if userdata['status'] == 'frozen':
                    print('账户被冻结')
                else:
                    status = True
            else:
                print('ID或密码错误!')
            return status
        else:
            print('ID或密码错误!')
    else:
        return True
