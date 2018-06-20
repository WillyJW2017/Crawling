class Programmer(object):

    # def __new__(cls, *args, **kwargs):
    #     print('call __new__ method')
    #     print(args)
    #     return super(Programmer, cls).__new__(cls, *args, **kwargs)

    hobby = 'Coding with Python'
    def __init__(self, name, age, weight):
        print('call __init__ method')
        self.name = name    # 公有变量
        self._age = age     # 私有变量
        self.__weight = weight # 外部访问时不能直接访问，使用 pro._Programmer__weight 访问

    def get_weight(self):
        return self.__weight

    # 类方法，调用时直接使用类名 Programmer.get_hobby()
    @classmethod
    def get_hobby(cls):
        return cls.hobby
    # 类属性，调用时使用实例名，方法不用加(): pro.get_name
    @property
    def get_name(self):
        return self.name + 'Guys!!!'

    def self_introduce(self):
        print('My Name is %s, my age is %s' %(self.name, self._age) )


class BackEndProgrammer(Programmer):
    def __init__(self, name, age, weight, language):
        super(BackEndProgrammer, self).__init__(name, age, weight)
        self.language = language

    def self_introduce(self):
        print('My Name is %s, my language is %s' %(self.name, self.language))


def introduce(programmer):
    if isinstance(programmer, Programmer):
        programmer.self_introduce()

if __name__ == '__main__':
    pro1 = Programmer('Tom', '30', '120')
    pro = BackEndProgrammer('sky', '20','60', 'Python')
    # print(pro.__dict__)
    # print(pro.get_weight())
    # print(pro._Programmer__weight)
    # print(Programmer.get_hobby())   #
    # print(pro.get_name)
    # print(pro.__dict__)
    # introduce(pro1)
    # introduce(pro)
