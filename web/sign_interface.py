from flask import Flask, request
import json
import hashlib
import time

app = Flask(__name__)

####参考网址——

# 只接受POST方法访问

@app.route("/getSign", methods=["POST"])
def check():
    # 默认返回内容
    return_dict = {"return_code": "200", "return_info": "处理成功", "result": False}
    # 判断入参是否为空
    if request.get_data() is None:
        return_dict["return_code"] = "5004"
        return_dict["return_info"] = "请求参数为空"
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的参数
    get_Data = request.get_data()
    print(type(get_Data))
    print(get_Data)
    # 传入的参数为bytes类型，需要转化成json
    get_Data = json.loads(get_Data)


    #name = get_Data.get("name")
    #age = get_Data.get("age")
    myKey = "75cfb1b37a20579ce069ae6a6d23192e"   #######第三方京东拉新的秘钥
    #myKey = "5577e10dd45dec0c528e1c3eefa31adc"  #######内部自己做的接口定制的秘钥
    # 对参数进行操作

    return_dict["result"] = signature(get_Data,myKey)
    now=time.time()
    return_dict["now"] = now

    return json.dumps(return_dict, ensure_ascii=False)  ###返回json格式的


# 功能函数
def signature(data_source, private_key):           ###需要传入的参数：data_source是一个字典，private_key是私钥
    #data_source["key"] = private_key
    data_source["secret"] = private_key
    # md5签名
    result = hashlib.md5(sort_to_str(data_source,private_key).encode(encoding="utf-8"))
    # 转化为16进制
    result = result.hexdigest().upper()
    print("md5签名值是:{}".format(result))
    return result


def sort_to_str(data_source,private_key):
    """ 对传入的数据升序排序后并返回 """
    result_str = ""
    print("排序前的数据是:{}".format(data_source))
    # 对字典升序排序,sorted默认为升序排序
    sorted_result = sorted(data_source.items(), reverse=False)
    print("排序后的数据是:{}".format(sorted_result))
    # 遍历数组
    for i in range(0, len(sorted_result)):
        data_i = sorted_result[i]
        # 拼接字符串：key1=value1&key2=value2
        d_str = data_i[0] + "=" + data_i[1] + "&"
        result_str = result_str + d_str
    # 截取最后一个&符号
    if len(result_str) > 0:
        result_str = result_str[0:len(result_str) - 1]
        print("截取最后一个&符号:{}".format(result_str))

    return result_str+"&key="+private_key


if __name__ == "__main__":
    app.run(debug=True)
