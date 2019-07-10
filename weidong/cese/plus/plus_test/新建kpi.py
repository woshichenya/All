from baibaoxiang import baibaoxiangInterface
url="https://test-plus.moliyan.com.cn/api/Kpi/add"
data={
    "name":"1905",
    "type":"1",
    "data[0][id]":"100",
    "data[0][target]":"100",
    "data[0][data][0-0]":"1",
    "data[0][data][1-5]":"50",
    "data[0][data][6-10]":"100",
    "data[0][weight]":"100",
    "uids":"1067,1435",
    "date":"2019-05",
    "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwbHVzIiwiaWF0IjoxNTU2MjU4MDI2LCJleHAiOjE1NTYzNDQ0MjYsInVpZCI6IjEwMTYifQ.s_VQXxi-EPc-4li3eNdSvMFHlYQ5hG5bDMjhxBJloH8",
}
baibaoxiangInterface.go().post(url,data,"","添加考核")