from baibaoxiang import baibaoxiang
import time

class Login_go():
    def __init__(self,system="test"):
        """

        :param system: 选择打开的系统
        """
        self.system=system
        if self.system == "test":
            print("测试系统")
            # self.url="http://test-183run-admin.vdongchina.com/admin.php"
            self.url="http://test-183run-admin.vdongchina.com.cn/admin.php"

            self.admin = {
                "username": "admin",
                "password": "admin",
            }
        if self.system == "china":
            print("正式系统")
            # self.url="http://183run-admin.vdongchina.com/admin.php"
            self.url = "http://183run-admin.vdongchina.com.cn/admin.php"
            self.admin = {
                "username": "admin",
                "password": "vdong123",
            }


    def on(self):
        go = baibaoxiang.geturl(self.url)

        whu=self.admin
        go.Sid("login-username","用户名",whu["username"],"输入用户名","无法输入用户名")
        go.Sid("login-password","密码",whu["password"],"输入密码","无法输入密码")
        go.CTag_name_zidingyi("button","text","登 录","登录","登录成功","登录失败")
        go.llq.maximize_window()
        old_url = go.llq.current_url
        while old_url == go.llq.current_url:
            go.CText_partial_s_key("183RUN", "183RUN菜单", "进入183RUN菜单", "183RUN菜单报错")
            time.sleep(2)
        return go



if __name__ == "__main__":
    Login_go("china").on()