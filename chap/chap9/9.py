# coding=utf-8

class Car(object):
    pass

car = Car()



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
d = Dog("qiuqiu", 2)
print("我们家狗狗名叫{0}，{1}岁了。".format(d.name, d.age))

class Dog:
    def __init__(self, name, age, sex ="cixing"):
        self.name = name
        self.age = age
        self.sex = sex

d1 = Dog("qiuqiu", 2)
d2 = Dog("hh", 1, "xiongxing")
d3 = Dog(name="uob",sex="ongxing", age = 3)
print