from pack.Pc_pack.中欧.pack import *


class input_excel_daka_go():
    def __init__(self,system=1,sys="china"):
        """
        system:调用那个系统，中欧=1，跑团=2
        :param sys: 正式系统china;;;测试系统test;;;

        """
        g = PC_GO(system,sys)
        sum_old = []
        sum_new = []
        for x in (0, 1, 2):
            xx = g.input_excel_daka_list_print_sum(x)
            sum_old.append(xx)
        '''执行导入'''
        text_1 = g.input_excel_daka()
        for x in (0, 1, 2):
            xx = g.input_excel_daka_list_print_sum(x)
            sum_new.append(xx)
        ok = [sum_old[1], sum_new[1], sum_new[1] - sum_old[1]]
        all = [sum_old[0], sum_new[0], sum_new[0] - sum_old[0]]
        over = [sum_old[2], sum_new[2], sum_new[2] - sum_old[2]]

        '''输出区域'''
        print("*" * 60, "输出区域", "*" * 70)
        print("导入前，今天共有：%d条数据，成功：%d 条，失败：%d 条" % (all[0], ok[0], over[0]))
        print("导入后，今天共有：%d条数据，成功：%d 条，失败：%d 条" % (all[1], ok[1], over[1]))
        print("共  导  入: %d条数据，成功：%d 条，失败：%d 条" % (all[2], ok[2], over[2]))
        if text_1 != "":
            print("执行结果：", text_1)
        else:
            print("执行结果未获取到，需要进行ui判断")
        print("*" * 60, "输出结束", "*" * 70)

        g.end()

if __name__ == "__main__":
    g = input_excel_daka_go(2,"china")