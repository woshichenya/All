from pack.Pc_pack.中欧.pack import *

class user_new:
    """"""
    def __init__(self,system=1,sys="test",nickename="test",name="test",sex=1):
        """
        system:调用那个系统，中欧=1，跑团=2
        :param sys: 正式系统china;;;测试系统test;;;
        :param nickename: 昵称；；；
        :param name: 真实姓名；；；
        :param sex: 性别，1=男，2=女；；；
        """
        g = PC_GO(system, sys).user_new(nickename=nickename, name=name, sex=sex)



if __name__ == "__main__":
    g=user_new(1,"test","test","test",1)

