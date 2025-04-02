# # coding=utf-8
#
# i = input('请输入数字：')
#
# n = 8888
#
# try:
#     result = n / int(i)
#     print(result)
#     print('{0}除以{1}等于{2}'.format(n, i, result))
# except ZeroDivisionError as e:
#     print('不能除以0，异常：{}'.format(e))
# except ValueError as e:
#     print('输入的是无效数字，异常：{}'.format(e))
#
#
# i = input('请输入数字：')
#
# n = 8888
#
# try:
#     result = n / int(i)
#     print(result)
#     print('{0}除以{1}等于{2}'.format(n, i, result))
# except (ZeroDivisionError,ValueError) as e:
#     print('不能除以0，异常：{}'.format(e))
# finally:
#     print('资源释放...')



class ZhijieketangException(Exception):
    def __init__(self, message):
        super().__init__(message)
i = input('请输入数字')
n = 8888
try:
    result = n / int(i)
    print(result)
    print('{0}除以{1}等于{2}'.format(n, i, result))
except ZeroDivisionError as e:
    raise ZhijieketangException('不能除以0')
except ValueError as e:
    raise ZhijieketangException('输入的是无效数字')





# i = input('请输入数字：')
# n = 8888
#
# try:
#     i2 = int(i)
#     try:
#         result = n / i2
#         print('{0}除以{1}等于{2}'.format(n, i2, result))
#     except ZeroDivisionError as e1:
#         print('不能除以0，异常:{}'.format(e1))
# except ValueError as e2:
#     print('输入的是无效数字，异常：{}'.format(e2))
