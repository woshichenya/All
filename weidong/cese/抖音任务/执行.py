import threading
from appium import webdriver
import time
import traceback
from cese.抖音任务.数据 import *
from cese.抖音任务.步骤 import *




if __name__=="__main__":
    D15=test_douyin_mobile_data().desired_caps_testD15
    # D15=test_douyin_mobile_data().desired_caps_xiaomi8
    desired_caps_douyin = {
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True,
        "platformName": "Android",
        "appPackage": "com.ss.android.ugc.aweme",
        "appActivity": ".main.MainActivity",
        'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'},
    }
    D15.update(desired_caps_douyin)
    t=D15
    k2=Douyin_Go(t)
    k2.start()
