import math
'''
热度指数 
原公式：
传播指数：
DCI={0.10*ln(X1+1)+0.76*[0.17*ln(X2+1)+0.37*ln(X3+1)+0.46*ln(X4+1)]+0.14*[0.89*ln(X5+1)+0.11*ln(X6+1)]}*100
热度指数：
Dhot={0.17*ln(X2+1)+0.37*ln(X3+1)+0.46*ln(X4+1)}*100
成长指数：
DGI={}[0.89*ln(X5+1)+0.11*ln(X6+1)]}*100
'''

'''
热度指数：
'''
x2=14
x3=5
x4=1
x=0.17*float(math.log(x2+1))+0.37*float(math.log(x3+1))+0.46*float(math.log(x4+1))
print("热度指数：",format(x*100,'.2f'))

'''
传播指数：
'''
X1=0
X2=14
X3=5
X4=1
X5=0
X6=0

xx1=0.10*math.log(X1+1)
xx2=0.76
xx3=0.17*math.log(X2+1)+0.37*math.log(X3+1)+0.46*math.log(X4+1)
xx4=0.14
xx5=0.89*math.log(X5+1)+0.11*math.log(X6+1)
# print(xx1,xx2,xx3,xx4,xx5)
x=xx1+xx2*xx3+xx4*xx5
print("传播指数：",format(x*100,'.2f'))

# print(Dhot)
'''
X1=新增作品数
X2=点赞数
X3=评论数
X4=分享数
X5=新增粉丝数
X6=总粉丝数
'''