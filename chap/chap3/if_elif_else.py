# coding=utf-8
# 代码文件：ch05.py

score = int(input("请输入一个0~100的整数："))

if score >= 90:
    grade = "A"
elif score >=80:
    grade ="B"
elif score >=70:
    grade ="C"
else:
    grade = "F"

print("Grade =" +grade)