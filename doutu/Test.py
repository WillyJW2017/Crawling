class Pro():
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight


if __name__ == '__main__':
    pro = Pro('sky', '20','60')
    print(pro.get_weight())
    print(pro.__dict__)
    print(pro.__dir__())
    print(pro._Pro__weight)