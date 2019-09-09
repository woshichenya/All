from baibaoxiang import baibaoxiang


class zhanghao_go():
    def on(self,url,username,password):
        xx = 1
        go = baibaoxiang.geturl(url)
        print("url是：",url)
        go.Sid("login-username","用户名",username,"输入用户名","无法输入用户名")
        go.Sid("login-password","密码",password,"输入密码","无法输入密码")
        go.CTag_name_zidingyi("button","type","submit","登录按钮","登录成功","登录失败")
        go.llq.maximize_window()
        return go

if __name__ == "__mian__":
    print("当前为启动页")
    user=""
    username=""
    pasword=""
    zhanghao_go().on(username,pasword)