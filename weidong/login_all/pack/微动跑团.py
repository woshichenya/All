from baibaoxiang import baibaoxiang
import time

class paotuan_go():
    def __init__(self,system="test"):
        """
        :param system: 选择打开的系统
        """
        self.system=system
        if self.system == "test":
            print("测试系统")
            self.url="http://test-run-admin.molixyou.com/admin.php"
            self.admin = {
                "username": "admin",
                "password": "admin",
            }
        if self.system == "china":
            print("正式系统")
            self.url="http://run-admin.molixyou.com/"
            self.admin = {
                "username": "admin",
                "password": "admin",
            }


    def on(self):
        go = baibaoxiang.geturl(self.url)
        whu=self.admin
        go.Sid("login-username","用户名",whu["username"],"输入用户名","无法输入用户名")
        go.Sid("login-password","密码",whu["password"],"输入密码","无法输入密码")
        go.CTag_name_zidingyi("button","text","登 录","登录","登录成功","登录失败")
        go.llq.maximize_window()
        old_url=go.llq.current_url
        while old_url == go.llq.current_url :
            go.CText_partial_s_key("微动跑团", "微动跑团", "进入微动跑团", "进入微动跑团菜单报错")
            time.sleep(2)

        return go



if __name__ == "__main__":
    paotuan_go("china").on()