# def greet(name, message='你好'):
#     print(f'{message},{name}!')
#
#
# greet('小明')
# greet('小红', '早上好')
# greet(message='欢迎', name='老师')

# def sum_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
#
# print(sum_numbers(1, 2, 3))
#
#
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
#
# print_info(name='小明', age=18)
#
#
# def celsius_to_fahrenheit(c):
#     """摄氏度转换华氏度"""
#     return c * 9/5 + 32
#
#
# def fahrenheit_to_celsius(f):
#     """华氏度转换摄氏度"""
#     return (f - 32) * 5/9
#
#
# print(f'35 °C ={celsius_to_fahrenheit(35):.1f}°F')
# print(f'95 °F ={fahrenheit_to_celsius(95):.1f}°C')

from file_utils import read_file

content = read_file('data.txt')
print('文件内容：', content)
