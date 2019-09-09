from login_all.pack.user_all import *
from login_all.pack.sso import *
from login_all.pack.zhongou import *
from login_all.pack.微动跑团 import *
from login_all.pack.微尘客户管理系统 import *

class Login():
    def __init__(self,system=test(),user="",rukou="",dingzhi_y_n="no"):
        """
        :param system: 操作系统，分别是china()和test()/ceshi()，对应正式系统和研发系统，以及测试系统;;;;
        :param user: 在user_all中的user名称;;;;
        :param rukou: 指登录sso之后，进入哪个系统，1=vchen/2=plus/3=yunying，不进不写;;;;
        :param dingzhi_y_n: 是否是客户定制，如果是,写1，如果不是，随便写;;;;
        如果是中欧系统、微动跑团，则什么都不用写;;;;
        启动sso，用on;;;
        启动中欧,用zhongou_on;;;
        """
        '''选择登录系统'''
        self.t=system
        if dingzhi_y_n == 1:
            self.url = system.url_dingzhi
        else:
            self.url = system.url
        # print(self.url)
        '''选择登录账号'''
        self.user=user
        '''选择入口'''
        if rukou == 0:
            self.rukou=""
        if rukou == 2:
            self.rukou = "plus"
        elif rukou == 3:
            self.rukou = "yunying"
        elif rukou == 1:
            self.rukou = "vchen"
        else:
            self.rukou = rukou



    def on(self):
        """
        :return: 全局参外引
        """
        go = login_go().on(self.url, self.user["username"], self.user["password"], self.rukou)
        return go

    def zhongou_on(self,system="test"):
        """
        调用中欧启动页
        :param system: 启动中欧正式系统还是测试系统，china/test
        :return:
        """
        ss=Login_go(system).on()
        return ss

    def paotuan_on(self,sys):
        """
        调用微动跑团启动页
        :param sys: 启动正式系统还是测试系统，china/test
        :return:
        """
        ss = paotuan_go(sys).on()
        return ss

    def kehuguanli_on(self):
        """
        调用客户管理系统
        :return:
        """
        kh=zhanghao_go().on(self.url, self.user["username"], self.user["password"])
        return kh



if __name__ == "__main__":
    print("当前执行页")
    '''选择登录系统'''
    t = test()
    '''选择登录账号'''
    user = t.vchen_plus_really_really
    s=Login(system=t,user=user,rukou=2,dingzhi_y_n=2).on()
    # s=Login(system=t,user=user,rukou=0,dingzhi_y_n=2).kehuguanli_on()
    # Login().zhongou_on("china")

'''format'''
'''
sso	        plus_test
小芳	    vchen_plus3
sso-微尘	vchen_plus
SSO-Plus	plus_shop
SSO-运营版	vchen_plus3
小芳-微尘	vchen_plus2
小芳-Plus	plus_daili
'''
