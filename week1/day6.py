# def calculate(number_a, number_b):
#     return number_a + number_b

# def calculate_bmi(weight=20, height=20):
#     """计算BMI指数
#
#     args:
#         weight (float):体重（千克）
#         height (float):身高（米）
#
#     Returns:
#         float:BMI值，保留两位小数
#
#     Raises:
#         ValueError:如果身高为0或者复数
#     """
#     if height <= 0:
#         raise ValueError('身高必须为正数')
#     return round(weight / (height ** 2), 2)
#
#
# print(calculate_bmi(67, 23))

# 计算圆的面积
# radius = 5
# area = 3.14 * radius ** 2
# print('面积是：', area)
#
# item_price = 10
# quantity = 3
# total_cost = item_price * quantity
# print('总价：', total_cost)

# def check_odd_even(number):
#     """判断一个数字是奇数还是偶数
#
#     Args:
#         number (int): 需要判断的整数
#
#     Returns:
#         str: '奇数' 或 '偶数'
#     """
#     if number % 2 == 0:
#         return "偶数"
#     else:
#         return "奇数"
#
#
# print(check_odd_even(8))  # 输出：奇数
# 用户信息录入
user_name = "小明"    # 姓名
user_age = 18        # 年龄
hobbies = ["篮球", "音乐","足球"]  # 爱好列表

# 格式化输出
print(f"""
---------- 信息卡 ----------
姓名：{user_name}
年龄：{user_age}
爱好：{'、'.join(hobbies)}
----------------------------
""")