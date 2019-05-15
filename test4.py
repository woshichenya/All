# from baibaoxiang import baibaoxiangMobile
# baibaoxiangMobile.MGO().go()
from appium import webdriver
import time
from baibaoxiang import femail
import traceback
import requests
import json
from PIL import Image
import pytesseract





class MGO():

    '''封装wechat方法'''
    def go(self):
        MGO.bug_num=0
        desired_caps = {}
        desired_caps = {
              "platformName": "Android",
              "platformVersion": "9",
              "deviceName": "7&1c3e0558&0&0001",
              "noReset": True,
              "appPackage": "com.tencent.mm",
              "appActivity": "com.tencent.mm.ui.LauncherUI"
        }
        # desired_caps = {
        #     'platformName': 'Android',
        #     'platformVersion': '5.1',
        #     # 'platformVersion': '4.4.2',
        #     # 'deviceName': '127.0.0.1:62001',
        #     #'deviceName': '10.130.33.11:5555',
        #     'deviceName': '10.130.32.191:5555',
        #     'unicodeKeyboard': True,
        #     'resetKeyboard': True,
        #     'noReset': True,
        #     'appPackage': 'com.tencent.mm',
        #     'appActivity': 'com.tencent.mm.ui.LauncherUI',
        #     'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
        # }
        '''开始启动程序'''
        i=1
        go=1

        try:
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
            #self.driver = webdriver.Remote('http://127.0.0.1:5555/wd/hub', desired_caps)
            print("启动手机程序打开微信")
            self.driver.implicitly_wait(5)
            print("已经打开微信程序")
            self.driver.implicitly_wait(5)
            print("等待五秒")
            time.sleep(10)
            go=2
        except Exception as e:
            ee = traceback.format_exc()
            print("开始打印错误日志")
            print(ee)
            print("结束打印错误日志")
            i+=1
            time.sleep(1)

MGO().go()