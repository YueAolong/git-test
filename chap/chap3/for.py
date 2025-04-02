# coding=utf-8
# 代码文件： ch05/ch5_2_2_1.py

print("---字符串----")
for item in "Hello":
    print(item)

# 声明整数列表
numbers = [43,32,55,74]
print("---整数列表---")
for item in numbers:
    print(item)

for item in range(10):
    if item == 3:
        break
    print(item)
else:
    print("For over!")


for item in range(10):
    if item == 3:
        continue
    print(item)
else:
    print("For over!")