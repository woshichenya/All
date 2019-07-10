from baibaoxiang import baibaoxiang
from selenium.webdriver.common.keys import Keys
import time
import traceback

class login_go():
    def on(self,url,username,password,rukou):
        xx = 1
        go = baibaoxiang.geturl(url)
        go.Sid("inphoneinput","用户名",username,"输入用户名","无法输入用户名")
        go.Sid("pasword","密码",password,"输入密码","无法输入密码")
        go.CTag_name_zidingyi("button","text","登录","登录","登录成功","登录失败")
        go.llq.maximize_window()
        shuxing="默认值"
        if rukou=="plus":
            print("进入管家plus")
            go.Cxpath("/html/body/div[2]/ul/li[2]/div[1]/a", "运营系统入口", "进入运营系统", "无法进入运营系统")
            shuxing = "进入系统"
            sum=1
        if rukou=="yunying":
            print("进入管家plus运营版")
            xx=2
            go.Cxpath("/html/body/div[2]/ul/li[3]/div[1]/a","运营系统入口","进入运营系统","无法进入运营系统")
        if rukou=="vchen":
            print("进入微尘4.0")
            go.Cxpath("/html/body/div[2]/ul/li[1]/div[1]/a", "运营系统入口", "进入运营系统", "无法进入运营系统")
            shuxing = "进入系统"
            sum=0
        # print(shuxing)

        return go

if __name__ == "__mian__":
    print("当前为启动页")
    user=""
    username=""
    pasword=""
    login_go().on(username,pasword)