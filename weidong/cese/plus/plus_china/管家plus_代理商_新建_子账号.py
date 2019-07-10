from login_all.login import *
from pack.shoujihao import *


a=Login(china(),china().plus_daili,"plus")
go=a.on()


go.CTag_name_zidingyi("span","text","账号管理","账号管理下拉框","展开账号管理","Bug--无法打开账号管理")
go.CTag_name_zidingyi("span","text","代理商管理","代理商管理","进入代理商管理","Bug--无法打开代理商管理")
for i in range (1,3):
    go.CTag_name_zidingyi("span","text","开通子账号","开通子账号","进入开通子账号","Bug--无法打开开通子账号")
    try:
        sj=Shoujihao()
        shoujihao=sj.shouji()
        shoujihao_t="脚本"+str(shoujihao)
        go.STag_name_zidingyi("input","placeholder","请输入手机号",shoujihao,"输入手机号","输入手机号","无法输入手机号")
        input_all=go.llq.find_elements_by_tag_name("input")
        for x in input_all:
            if "password" in x.get_attribute("type"):
                x.send_keys("1234567a")
            if "请输入姓名" in x.get_attribute("placeholder"):
                x.send_keys(shoujihao_t)
            if "请输入所属公司" in x.get_attribute("placeholder"):
                x.send_keys(shoujihao_t)
            if "省级地区" in x.get_attribute("placeholder"):
                x.click()
                s_span_all=go.llq.find_elements_by_tag_name("span")
                for s_x in s_span_all:
                    if "湖北省" in s_x.text:
                        s_x.click()
                        break
            if "市级地区" in x.get_attribute("placeholder"):
                x.click()
                s_span_all=go.llq.find_elements_by_tag_name("span")
                for s_x in s_span_all:
                    if "襄阳市" in s_x.text:
                        s_x.click()
                        break

            if "请选择版本" in x.get_attribute("placeholder"):
                x.click()
                s_span_all=go.llq.find_elements_by_tag_name("span")
                for s_x in s_span_all:
                    if "综合版" in s_x.text:
                        s_x.click()
                        break
            if "请选择" in x.get_attribute("placeholder"):
                x.click()
                s_span_all=go.llq.find_elements_by_tag_name("span")
                for s_x in s_span_all:
                    if "1年" in s_x.text:
                        s_x.click()
                        break
            s_span_all = go.llq.find_elements_by_tag_name("span")
            for s_x in s_span_all:
                if "提交" in s_x.text:
                    s_x.click()
                    break
    except:
        go.CTag_name_zidingyi("span", "text", "代理商管理", "代理商管理", "进入代理商管理", "Bug--无法打开代理商管理")
