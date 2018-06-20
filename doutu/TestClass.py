class Programmer():

    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('Age must be int')

    def __eq__(self, other):
        if isinstance(other, Programmer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('The instance is not Programmer')

    def __add__(self, other):
        if isinstance(other, Programmer):
            return self.age + other.age
        else:
            raise Exception('The instance is not pro')

    def __dir__(self):
        return self.__dict__.keys()

    def __str__(self):
        return 'My name is %s, my age is %s' %(self.name, self.age)

    def __setattr__(self, key, value):
        self.__dict__[key] = value



if __name__ == '__main__':
    pro1 = Programmer('XiaoMing', 20)
    pro2 = Programmer('JiaJun', 30)
    print(pro1 == pro2)
    print(pro1 + pro2)
    print(dir(pro2))
    print(pro2)

