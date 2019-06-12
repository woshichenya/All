from beifen import baibaoxiang




url = "http://test-183run-admin.vdongchina.com/admin.php/user/publics/signin.html"
go = baibaoxiang.geturl(url)
admin = {
    "username": "admin",
    "password": "admin",
}
whu=admin
go.Sid("login-username","用户名",whu["username"],"输入用户名","无法输入用户名")
go.Sid("login-password","密码",whu["password"],"输入密码","无法输入密码")
# go.Cxpath("/html/body/div[1]/div[1]/div[1]/div[6]/button","登录","登录成功","登录失败")
go.CTag_name_zidingyi("button","text","登 录","登录","登录成功","登录失败")
go.llq.maximize_window()
#http://183run-admin.vdongchina.com/admin.php/user/publics/signin.html
go.CText_partial_s_key("183RUN","183RUN菜单","进入183RUN菜单","183RUN菜单报错")



'''
SELECT * from vd_users WHERE user_id =1;
SELECT * FROM `vd_attendance` WHERE  user_id =1;
SELECT user_id FROM `vd_attendance` WHERE created_at <1556640000  GROUP BY user_id; #五月前有多少id打过卡
SELECT user_id FROM `vd_attendance`  GROUP BY user_id;#所有打卡人员的id
SELECT * FROM `vd_attendance`  GROUP BY user_id;#共有多少个人打卡
SELECT * FROM `vd_attendance` WHERE created_at >1556640000 and user_id =17;
SELECT * FROM `vd_attendance` WHERE created_at >1556640000 and user_id =4;
SELECT sum(run_km) FROM `vd_attendance` WHERE created_at >1556640000 and user_id =17;
SELECT * FROM `vd_attendance` WHERE attendance_time >1556640000 GROUP BY user_id;
'''
