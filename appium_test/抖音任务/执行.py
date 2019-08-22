import threading
from appium import webdriver
import time
import traceback
from appium_test.抖音任务.数据 import *
from appium_test.抖音任务.步骤 import *




if __name__=="__main__":
    desired_caps_douyin = {
        'unicodeKeyboard': "True",
        'resetKeyboard': "True",
        # 'noReset': True,
        "platformName": "Android",
        "appPackage": "com.ss.android.ugc.aweme",
        "appActivity": ".main.MainActivity",
        'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'},
    }
    test_douyin_mobile_data().desired_caps_testJ110.update(desired_caps_douyin)
    t=test_douyin_mobile_data().desired_caps_testJ110
    k2=Douyin_Go(t)
    k2.start()

