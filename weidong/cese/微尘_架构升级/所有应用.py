from login_all.pack.user_all import *
from login_all.login import *

'''选择登录系统'''
t = xingneng()
'''选择登录账号'''
user = t.vchen_me_test
s = Login(system=t, user=user, rukou=1, dingzhi_y_n=2).on()