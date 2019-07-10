from baibaoxiang import baibaoxiang

go= baibaoxiang.geturl("https://open.weixin.qq.com/")

test_ceshi={
    "username":"vdong06@sohu.com",
    "password":"vdong123"
}
china={
    "username":"kfpt0001@163.com",
    "password":"sunqiuping123"
}
china2={
    "username":"yuyan@vdongchina.com",
    "password":"vdongchina123"
}
url1=go.llq.current_url
go.llq.maximize_window()
ho = china
go.Cid("loginBarBt","登录框","打开登录框","无法找到登录按钮")
go.STag_name_zidingyi("input","placeholder","请填写登录邮箱",ho["username"],"用户名输入框","ok","no ok")
go.STag_name_zidingyi("input","placeholder","请填写密码",ho["password"],"用户名输入框","ok","no ok")
url2 =go.llq.current_url
login=go.llq.find_elements_by_link_text("登录")

for ll in login:
    ll.click()
