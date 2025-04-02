# name = input("请输入你的名字:")
# print("你好，" + name + "!")
#
# age = int(input("请输入年龄："))
# print("明年你的年龄是：", age + 1)
#
# num1 = float(input("请输入第一个数字："))
# num2 = float(input("请输入第二个数字："))
# sum = num1 + num2
# print(f"这两个数字的和是：{sum}")

# input_str = input("输入两个数字（格式：3，5）：")
# num1, num2 = map(float, input_str.split(","))
# print(f"乘积是：{num1 * num2:.2f}")

# try:
#     age = int(input("请输入你的年龄："))
# except ValueError:
#     print("请输入数字！")
#     age = 0
# print("年龄：", age)

# unit = input("选择转换方向(1：厘米→英寸 2：英寸→厘米):")
# value = float(input("输入数值："))

# if unit == "1":
#     result = value / 2.54
#     print(f"{value}厘米 = {result:.2f}英寸")
# elif unit == "2":
#     result = value * 2.54
#     print(f"{value}英寸 = {result:.2f}厘米")
# else:
#     print("输入错误！")

# print("===知识问答===")
# score = 0
#
# answer = input("中国的首都是？")
# if answer.strip() == "北京":
#     score += 10
#     print("回答正确！")
# else:
#     print("回答错误！")
#
# try:
#     num = int(input("1+1=？"))
#     if num == 2:
#         score += 10
# except ValueError:
#     print("请输入数字！")
#
# print(f"你的得分：{score}")


# name = input("姓名：").strip()
# birth_year = input("出生年份：")
# user_id = name[:3] + birth_year[-2:]
# print(f"你的用户ID：{user_id.upper()}")

# while True:
#     weight = input("输入体重(kg, 必须>0):")
#     try:
#         weight = float(weight)
#         if weight > 0:
#             break
#         else:
#             print("体重不能为负数！")
#     except:
#         print("请输入数字！")
# print("录入成功：", weight)

# height = float(input("请输入你的身高（m）"))
# weight = float(input("请输入你的体重（kg）"))
# BMI = weight/height**2
# if BMI < 18.5:
#     print("偏瘦")
# elif 18.5 <= BMI < 24:
#     print("正常")
# else:
#     print("过重")

# height = input("请输入你的身高（m）")
# weight = input("请输入你的体重（kg）")
#
# try:
#     weight = float(weight)
#     height = float(height)
#     BMI = weight/height**2
# if BMI < 18.5:
#     print("偏瘦")
# elif 18.5 <= BMI < 24:
#     print("正常")
# else:
#     print("过重")

# def calculate_bmi():
#     try:
#         height = float(input("请输入您的身高（米）："))
#         weight = float(input("请输入您的体重（kg）："))
#
#         if height <= 0 or weight <= 0:
#             print("身高和体重必须是正数，请重新输入。")
#             return
#
#         bmi = weight / (height ** 2)
#         print(f"您的 BMI 值为：{bmi:.2f}")
#
#         if bmi < 18.5:
#             print("您的体重等级：偏瘦")
#         elif 18.5 <= bmi < 24:
#             print("您的体重等级：正常")
#         else:
#             print("您的体重等级：过重")
#
#     except ValueError:
#         print("输入无效，请输入正确的数字！")
#
#
# # 运行 BMI 计算器
# calculate_bmi()


input_str = input("输入单价和数量（格式：价格，数量）：")
price, quantity = map(float, input_str.split("，"))
total = price * quantity
if total > 100:
    total *= 0.9
print(f"应付金额：{total:.2f}元")
