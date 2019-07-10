import login_all.login
from selenium.webdriver.common.keys import *
from pack.shoujihao import *


a=login_all.login.Login()
go=a.on("test","plus_admin","","")
go.CTag_name_zidingyi("span","text","账号管理","账号管理下拉框","展开账号管理","Bug--无法打开账号管理")
go.CTag_name_zidingyi("span","text","直营管理","直营管理","进入直营管理","Bug--无法打开直营管理")
go.CTag_name_zidingyi("span", "text", "账号管理", "账号管理", "进入账号管理", "Bug--无法打开账号管理")


aa = go.llq.find_elements_by_tag_name("span")
print("共", len(aa), "个", "span", "控件")
for a in aa:
        a_gei_get_zidingyi = a.text
        print(a_gei_get_zidingyi)
        if a_gei_get_zidingyi == "账号管理":
                a.send_keys(Keys.ENTER)
                break

