import time
t=time.strftime("%Y-%m-%d", time.localtime())
print(t)

print(str(t)+" - "+str(t))

sum_old = []
sum_new = []
for x in (0, 1, 2):

    sum_old.append(x)

for x in range(6, 9):
    sum_new.append(x)

'''输出区域'''
print("*" * 60, "输出区域", "*" * 70)
print("导入前共有：%d条数据，成功：%d条，失败：%d条"%(sum_old[0],sum_old[1],sum_old[2]))
print("导入后共有：%d条数据，成功：%d条，失败：%d条"%(sum_new[0],sum_new[1],sum_new[2]))
print("一共导入了", sum_new[0]-sum_old[0], "条数据","成功：%d条；；；失败：%d条"%(sum_new[1]-sum_old[1],sum_new[2]-sum_old[2]))
print("*" * 60, "输出结束", "*" * 70)