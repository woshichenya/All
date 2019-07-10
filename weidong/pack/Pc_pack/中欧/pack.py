from login_all.login import *
import time


"""
通用数据模块
"""
'''导入文件路径'''
excel_addres = "D:\工作文件\项目\中欧项目\\190613导入打卡\\11111runkmTemplate.xls"
'''获取数量的path路径'''
sum_daoru_xpath = "/html/body/div[1]/main/div[2]/div/div/div/div[2]/div/div[4]/div/div/div/div/strong[2]"
'''获取今天日期'''
t = time.strftime("%Y-%m-%d", time.localtime())
time_riqi = str(t) + " - " + str(t)
'''获取成功CSS路径'''
ok_css = "html.no-focus body span.select2-container.select2-container--default.select2-container--open span.select2-dropdown.select2-dropdown--below span.select2-results ul#select2-search_status-results.select2-results__options"
over_css="html.no-focus body span.select2-container.select2-container--default.select2-container--open span.select2-dropdown.select2-dropdown--below span.select2-results ul#select2-search_status-results.select2-results__options li#select2-search_status-result-07g6-2.select2-results__option.select2-results__option--highlighted"

"""
通用数据模块
"""




class PC_GO():
    def __init__(self,system=2, sys="test"):
        """
        system:调用那个系统，中欧=1，跑团=2
        :param sys: 正式系统china;;;测试系统test;;;
        """
        '''执行登录'''
        if system == 2:
            go = Login().paotuan_on(sys)
        elif system == 1:
            go = Login().zhongou_on(sys)
        self.go = go

    def input_excel_daka(self):

        '''执行导入报表'''
        self.go.CText_partial_s("打卡列表", "打卡列表菜单", "进入打卡列表菜单", "无法进入打卡列表菜单")
        self.go.CTag_name_zidingyi("a", "title", "导入跑步数据", "导入跑步数据按钮", "进入导入页面", "无法进入导入页面")
        self.go.Sname("file", "导入文件", excel_addres, "添加表格完成", "添加表格失败")
        self.go.CTag_name_zidingyi("input", "type", "submit", "提交导入表格", "提交表格成功", "提交失败")
        for i in range(1, 40):
            try:
                out_text = self.go.llq.find_element_by_xpath("/html/body/div[1]/div/div/h1").text
            except:
                out_text = "无法截取结果"
                self.go.error()
            if out_text != "":
                print("第", i, "次运行,获取到运行结果：", out_text)
                break
        return out_text

    def input_excel_daka_list_print_sum(self, ok_or_over=0):
        """
        :param ok_or_over: 1=成功 ;;2=失败；；；0=全部
        :return:
        """
        '''查看导入数据记录'''
        self.go.CText_partial_s("查看导入数据记录", "查看导入数据记录菜单", "进入查看导入数据记录菜单", "无法进入查看导入数据记录菜单")
        try:
            sum_daoru_all = self.go.llq.find_element_by_xpath(sum_daoru_xpath).text
        except:
            self.go.error()
            print("无法获取全部导入数量，ui可能发生变化，需要及时更新")
        self.go.Sname("created_at", "日期控件", time_riqi, "已输入日期", "无法输入日期")
        if ok_or_over == 0:
            self.go.CTag_name_zidingyi("span", "text", "×", "清空搜索", "删除搜索条件", "无法删除搜索条件")
        if ok_or_over == 1:
            self.go.CTag_name_zidingyi("span", "id", "select2-search_status-container", "搜索下拉框", "展开下拉框", "无法展开下拉框")
            try:
                self.go.llq.find_element_by_css_selector(ok_css).click()
            except:
                self.go.error()
                print("无法选择成功选项，检查css路径是否正确")
        self.go.CTag_name_zidingyi("button", "type", "submit", "搜索按钮", "执行搜索", "无法点击搜索")
        try:
            sum_daoru = self.go.llq.find_element_by_xpath(sum_daoru_xpath).text
            return int(sum_daoru)
        except:
            self.go.error()
            return 0

    def user_new(self,nickename="test",name="test",sex=1):
        """
        :param nickename: 昵称；；；
        :param name: 真实姓名；；；
        :param sex: 性别，1=男，2=女；；；
        :return:
        """
        a = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "`", "~", "￥", "[", "]", "\\", "{",
             "}", "|", ";", "", ":", "\"", ",", ".", "/", "<", ">", "?"]
        if sex == 1 :
            sex ="男"
        elif sex ==2 :
            sex ="女"
        self.go.CTag_name_zidingyi("span", "text", "用户管理", "用户管理菜单", "打开用户管理菜单", "无法打开用户管理菜单")
        self.go.CText_partial_s_key("会员用户", "会员用户菜单", "进入会员用户菜单", "进入会员用户菜单报错")
        self.go.CText_partial_s_key("新增", "新增会员", "进入新增会员", "进入新增会员报错")
        self.go.Sid("nickname", "用户名输入框", nickename, "输入名称", "无法输入名称")
        self.go.Sid("name", "真实姓名输入框", name, "输入真实姓名", "无法输入真实姓名")
        # self.go.Cid(sex, "性别", "选择性别", "无法选择性别")
        self.go.CTag_name_zidingyi("label","text",sex,"性别", "选择性别", "无法选择性别")
        # 提交
        self.go.CTag_name_zidingyi("button", "type", "submit", "提交按钮", "点击提交按钮", "无法点击提交按钮")


    def end(self):
        time.sleep(120)
        self.go.llq.quit()


        # g.end()


if __name__ == "__main__":
    g = PC_GO(2, "test").user_new()
