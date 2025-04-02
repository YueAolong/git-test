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

print("{0}:{1}sui{2}。".format(d1.name, d1.age, d1.sex))
print("{0}:{1}sui{2}。".format(d2.name, d2.age, d2.sex))
print("{0}:{1}sui{2}。".format(d3.name, d3.age,d3.sex))

class Dog:
    def __init__(self, name, age, sex = "cixing"):
        self.name = name
        self.age = age
        self.sex = sex

    def run(self):
        print("{}zaipao...".format(self.name))

    def speak(self, sound):
        print('{}zaijiao,"{}"!'.format(self.name, sound))

dog = Dog("qiuqiu",2)
dog.run()
dog.speak("wangwangwang")

class Account:
    interest_rate = 0.0568
    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount

account = Account('Toney',80000.0)

print('zhanghuming:{0}'.format(account.owner))
print('zhanghujine:{0}'.format(account.amount))
print('lilv:{0}'.format(Account.interest_rate))

class Account:
    interest_rate = 0.0667

    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount

    @classmethod
    def interest_by(cls, amt):
        return cls.interest_rate * amt

interest = Account.interest_by(12000.0)
print('jisuanlixi:{0:.4f}'.format(interest))

class Account:
    _interest_rate = 0.0667

    def __init__(self, owner, amount):
        self.owner = owner
        self._amount = amount

    def desc(self):
        print('{0}金额:{1} 利息:{2}。'.format(self.owner, self. _amount, Account._interest_rate))

    def desc(self):
        print(self._get_info())

account = Account('Tony', 80000.0)
account.desc()

print('账户名:{0}'.format(account.owner))
print('账户金额:{0}'.format(account._amount))
print('利息:{0}'.format(Account._interest_rate))

class Dog:
    def __init__(self,name, age, sex = '雌性'):
        self.name = name
        self._age = age

    def run(self):
        print('{}在跑...'.format(self.name))

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

dog = Dog('qiuqiu',2)
print('gougounianling:{}'.format(dog.get_age()))
dog.set_age(3)
print('修改后狗狗年龄:{}'.format(dog.get_age()))


class Dog:
    def __init__(self, name, age, sex = '雌性'):
        self.name = name
        self._age = age

    def run(self):
        print('{}zaipao...'.format(self.name))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

dog = Dog('qiuqiu',2)
print('gougounianling:{}'.format(dog.age))
dog.age = 3
print('xiugaihoudegougounianling:{}'.format(dog.age))


class Animal:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return('动物的名字:{0}'.format(self.name))
    def move(self):
        print('动一动。。。')

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
cat = Cat('Tom',2)
cat.move()
print(cat.show_info())



class Horse:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return('马的名字:{0}'.format(self.name))

    def run(self):
        print('马跑。。。')

class Donkey:
    def __init__(self, name):
        self.name = name
    def show_info(self):
        return('驴的名字:{0}'.format(self.name))
    def run(self):
        print('驴跑。。。')
    def roll(self):
        print('驴打滚。。。')

class Mule(Horse, Donkey):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def show_info(self):
        return('hhh:{0},{1}sui.'.format(self.name,self.age))
m = Mule('啊咧咧', 1)
m.run()
m.roll()
print(m.show_info())



class Animal:
    def speak(self):
        print('动物叫，但是不知道是哪种动物')

class Dog(Animal):
    def speak(self):
        print('小狗：汪汪叫。。。')

class Cat(Animal):
    def speak(self):
        print('xiaomao:miaomiaojiao')

class Car:
    def speak(self):
        print('xiaoqiche:didijiao')

an1 = Dog()
an2 = Cat()
an1.speak()
an2.speak()

def start(obj):
    obj.speak()

class Animal:
    def speak(self):
        print('动物叫，但是不知道是哪种动物')
class Dog(Animal):
    def speak(self):
        print('小狗：汪汪叫。。。')
class Car:
    def speak(self):
        print('xiaoqiche:didijiao')

start(Dog())
start(Car())
