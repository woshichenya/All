from baibaoxiang import baibaoxiang
from login_all.pack.wchat_user import *
class wchat:
    def __init__(self,user="",username="",password=""):
        """
        微信登录脚本，填写微信公众号名称，或者输入用户名密码，即可进行UI自动登录操作——
        :param user: 填写公众号名称——
        :param username: 登录账号——
        :param password: 登录密码——
        """
        go = baibaoxiang.geturl("https://mp.weixin.qq.com/")

        if user != "":
            u=user["user"]
            p=user["password"]
        else:
            u=username
            p=password
        go.Sname("account", "用户名", u, "输入用户名", "无法输入用户名")
        go.Sname("password", "密码", p, "输入密码", "无法输入密码")
        go.CTag_name_zidingyi("a", "title", "点击登录", "登录按钮", "登录", "无法登录")
        go.llq.maximize_window()

if __name__ == "__main__":
    wchat(user=产品研发中心7,username="1",password="1")