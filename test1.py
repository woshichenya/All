sum_old = []
sum_new = []
for x in (0, 1, 2):
    sum_old.append(x)
'''执行导入'''
for x in (0, 1, 2):

    sum_new.append(x)

ok = [sum_old[1], sum_new[1], sum_new[1] - sum_old[1]]
all = [sum_old[0], sum_new[0], sum_new[0] - sum_old[0]]
over = [sum_old[2], sum_new[2], sum_new[2] - sum_old[2]]

'''输出区域'''
print("*" * 60, "输出区域", "*" * 70)
print("导入前，今天共有：%d条数据，成功：%d 条，失败：%d 条" % (all[0],ok[0] ,over[0]))
print("导入后，今天共有：%d条数据，成功：%d 条，失败：%d 条" % (all[1],ok[1] ,over[1]))
print("共  导  入: %d条数据，成功：%d 条，失败：%d 条" % (all[2],ok[2] ,over[2]))
print("*" * 60, "输出结束", "*" * 70)