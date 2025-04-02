# name = "小明"
# age = "18"
# height = "178"
# print(name)
# print("年龄：",age)
# a = 10
# b = 3
# print(a+b)
# print(a*b)
# print(a/b)
# print(a//b)

weight = float(input("请输入你的体重(kg)："))
height = float(input("请输入你的身高(m)："))
BMI = weight / (height**2)
print("你的BMI指数是：", BMI)
if BMI > 1:
    print("您的身体很健康！")
elif 0.5 < BMI < 1:
    print("你的身体一般，勤加锻炼哦！")
else:
    print("您非常不健康，请注意饮食")
