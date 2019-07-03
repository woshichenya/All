from baibaoxiang import baibaoxiang
from selenium.webdriver import ActionChains
import time

go=baibaoxiang.geturl("https://www.qichacha.com/user_login?back=%2F")
go.llq.maximize_window()
go.Cid("normalLogin","账号密码登录",2,3)
go.Sid("nameNormal","用户名","18803000357",1,2)
go.Sname("pwdNormal","密码","a111111",1,2)
tuo=go.llq.find_element_by_id("nc_1_n1z")
print("开始悬停")
l=ActionChains(go.llq)
l.move_to_element(tuo).perform()
print("开始拖拽")
try:
    l.click_and_hold(on_element=tuo).perform()
    time.sleep(0.15)
    l.move_to_element_with_offset(to_element=tuo, xoffset=400, yoffset=10).perform()
    time.sleep(1)
except:
    go.error()
go.CTag_name_zidingyi("button","type","submit","登录按钮",1,2)



time.sleep(5)
go.llq.quit()
print("关闭浏览器")
