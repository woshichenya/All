from pack.shoujihao import *

class new_user_GO:
    def __init__(self,go):
        try:
            sj = Shoujihao()
            shoujihao = sj.shouji()
            shoujihao_t="脚本"+str(shoujihao)
            go.STag_name_zidingyi("input","placeholder","请输入手机号",shoujihao,"输入手机号","输入手机号","无法输入手机号")
            input_all=go.llq.find_elements_by_tag_name("input")
            for x in input_all:
                if "请输入密码8至15位，只限英文和数字" in x.get_attribute("placeholder"):
                    x.send_keys("1234567a")
                if "请选择姓名" in x.get_attribute("placeholder"):
                    x.send_keys(shoujihao_t)

                if "请输入职位全称，不超过10个字" in x.get_attribute("placeholder"):
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

                if "请选择职位" in x.get_attribute("placeholder"):
                    print(x.text)
                #     x.click
                #     # go.CTextS("店长", "店长职位", "选中店长职位", "无法选中店长职位")
                #     print("手动选择职位")
        except:
            go.CTag_name_zidingyi("span", "text", "代理商管理", "代理商管理", "进入代理商管理", "Bug--无法打开代理商管理")

class new_shop_GO:
    def __init__(self,go):
        try:
            sj = Shoujihao()
            shoujihao = sj.shouji()
            shoujihao_t="脚本"+str(shoujihao)
            go.STag_name_zidingyi("input","placeholder","请输入门店账号",shoujihao,"输入手机号","输入手机号","无法输入手机号")

            input_all=go.llq.find_elements_by_tag_name("input")
            for x in input_all:
                if "请输入密码8至15位，只限英文和数字" in x.get_attribute("placeholder"):
                    x.send_keys("1234567a")
                if "请输入门店名称" in x.get_attribute("placeholder"):
                    x.send_keys(shoujihao_t)

                if "请填写街道地址" in x.get_attribute("placeholder"):
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

                if "请选择职位" in x.get_attribute("placeholder"):
                    x.click()
                    s_span_all = go.llq.find_elements_by_tag_name("span")
                    for s_x in s_span_all:
                        if "BOSS" in s_x.text:
                            s_x.click()
                            break
            # go.CTag_name_zidingyi("span", "text", "提交", "提交", "无法提交")
            go.Cxpath("/html/body/div[1]/div/div[2]/section/div[2]/div[2]/div/div[2]/form/div[10]/div/button[1]","提交按钮","提交","无法提交")
        except:
            go.error