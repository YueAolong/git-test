# coding=utf-8
# 代码文件： ch5/ch5_2_1_1.py

i = 0

while i * i < 1000:
    i +=1

print("i =" +str(i))
print("i * i=" +str(i * i))

i = 0

while i * i < 10:
    i += 1
    if i == 3:
        break
    print(str(i) + "*" + str(i) + "=", i * i)
else:
    print("while over!")