import threading
from appium import webdriver
import time
import traceback
from appium_test.抖音任务.数据 import *
from appium_test.抖音任务.test import *




class Douyin_Go(threading.Thread):
    def __init__(self,des):
        threading.Thread.__init__(self)
        self.mobile_name=des["mobile_name"]
        self.des=des
        self.PC='http://'+des["PC_ip"]+':'+des["PC_port"]+'/wd/hub'

    def run(self):
        time_on=time.time()
        try:
            print("执行手机为：",self.mobile_name,"本次开始执行时间：",time_on)
            driver = webdriver.Remote(self.PC,self.des)
            print(self.mobile_name, "已启动抖音")
            fangou().Cid(driver, "com.ss.android.ugc.aweme:id/y0", "个人信息保护指引", "关闭个人信息保护指引", "没有个人信息保护指引",Time=5)
            try:
                driver.find_element_by_id("com.ss.android.ugc.aweme:id/dhn")
                fangou().Cid(driver, "com.ss.android.ugc.aweme:id/dhn", "青少年模式提示框", "关闭青少年模式提示框", "没有青少年模式提示框",Time=5)
            except:
                driver.tap([(183, 437),(190,440)],500)
                print("点击任一位置解除提示框")
            '''
            点击搜索
            '''
            bozhu_name="东尔夋"
            bozhu_num="1981646269"
            fangou().Cxpth(driver,"//android.widget.ImageView[@content-desc='搜索']","搜索按钮","点击搜索按钮","无法点击搜索按钮")

            fangou().Cid(driver,"com.ss.android.ugc.aweme:id/aai","搜索框","点击搜索内容","点击输入搜索内容")
            fangou().Sid(driver,"com.ss.android.ugc.aweme:id/aai",bozhu_name,"搜索框","输入搜索内容","无法输入搜索内容")
            xf=driver.find_element_by_id("com.ss.android.ugc.aweme:id/aai").text
            fangou().Cid(driver,"com.ss.android.ugc.aweme:id/di9","搜索按钮","开始搜索","无法开始搜索")
            fangou().Cid(driver,"com.ss.android.ugc.aweme:id/dli","第一个播主名称","点击进入第一个播主","无法进入第一个播主")



        except Exception as e:
            ee = traceback.format_exc()
            print(self.mobile_name,"开始打印错误日志")
            print(ee)
            print(self.mobile_name,"结束打印错误日志")
        time_off = time.time()
        print("执行手机为：", self.mobile_name, "本次结束执行时间是：", time_off)
        print(self.mobile_name,"执行时长:",time_off-time_on,"秒")