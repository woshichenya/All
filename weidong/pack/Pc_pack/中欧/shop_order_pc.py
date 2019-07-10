from login_all.login import *
import time

class Shop_order_pc():
    def __init__(self, sys,s):
        """
        后台补录订单
        :param sys: 正式系统china;;;测试系统test;;;
        """
        '''获取今天日期'''
        t = time.strftime("%Y-%m-%d", time.localtime())
        self.time_riqi = str(t) + " - " + str(t)
        '''执行登录'''
        self.go = Login().zhongou_on(sys)
        self.s=s

    def shop_order_go(self):
        self.go.CTag_name_zidingyi("a","data-original-title","兑换","兑换按钮","点击兑换","无法点击兑换")
        '''记录当前商品数量'''
        # self.go.llq.

    def to_shop_sum(self):
        self.go.CTag_name_zidingyi("span","text","商品管理","商品管理菜单","进入商品管理菜单","无法进入商品管理菜单")
        for i in self.s:
            self.go.Sid("search_title","商品名称",i,"输入商品名","无法输入商品名")
            self.go.CTag_name_zidingyi("button","type","submit","搜索按钮","执行搜索","无法执行搜索")
            





class Shop_order_pc_go():
    def __init__(self,sys):
        g = Shop_order_pc(sys)
        ######商品管理
        g.to_shop_sum()




if __name__ == "__main__":
    g = Shop_order_pc_go("test")