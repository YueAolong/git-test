#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
这个脚本生成一个包含学生姓名和成绩的CSV文件，每行格式为：姓名,成绩
"""

import random
import os

# 示例学生姓名列表
STUDENT_NAMES = [
    "张三", "李四", "王五", "赵六", "钱七", 
    "孙八", "周九", "吴十", "郑十一", "王十二",
    "刘一", "陈二", "杨三", "黄四", "周五",
    "吴六", "郑七", "王八", "冯九", "陈十"
]

def generate_student_grades_file(filename, count=20, min_grade=60, max_grade=100):
    """
    生成一个包含学生姓名和成绩的CSV文件
    
    参数:
        filename (str): 要创建的文件名
        count (int): 要生成的学生记录数量
        min_grade (int): 最低成绩
        max_grade (int): 最高成绩
    """
    # 确保不超过可用学生姓名数量
    count = min(count, len(STUDENT_NAMES))
    
    # 随机选择学生姓名
    selected_students = random.sample(STUDENT_NAMES, count)
    
    with open(filename, 'w', encoding='utf-8') as f:
        # 写入表头
        f.write("姓名,成绩\n")
        
        # 为每个学生生成随机成绩
        for student in selected_students:
            # 生成随机整数成绩
            grade = random.randint(min_grade, max_grade)
            # 写入文件，格式为：姓名,成绩
            f.write(f"{student},{grade}\n")
    
    print(f"已生成包含 {count} 个学生成绩的文件: {filename}")

if __name__ == "__main__":
    # 生成一个包含20个学生成绩的文件
    generate_student_grades_file("student_grades.csv", 20, 60, 100) 