from baibaoxiang import sql
go=sql.sql()
sql_a="SELECT SUM(run_time),SUM(pace)/COUNT(run_time),SUM(run_km) FROM `vd_attendance`"
aa=go.lianjie_sql("vd_183run",sql_a)
pace=aa[0][1]
run_time=aa[0][0]
run_km=aa[0][2]
print("数据报表，平均配速",int(pace/60),"分",int(pace%60),"秒")
print("数据报表，总时长",int(run_time/3600),"小时",int(int(run_time%3600)/60),"分",int(run_time%60),"秒")
print("数据报表，总距离",run_km,"公里")

# print(aa[0][1])