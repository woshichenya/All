from beifen import baibaoxiang

url="http://sso.vdongchina.com"
url_dingzhi="http://sso.thefangtalk.com/"
go= baibaoxiang.geturl(url_dingzhi)

wchen_vdong={
    "username":"vdongshops",
    "password":"1234567890",
}
wchen_plus={
    "username":"18000000356",
    "password":"1234567a",
}
vchen_plus2={
    "username":"18000000486",
    "password":"1234567a",
}
plus={
    "username":"18811020000",
    "password":"12345678",
}
plus_boss={
    "username":"18100000000",
    "password":"1234567a",
}
plus_shop={
    "username":"18000000355",
    "password":"1234567a",
}


plus_admin={
    "username":"account",
    "password":"a12345678",
}
plus_daili = {
    "username": "18000000448",
    "password": "1234567a",
}
plus_test={
    "username":"18000000449",
    "password":"1234567a",
}



ho=wchen_plus
go.Sid("inphoneinput","用户名",ho["username"],"输入用户名","无法输入用户名")
go.Sid("pasword","密码",ho["password"],"输入密码","无法输入密码")
# go.Cxpath("/html/body/div[1]/div[1]/div[1]/div[6]/button","登录","登录成功","登录失败")
go.CTag_name_zidingyi("button","text","登录","登录","登录成功","登录失败")
go.llq.maximize_window()
