import os

for i in range (1,3):
    sogo_cmd = "adb shell ime set com.sohu.inputmethod.sogou/.SogouIME"
    p=os.popen(sogo_cmd)
    print(p.read())






