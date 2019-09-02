import threading
from appium import webdriver
import time
import traceback
from appium_test.抖音任务.数据 import *
from appium_test.抖音任务.test import *
import os

app_cmd="adb shell ime set io.appium.android.ime/.UnicodeIME"
sogo_cmd="adb shell ime set com.sohu.inputmethod.sogou/.SogouIME"



go=fangou()


class Douyin_Go(threading.Thread):
    def __init__(self,des):
        threading.Thread.__init__(self)
        self.mobile_name=des["mobile_name"]
        self.des=des
        self.PC='http://'+des["PC_ip"]+':'+des["PC_port"]+'/wd/hub'

    def run(self):
        time_on=time.time()
        try:
            '''
            启动抖音************0****************************************************************************
            '''
            print("执行手机为：",self.mobile_name,"本次开始执行时间：",time_on)
            driver = webdriver.Remote(self.PC,self.des)
            print(self.mobile_name, "已启动抖音")
            tx1=time.time()
            print("启动抖音共用了：",tx1-time_on,"秒")

            '''
            检测提示框************0****************************************************************************
            '''
            driver.tap([(183, 437), (190, 440)], 500)
            print("先点一次")
            geren_baohu="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[3]"
            go.Cxpth(driver, geren_baohu, "个人信息保护指引", "关闭个人信息保护指引", "没有个人信息保护指引",Time=5)
            try:
                driver.find_element_by_id("com.ss.android.ugc.aweme:id/dhn")
                fangou().Cid(driver, "com.ss.android.ugc.aweme:id/dhn", "青少年模式提示框", "关闭青少年模式提示框", "没有青少年模式提示框",Time=5)
            except:
                driver.tap([(183, 437),(190,440)],500)
                print("点击任一位置解除提示框")
                time.sleep(3)
            tx2 = time.time()
            print("检测提示共用了：", tx2 - tx1, "秒")

            '''
            点击搜索************0****************************************************************************
            '''
            bozhu_name='东尔夋'
            fangou().Cxpth(driver,"//android.widget.ImageView[@content-desc='搜索']","搜索按钮","点击搜索按钮","无法点击搜索按钮")
            # fangou().Cxpth(driver,"//android.widget.Button[@content-desc='搜索']","搜索按钮","点击搜索按钮","无法点击搜索按钮")
            '''
            在输入框输入搜索内容,开始搜索************0****************************************************************************
            '''
            # os.popen(sogo_cmd)
            input_button="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.EditText"
            go.Cxpth(driver,input_button,"输入框","点击搜索输入框","无法点击搜索输入框")
            go.Sxpath(driver,input_button,"东尔夋","输入框","输入搜索内容框","无法输入搜索内容框")
            '''
            切回搜狗输入法
            '''

            time.sleep(3)
            t = os.popen(sogo_cmd)
            print(t.read())
            print("键盘回车，开始搜索")
            time.sleep(3)
            driver.press_keycode(66)

            fangou().Cid(driver,"com.ss.android.ugc.aweme:id/dli","第一个播主名称","点击进入第一个播主","无法进入第一个播主")



        except Exception as e:
            ee = traceback.format_exc()
            print(self.mobile_name,"开始打印错误日志")
            print(ee)
            print(self.mobile_name,"结束打印错误日志")
        time_off = time.time()
        print("执行手机为：", self.mobile_name, "本次结束执行时间是：", time_off)
        print(self.mobile_name,"执行时长:",time_off-time_on,"秒")