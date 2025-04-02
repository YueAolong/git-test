# # class BankAccount:
# #     interest_rate = 0.03
# #
# #     def __init__(self, owner, balance=0):
# #         self.owner = owner
# #         self.balance = balance
# #
# #     def add_interest(self):
# #         self.balance *= (1 + BankAccount.interest_rate)
# #
# #
# # account1 = BankAccount("小明", 1000)
# # account2 = BankAccount('小红')
# #
# #
# # BankAccount.interest_rate = 0.05
# # account1.add_interest()
# # print(account1.balance)
#
# #
# # class StringUtils:
# #     @staticmethod
# #     def is_palindrome(s):
# #         s = s.lower().replace(" ", "")
# #         return s == s[::-1]
# #
# #     @classmethod
# #     def from_file(cls, filename):
# #         with open(filename) as f:
# #             data = f.read()
# #             return cls(data)
# #
# # print(StringUtils.is_palindrome("A man a plan acanal Panama"))
# #
# # utils = StringUtils.from_file("text.txt")
#
# class StringUtils:
#     def __init__(self, text):
#         self.text = text
#
#     @staticmethod
#     def is_palindrome(s):
#         """判断是否是回文字符串"""
#         s = s.lower().replace(" ", "")
#         return s == s[::-1]
#
#     @classmethod
#     def from_file(cls, filename):
#         """从文件创建工具实例"""
#         with open(filename, 'r', encoding='utf-8') as f:
#             data = f.read()
#         return cls(data)
#
#
# # 使用静态方法
#
#
# print(StringUtils.is_palindrome("A man a plan a canal Panama"))  # True
#
# # 使用类方法
# utils = StringUtils.from_file("text.txt")
# print(utils.text)

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print(f'{self.name}:汪汪！')
#
#
# my_dog = Dog('小黑', 3)
# your_dog = Dog('小白', 2)
#
# print(my_dog.name)
# my_dog.bark()
# your_dog.bark()
# 父类（基类）
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f"{self.name}在吃东西")
#
# # 子类（继承Animal）
# class Cat(Animal):  # 括号里写父类名
#     def meow(self):  # 子类特有方法
#         print("喵喵~")
#
# # 使用
# my_cat = Cat("橘猫")
# my_cat.eat()  # 调用父类方法 → 橘猫在吃东西
# my_cat.meow() # 调用子类方法 → 喵喵~
# print(my_cat.name)

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, money):
        if money > 0:
            self.__balance += money

    def get_balance(self):
        return self.__balance


account = BankAccount(100)
account.deposit(50)
print(account.get_balance())


class Dog:
    def speak(self):
        print('汪汪')
class Cat:
    def speak(self):
        print('喵喵')
def animal_talk(animal):
    animal.speak()


animal_talk(Dog())
animal_talk(Cat())


class Student:
    def __init__(self, name, student_id, score):
        """初始化学生对象"""
        self.name = name  # 学生姓名
        self.student_id = student_id  # 学号
        self.score = score  # 分数

    def update_score(self, new_score):
        """更新学生的分数"""
        if 0 <= new_score <= 100:
            self.score = new_score
            print(f"{self.name} 的新分数更新为: {self.score}")
        else:
            print("错误：分数必须在 0 到 100 之间！")

# 创建 3 个学生对象并测试
stu1 = Student("小明", "2024001", 90)
stu2 = Student("小红", "2024002", 85)
stu3 = Student("小刚", "2024003", 78)

# 更新分数
stu1.update_score(95)
stu2.update_score(88)
stu3.update_score(102)  # 这里会触发错误提示
