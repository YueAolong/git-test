# coding=utf-8
# 代码文件：ch05/ch5_4.py

i = 100; r = 0;  s = 0; t = 0

while i < 1000:
    r = i // 100
    s = (i - r * 100) // 10
    t = i - r * 100 - s * 10
    if i - r ** 3 - s ** 3 - t ** 3 ==0:
        print("i = " + str(i))
    i += 1