#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
数据清洗脚本
功能：
1. 读取CSV文件
2. 删除空值
3. 删除重复数据
4. 将指定列转换为浮点数
"""

import pandas as pd
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from typing import Optional


def select_file() -> Optional[str]:
    """
    通过文件对话框选择CSV文件
    """
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="选择CSV文件",
        filetypes=[("CSV文件", "*.csv"), ("所有文件", "*.*")]
    )
    return file_path if file_path else None


def generate_sample_data(output_file: str = 'sample_data.csv') -> str:
    """
    生成示例数据并保存为CSV文件
    """
    np.random.seed(42)

    df = pd.DataFrame({
        'ID': range(1, 21),
        '姓名': [f'用户{i}' for i in range(1, 21)],
        '年龄': np.random.randint(18, 60, 20),
        '工资': np.random.randint(5000, 20000, 20),
        '评分': np.random.uniform(1, 10, 20).round(1)
    })

    # 添加一些空值
    df.at[5, '年龄'] = np.nan
    df.at[10, '工资'] = np.nan
    df.at[15, '评分'] = np.nan

    # 添加一些重复行（复制第5行到第18行）
    df.loc[18] = df.loc[4]

    # 添加一些非数字的评分
    df.at[3, '评分'] = 'N/A'
    df.at[7, '评分'] = '未知'

    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"已生成示例数据文件: {output_file}")
    return output_file


def clean_data(file_path: str, float_column: str = '评分') -> None:
    """
    清洗数据并显示结果
    """
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='gbk')

    print("\n===== 原始数据信息 =====")
    print(f"行数: {df.shape[0]}")
    print(f"列数: {df.shape[1]}")
    print("\n列名:")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i}. {col}")
    print("\n前5行数据:")
    print(df.head())
    print("\n数据类型:")
    print(df.dtypes)
    print("\n空值统计:")
    print(df.isnull().sum())
    print("\n重复行数:", df.duplicated().sum())

    # 删除空值
    df_cleaned = df.dropna()
    print("\n===== 删除空值后 =====")
    print(f"行数: {df_cleaned.shape[0]}")
    print(f"删除的行数: {df.shape[0] - df_cleaned.shape[0]}")

    # 删除重复数据
    df_cleaned = df_cleaned.drop_duplicates()
    print("\n===== 删除重复数据后 =====")
    print(f"行数: {df_cleaned.shape[0]}")
    print(f"删除的行数: {df.shape[0] - df_cleaned.shape[0]}")

    # 转换为浮点数
    if float_column in df_cleaned.columns:
        df_cleaned.loc[:, float_column] = pd.to_numeric(df_cleaned[float_column], errors='coerce')
        before_drop = df_cleaned.shape[0]
        df_cleaned = df_cleaned.dropna(subset=[float_column])
        print(f"\n===== 将 '{float_column}' 列转换为浮点数后 =====")
        print(f"行数: {df_cleaned.shape[0]}")
        print(f"删除的行数: {before_drop - df_cleaned.shape[0]}")
        print(f"\n'{float_column}' 列的数据类型: {df_cleaned[float_column].dtype}")
        print(f"\n'{float_column}' 列的基本统计:")
        print(df_cleaned[float_column].describe())

    print("\n===== 清洗后的数据 (前5行) =====")
    print(df_cleaned.head())

    output_file = os.path.splitext(file_path)[0] + '_cleaned.csv'
    df_cleaned.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"\n清洗后的数据已保存为: {output_file}")


def main():
    print("===== 数据清洗程序 =====")
    choice = input("是否生成示例数据? (y/n): ").lower()

    if choice == 'y':
        file_path = generate_sample_data()
    else:
        file_path = select_file()
        if not file_path:
            print("未选择文件，程序退出")
            return
        if not os.path.exists(file_path):
            messagebox.showerror("错误", f"文件 '{file_path}' 不存在")
            print(f"错误: 文件 '{file_path}' 不存在")
            return

    float_column = input("请输入需要转换为浮点数的列名 (默认为'评分'): ").strip()
    if not float_column:
        float_column = '评分'

    clean_data(file_path, float_column)


if __name__ == "__main__":
    main()
