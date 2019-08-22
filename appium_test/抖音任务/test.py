import threading
from appium import webdriver
import time
import traceback
from appium_test.抖音任务.数据 import *


class fangou:
    def Cid(self,driver,shuxing ,name,ok,over,Time=30):
        xxx = 1
        i = 1
        while xxx == 1 and i < Time:
            try:
                driver.find_element_by_id(shuxing)
                print(name, "存在，执行下一步")
                xxx = 2
                i = 1
                while xxx == 2 and i < Time:
                    try:
                        i = 1
                        driver.find_element_by_id(shuxing).click()
                        print(ok)
                        xxx = 3
                    except:
                        print(over, "执行等待操作，当前执行", i, "次")
                        i += 1
            except:
                print(name, "不存在，执行等待操作，当前等待", i, "秒")
                i += 1
                time.sleep(1)
                ee = traceback.format_exc()
        if xxx == 1 and i == Time:
            print("报错开始")
            print(ee)
            print("报错结束")

    def Sid(self,driver,shuxing ,input_text,name,ok,over,Time=30):
        xxx = 1
        i = 1
        while xxx == 1 and i < Time:
            try:
                driver.find_element_by_id(shuxing)
                print(name, "存在，执行下一步")
                xxx = 2
                i = 1
                while xxx == 2 and i < Time:
                    try:
                        i = 1
                        driver.find_element_by_id(shuxing).send_keys(input_text)
                        print(ok)
                        xxx = 3
                    except:
                        print(over, "执行等待操作，当前执行", i, "次")
                        i += 1
            except:
                print(name, "不存在，执行等待操作，当前等待", i, "秒")
                i += 1
                time.sleep(1)
                ee = traceback.format_exc()
        if xxx == 1 and i == Time:
            print("报错开始")
            print(ee)
            print("报错结束")


    def Cxpth(self,driver,shuxing ,name,ok,over,Time=30):
        xxx = 1
        i = 1
        while xxx == 1 and i < Time:
            try:

                driver.find_element_by_xpath(shuxing)
                print(name, "存在，执行下一步")
                xxx = 2
                i = 1
                while xxx == 2 and i < Time:
                    try:
                        i = 1
                        driver.find_element_by_xpath(shuxing).click()
                        print(ok)
                        xxx = 3
                    except:
                        print(over, "执行等待操作，当前执行", i, "次")
                        i += 1
            except:
                print(name, "不存在，执行等待操作，当前等待", i, "秒")
                i += 1
                time.sleep(1)
                ee = traceback.format_exc()
        if xxx == 1 and i == Time:
            print("报错开始")
            print(ee)
            print("报错结束")

    def fangou_zuobiao_click(self,driver,x,y,endx,endy):
        driver.tap([(x, y), (endx, endy)], 500)