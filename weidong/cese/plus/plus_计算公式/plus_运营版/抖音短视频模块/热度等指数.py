import math
class zhishu:
    def reduzhishu(self,X2,X3,X4):
        x = 0.17 * float(math.log(X2 + 1)) + 0.37 * float(math.log(X3 + 1)) + 0.46 * float(math.log(X4 + 1))
        print("热度指数：", format(x * 100, '.2f'))
    def chuanbozhishu(self,X1,X2,X3,X4,X5,X6):
        xx1 = 0.10 * math.log(X1 + 1)
        xx2 = 0.76
        xx3 = 0.17 * math.log(X2 + 1) + 0.37 * math.log(X3 + 1) + 0.46 * math.log(X4 + 1)
        xx4 = 0.14
        xx5 = 0.89 * math.log(X5 + 1) + 0.11 * math.log(X6 + 1)
        x = xx1 + xx2 * xx3 + xx4 * xx5
        print("传播指数：", format(x * 100, '.2f'))


if "__name__" == "__main__":
    zhishu().chuanbozhishu()

'''
X1=新增作品数
X2=点赞数
X3=评论数
X4=分享数
X5=新增粉丝数
X6=总粉丝数
'''
