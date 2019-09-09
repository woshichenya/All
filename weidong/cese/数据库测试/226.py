import time
import threading
from baibaoxiang import baibaoxiangInterface,excel,sys_powel
from baibaoxiang.sql import *
from cese.数据库测试.pack.sql_user import *
import sys


xxx=[]
class a(threading.Thread):
    def __init__(self,user_sum,sqlserver,sql,sql_name):
        threading.Thread.__init__(self)
        self.user_sum=int(user_sum)
        self.sqlserver=sqlserver
        self.sql=sql
        self.sql_name=sql_name


    def run(self):
        for i in range(self.user_sum):
            sql_b = "SELECT * FROM `plus_users` WHERE user_id >"+str(i+1)
            if i == 0:
                t4 = time.time()
            go=sql()
            aa = go.lianjie_sql(self.sql_name, sql_b, self.sqlserver)
            xxx.append(aa)
            # print("第",i+1,"条：",aa)
            if i == self.user_sum - 1:
                t5 = time.time()
                kk = sys.getsizeof(xxx)
                print("共消耗时间：",float(t5) - float(t4),"秒，获取了",kk,"字节数据")



class Bingfa_test:
    def bingfa_test_go(self,user_sum,b,c):
        t1=time.time()
        k1=a(user_sum,sql_226,b,c)
        k1.start()
        t2 = time.time()
        t3 = float(t2) - float(t1)
        print("发起",user_sum,"SQL请求，共耗时：", t3,"秒")




if __name__ == "__main__":
    sql_a = "SELECT * FROM `plus_users` WHERE user_id >10"
    Bingfa_test().bingfa_test_go("1",sql_a,"plus2test")