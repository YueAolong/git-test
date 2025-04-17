#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
这个脚本读取包含学生姓名和成绩的CSV文件，计算成绩的统计信息并显示结果。
"""

import os
import sys
import csv
from statistics import mean, median, stdev

def analyze_student_grades(filename):
    """
    读取学生成绩文件，计算统计信息
    
    参数:
        filename (str): 包含学生成绩的CSV文件名
        
    返回:
        dict: 包含统计信息的字典
    """
    if not os.path.exists(filename):
        print(f"错误: 文件 '{filename}' 不存在!")
        return None
    
    students = []
    grades = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # 使用CSV模块读取文件
            reader = csv.DictReader(f)
            
            for row in reader:
                name = row['姓名']
                grade = int(row['成绩'])
                
                students.append(name)
                grades.append(grade)
        
        if not grades:
            print("错误: 文件中没有有效的成绩数据!")
            return None
        
        # 计算统计信息
        stats = {
            'students': students,
            'grades': grades,
            'count': len(grades),
            'total': sum(grades),
            'average': mean(grades),
            'median': median(grades),
            'min': min(grades),
            'max': max(grades)
        }
        
        # 如果有足够的数据，计算标准差
        if len(grades) > 1:
            stats['stdev'] = stdev(grades)
        else:
            stats['stdev'] = 0
        
        return stats
    
    except ValueError as e:
        print(f"错误: 文件包含无效的成绩数据: {e}")
        return None
    except Exception as e:
        print(f"错误: 读取文件时发生错误: {e}")
        return None

def display_results(filename):
    """
    显示分析结果
    
    参数:
        filename (str): 包含学生成绩的CSV文件名
    """
    stats = analyze_student_grades(filename)
    
    if stats is None:
        return
    
    print(f"\n文件 '{filename}' 的分析结果:")
    print(f"学生人数: {stats['count']}")
    print(f"成绩总和: {stats['total']}")
    print(f"平均成绩: {stats['average']:.2f}")
    print(f"中位成绩: {stats['median']:.2f}")
    print(f"最低成绩: {stats['min']}")
    print(f"最高成绩: {stats['max']}")
    print(f"成绩标准差: {stats['stdev']:.2f}")
    
    print("\n学生成绩详情:")
    print("姓名\t成绩")
    print("-" * 20)
    
    for i in range(len(stats['students'])):
        print(f"{stats['students'][i]}\t{stats['grades'][i]}")
    
    # 按成绩排序
    sorted_data = sorted(zip(stats['students'], stats['grades']), key=lambda x: x[1], reverse=True)
    
    print("\n按成绩排序:")
    print("姓名\t成绩")
    print("-" * 20)
    
    for name, grade in sorted_data:
        print(f"{name}\t{grade}")

if __name__ == "__main__":
    # 默认文件名
    filename = "student_grades.csv"
    
    # 如果提供了命令行参数，使用它作为文件名
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    
    display_results(filename) 