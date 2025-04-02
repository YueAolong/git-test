# name = "Alice"
# greeting = "你好" + name + "!"
# print(greeting)
#
# age = 20
# print(f"我今年{age}岁")
#
# text = "Hello python"
# print(text[0])
# print(text[6:12])
#
# text = input("请输入一段话：")
# print("总字数：",len(text))
# print("前五个字：",text[:5])

# text =" Hello,  Python "
# print(text.strip())
# print(text.lstrip())
# print(text.replace("Python", "World"))

# fruits = "apple,banana,orange"
# list_fruits = fruits.split(",")
# print(list_fruits)
# new_str = "-".join(list_fruits)
# print(new_str)
# print(text.find("Python"))
# print(text.count("l"))

# poem = """静夜思
# 床前明月光
# 疑是地上霜"""
# print(poem)
# print("这是第一行\n这是第二行")
# print("路径：D：Documents\\test")

# password = input("输入密码：")
# strength = 0
# if len(password) >= 8:
#     strength += 1
# if any(c.isupper() for c in password):
#     strength +=1
# if any(c in "!@#$%^&*" for c in password):
#     strength += 1
# print(f"密码强度：{"★" * strength}")
#
# dirty_text = '  [重要]2024年报告（最终版）_v2.5.text'
# clean_text = dirty_text.strip(' [  ]')
# clean_text = clean_text.replace('_','-')
# print(clean_text)
#
# import random
#
# first_names = ['张', '玉', '李', '赵']
# last_names = ['伟', '芳', '强', '娜']
# number = random.randint(1000, 9999)
#
# username = random.choice(first_names) + random.choice(last_names) + str(number)
# print(f'推荐用户名：{username}')
#

# items = [
#     {'name': '笔记本', 'price': 15.5, 'quantity': 3},
#     {'name': '钢笔', 'price': 8.0, 'quantity': 2}
# ]
#
# total = 0
# print('{:<10}{:<10}{:<10}{:<10}'.format('商品', '单价', '数量', '小计'))
# for item in items:
#     subtotal = item['price'] * item['quantity']
#     total += subtotal
#     print(f'{item['name']:<12}{item['price']:<10.1f}{item['quantity']:<10}{subtotal:<10.1f}')
# print(f'\n总金额：{total:.2f}元')

# idiom = input('输入成语：')
# last_char = idiom[-1]
# print(f'下一个成语需以【{last_char}】开头！')

# sensitive_words = ['暴力', '色情']
# text = input('输入评论：')
# for word in sensitive_words:
#     text = text.replace(word, '☆☆☆')
# print('过滤后内容：',text)

# -*- coding: utf-8 -*-
# 成语接龙游戏（基础版）

import re

# 提取所有数字
text = "订单号：ABC123，金额：456.78元"
numbers = re.findall(r"\d+\.?\d*", text)  # 匹配整数或小数 → ['123', '456.78']
print(numbers)