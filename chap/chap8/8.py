# coding=utf-8
# 代码文件：ch08.py

def rect_area(width, height):
    area = width * height
    return area
r_area = rect_area(320, 480)
print("{0} * {1} 长方形的面积：{2:.2f}".format(320, 480, r_area))

def make_coffee(name= "卡布奇诺"):
    return "制备一杯{0}咖啡。".format(name)
coffee1 = make_coffee("拿铁")
coffee2 = make_coffee()
print(coffee1)
print(coffee2)

def sum(*numbers):
    total = 0.0
    for number in numbers:
        total +=number
    return total
print(sum(100.0, 20.0, 30.0))

def show_info(**info):
    print("---show_info---")
    for key, value in info.items():
        print("{0} - {1}".format(key, value))
print(show_info(name="tony", age=18, sex=True))


x = 20

def print_value():
    global x
    x = 10
    print("函数中x = {0}".format(x))

print_value()
print("全局变量x = {0}".format(x))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def calc(opr):
    if opr == "+":
        return add
    else:
        return sub
f1 = calc("+")
f2 = calc("-")
print("10 + 5 = {0}".format(f1(10, 5)))
print("10 - 5 = {0}".format(f2(10, 5)))

def f1(x):
    return x > 50
data1 = [66, 15, 91, 28, 50]
filtered = filter(f1, data1)
data2 = list(filtered)
print(data2)

data1 = [66, 15, 91, 28, 98, 50, 7, 80, 00]

filtered = filter(lambda x: (x > 50),data1)
data2 = list(filtered)
print(data2)

mapped = map(lambda x: (x*2), data1)
data3 = list(mapped)
print(data3)



