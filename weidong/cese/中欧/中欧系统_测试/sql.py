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