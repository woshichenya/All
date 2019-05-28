from beifen import baibaoxiang

url="http://ceshi-sso.vdongchina.com"
go= baibaoxiang.geturl(url)
wchen_shoptest={
    "username":"shoptester",
    "password":"ceshi123",
}
wchen_admin={
    "username":"maxstone",
    "password":"vdongchina2019",
}

'''
plus账号
'''
plus_admin={
    "username":"17400000000",
    "password":"12345678",
}
plus_boss={
    "username":"18000000482",
    "password":"1234567a",
}
plus_shop={
    "username":"18000000484",
    "password":"1234567a",
}
vchen_plus={
    "username":"18000000483",
    "password":"1234567a",
}
plus_test={
    "username":"18000000512",
    "password":"1234567a",
}





ho=wchen_shoptest
go.Sid("inphoneinput","用户名",ho["username"],"输入用户名","无法输入用户名")
go.Sid("pasword","密码",ho["password"],"输入密码","无法输入密码")
# go.Cxpath("/html/body/div[1]/div[1]/div[1]/div[6]/button","登录","登录成功","登录失败")
go.CTag_name_zidingyi("button","text","登录","登录","登录成功","登录失败")
go.llq.maximize_window()











