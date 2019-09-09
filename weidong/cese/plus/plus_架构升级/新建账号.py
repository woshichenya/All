from login_all.login import *
from cese.plus.pack.新建账号 import *


if __name__ == "__main__":
    print("当前执行页")
    '''选择登录系统'''
    t = xingneng()
    '''选择登录账号'''
    user = t.plus_zhiying_really
    go=Login(system=t,user=user,rukou=2,dingzhi_y_n=2).on()
    go.CTag_name_zidingyi("span", "text", "设置中心", "设置中心下拉框", "展开设置中心", "Bug--无法打开设置中心")
    '''
    新建员工账号
    '''
    # go.CTag_name_zidingyi("span", "text", "成员设置", "成员设置", "进入成员设置", "Bug--无法进入成员设置")
    # go.CTag_name_zidingyi("span", "text", "新增成员", "新增成员", "进入新增成员页面", "Bug--无法打开新增成员页面")
    '''
    新建门店账号
    '''
    go.CTag_name_zidingyi("span", "text", "门店设置", "门店设置", "进入门店设置", "Bug--无法进入门店设置")
    go.CTag_name_zidingyi("span", "text", "新增门店", "新增门店", "进入新增门店页面", "Bug--无法打开新增门店页面")
    # new_user_GOv
    new_shop_GO(go)


