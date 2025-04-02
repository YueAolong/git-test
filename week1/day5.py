# age = 25
# salary = 45000
# credit_score = 700
#
# if (age >= 18) and (salary > 40000 or credit_score >= 650):
#     print("符合贷款资格")
# else:
#     print("不符合条件")
#
#
# is_running = True
# while is_running:
#     command = input("输入命令（stop退出）:")
#     if command == "stop":
#         is_running = False
#     else:
#         print("执行命令:", command)
#

# age = 25
# salary = 45000
# credit_score = 7000
#
# if (age >= 18) and (salary > 40000 or credit_score >= 6500):
#     print("符合贷款资格")
# else:
#     print("不符合条件")
#
# is_running = True
# while is_running:
#     command = input("输入命令（stop退出）:")
#     if command == "stop":
#         is_running = False
#     else:
#         print("执行命令：", command)
#
# temperature = float(input("当前湿度："))
# humidity = float(input("当前湿度："))
#
# if temperature > 30 and humidity > 80:
#     print("高温高湿，建议打开空调除湿模式")
# elif temperature < 10 or humidity < 30:
#     print("低温低湿，建议开启加湿器")
# else:
#     print("环境舒适")
#
#
# correct_username = "admin"
# correct_password = "P@sswOrd"
#
# input_user = input("用户名：")
# input_pass = input("密码：")
#
# is_user_correct = (input_user == correct_username)
# is_pass_correct = (input_pass == correct_password)
#
# if is_user_correct and is_pass_correct
#     print("登陆成功！")
# elif not is_user_correct and is_pass_correct:
#     print("用户名和密码均错误！")
# elif not is_user_correct:
#     print("用户名不存在")
# else:
#     print("密码错误")

# has_sword = True
# has_potion = False
# health = 35
# can_fight = has_sword and (health > 20)
# can_escape = (not has_sword) or (health <= 20)
# print("可以战斗" if can_fight else "建议逃跑")

# weight = float(input("包裹重量（kg）："))
# distance = int(input("运输距离（km）："))
# is_fragile = input("是否易碎品（y/n）：").lower() == "y"
#
# base_fee = 10
# distance_fee = distance * 0.5
# fragile_fee = 15 if is_fragile else 0
# overweight_fee = (weight-1) * 2 if weight > 1 else 0
# total =base_fee + distance_fee + fragile_fee +overweight_fee
# print(f"总运费：{total:.2f}元")

# user_input = input("您的问题：").lower()
# if "退款" in user_input and "没到账" in user_input:
#     print("正在加急处理你的退款请求")
# elif "发货" in user_input or "物流" in user_input:
#     print("请提供订单号查询物流信息")
# elif any(word in user_input for word in ["密码","登录"]):
#     print("请尝试种植密码或联系客服")
# else:
#     print("正在转接人工客服...")

x, y = 2, 3
direction = input('移动方向（w上/a左/s下/d右）：')

can_move = (
    (direction == 'w' and y < 5) or
    (direction == 's' and y > 0) or
    (direction == 'a' and x > 0) or
    (direction == 'd' and x < 5)
)

if can_move:
    print('移动成功！')
else:
    print('撞墙了！')