# print(10/0)

# with open('不存在的文件.txt') as f:
#     content = f.read()

# num = int('abc')

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print('除数不能为0！')
#
# try:
#     with open('a.txt') as f:
#         cotent = f.read()
# except FileNotFoundError:
#     print('文件不存在，请检查路径')
#
# try:
#     num = int(input('输入数字:'))
#     print(10 / num)
# except ValueError:
#     print('输入的不是数字')
# except ZeroDivisionError:
#     print('不能输入0！')
#
try:
    num = int(input('输入数字：'))
    print(10 / num)
except(ValueError, ZeroDivisionError) as e:
    print(f'发生错误：{e}')
#
# try:
#     num = int(input('输入数字：'))
# except ValueError:
#     print('输入无效')
# else:
#     print('输入正确，结果为：', num * 2)
# finally:
#     print('处理完成')

# age = int(input('输入年龄：'))
# if age < 0:
#     raise ValueError('年龄不能为负数')

# while True:
#     try:
#         num1 = float(input('请输入第一个数字：'))
#         num2 = float(input('请输入第二个数字：'))
#         result = num1 / num2
#     except ValueError:
#         print('错误：请输入数字！')
#     except ZeroDivisionError:
#         print('错误，除数不能为零！')
#     else:
#         print(f'结果：{result:.2f}')
#         break
#     finally:
#         print('---本次计算结束---')

while True:
    try:
        user_name = input('请输入用户名（至少三个字符）：')
        if len(user_name) < 3:
            raise ValueError('用户名至少三个字符')

        user_age = int(input('请输入年龄（年龄 >= 18）：'))
        if user_age < 18:
            raise ValueError('年龄需>=18岁')
    except ValueError as e:
        print({f'错误：{e}'})
    else:
        print('注册成功')
        break




