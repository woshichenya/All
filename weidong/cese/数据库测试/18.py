import time
import threading
from baibaoxiang import baibaoxiangInterface,excel,sys_powel
from baibaoxiang.sql import *
from cese.数据库测试.pack.sql_user import *



class a(threading.Thread):
    def __init__(self,user_sum):
        threading.Thread.__init__(self)
        self.user_sum=int(user_sum)


    def run(self):
        for i in range(self.user_sum):
            go=sql()
            sql_a = "SELECT * FROM `plus_users` WHERE user_id >10"
            aa = go.lianjie_sql("plus2test", sql_a, sql_18)





class Bingfa_test:
    def bingfa_test_go(self,user_sum):
        t1=time.time()
        k1=a(user_sum)
        k1.start()
        t2 = time.time()
        t3 = float(t2) - float(t1)
        print("发起",user_sum,"请求，共耗时：", t3,"秒")




if __name__ == "__main__":
    Bingfa_test().bingfa_test_go(1000)