# from file_utils import read_file
#
# content = read_file('data.txt')
# print('文件内容：', content)
# main.py

from file_utils import read_file, write_file

# 写入内容到 data.txt
write_file("data.txt", "Hello, this is a test file!")

# 读取文件内容
content = read_file("data.txt")
print("文件内容：", content)
