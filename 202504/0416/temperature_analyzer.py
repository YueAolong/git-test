#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
温度数据分析工具
功能：
1. 通过弹窗选择两个Excel文件
2. 按日期合并数据
3. 计算每行的平均温度
4. 筛选出平均温度超过35度的数据
5. 保存为新Excel文件
"""

import pandas as pd
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from typing import Optional, List, Dict, Any, Tuple


def select_files() -> Tuple[Optional[str], Optional[str]]:
    """
    通过文件对话框选择两个Excel文件
    
    返回:
        Tuple[Optional[str], Optional[str]]: 两个选择的文件路径，如果用户取消则返回None
    """
    # 创建Tkinter根窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 选择第一个文件
    file1_path = filedialog.askopenfilename(
        title="选择第一个Excel文件",
        filetypes=[("Excel文件", "*.xlsx *.xls"), ("所有文件", "*.*")]
    )
    
    if not file1_path:
        return None, None
    
    # 选择第二个文件
    file2_path = filedialog.askopenfilename(
        title="选择第二个Excel文件",
        filetypes=[("Excel文件", "*.xlsx *.xls"), ("所有文件", "*.*")]
    )
    
    return file1_path, file2_path


def select_save_file() -> Optional[str]:
    """
    通过文件对话框选择保存位置
    
    返回:
        Optional[str]: 选择的保存路径，如果用户取消则返回None
    """
    # 创建Tkinter根窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 打开文件保存对话框
    file_path = filedialog.asksaveasfilename(
        title="选择保存位置",
        defaultextension=".xlsx",
        filetypes=[("Excel文件", "*.xlsx"), ("所有文件", "*.*")]
    )
    
    return file_path if file_path else None


def read_excel_file(file_path: str, file_name: str) -> pd.DataFrame:
    """
    读取Excel文件
    
    参数:
        file_path (str): Excel文件路径
        file_name (str): 文件名称（用于显示）
        
    返回:
        pd.DataFrame: 读取的数据
    """
    try:
        # 尝试读取Excel文件
        df = pd.read_excel(file_path)
        
        # 显示数据信息
        print(f"\n===== {file_name} 数据信息 =====")
        print(f"行数: {df.shape[0]}")
        print(f"列数: {df.shape[1]}")
        print(f"列名: {', '.join(df.columns)}")
        
        # 检查是否有日期列
        date_columns = [col for col in df.columns if '日期' in col or 'date' in col.lower()]
        if not date_columns:
            print(f"警告: {file_name} 中没有找到日期列")
        else:
            print(f"日期列: {', '.join(date_columns)}")
        
        # 检查是否有温度列
        temp_columns = [col for col in df.columns if '温度' in col or 'temp' in col.lower()]
        if not temp_columns:
            print(f"警告: {file_name} 中没有找到温度列")
        else:
            print(f"温度列: {', '.join(temp_columns)}")
        
        return df
    
    except Exception as e:
        print(f"读取 {file_name} 时出错: {str(e)}")
        raise


def merge_by_date(df1: pd.DataFrame, df2: pd.DataFrame, 
                 date_col1: str, date_col2: str) -> pd.DataFrame:
    """
    按日期合并两个DataFrame
    
    参数:
        df1 (pd.DataFrame): 第一个DataFrame
        df2 (pd.DataFrame): 第二个DataFrame
        date_col1 (str): 第一个DataFrame的日期列名
        date_col2 (str): 第二个DataFrame的日期列名
        
    返回:
        pd.DataFrame: 合并后的DataFrame
    """
    # 确保日期列是日期类型
    df1[date_col1] = pd.to_datetime(df1[date_col1])
    df2[date_col2] = pd.to_datetime(df2[date_col2])
    
    # 重命名日期列，以便合并
    df1 = df1.rename(columns={date_col1: '日期'})
    df2 = df2.rename(columns={date_col2: '日期'})
    
    # 按日期合并
    merged_df = pd.merge(df1, df2, on='日期', how='inner')
    
    print(f"\n合并后的数据行数: {merged_df.shape[0]}")
    
    return merged_df


def find_date_and_temp_columns(df: pd.DataFrame) -> Tuple[str, List[str]]:
    """
    查找日期列和温度列
    
    参数:
        df (pd.DataFrame): DataFrame
        
    返回:
        Tuple[str, List[str]]: 日期列名和温度列名列表
    """
    # 查找日期列
    date_columns = [col for col in df.columns if '日期' in col or 'date' in col.lower()]
    date_col = date_columns[0] if date_columns else None
    
    # 查找温度列
    temp_columns = [col for col in df.columns if '温度' in col or 'temp' in col.lower()]
    
    return date_col, temp_columns


def calculate_average_temperature(df: pd.DataFrame, temp_columns: List[str]) -> pd.DataFrame:
    """
    计算每行的平均温度
    
    参数:
        df (pd.DataFrame): 合并后的DataFrame
        temp_columns (List[str]): 温度列名列表
        
    返回:
        pd.DataFrame: 添加了平均温度的DataFrame
    """
    # 计算平均温度
    df['平均温度'] = df[temp_columns].mean(axis=1)
    
    print(f"\n平均温度统计:")
    print(f"  最小值: {df['平均温度'].min():.1f}°C")
    print(f"  最大值: {df['平均温度'].max():.1f}°C")
    print(f"  平均值: {df['平均温度'].mean():.1f}°C")
    
    return df


def filter_high_temperature(df: pd.DataFrame, threshold: float = 15.0) -> pd.DataFrame:
    """
    筛选出平均温度超过阈值的数据
    
    参数:
        df (pd.DataFrame): 包含平均温度的DataFrame
        threshold (float): 温度阈值，默认为15.0
        
    返回:
        pd.DataFrame: 筛选后的DataFrame
    """
    # 筛选高温数据
    high_temp_df = df[df['平均温度'] > threshold].copy()
    
    # 按平均温度降序排序
    high_temp_df = high_temp_df.sort_values(by='平均温度', ascending=False)
    
    print(f"\n筛选出平均温度超过 {threshold}°C 的数据:")
    print(f"  行数: {high_temp_df.shape[0]}")
    if high_temp_df.shape[0] > 0:
        print(f"  最高温度: {high_temp_df['平均温度'].max():.1f}°C")
        print(f"  最低温度: {high_temp_df['平均温度'].min():.1f}°C")
    
    return high_temp_df


def save_filtered_data(df: pd.DataFrame, save_path: str) -> None:
    """
    保存筛选后的数据
    
    参数:
        df (pd.DataFrame): 筛选后的DataFrame
        save_path (str): 保存路径
    """
    # 保存为Excel文件
    df.to_excel(save_path, index=False)
    print(f"\n筛选后的数据已保存至: {save_path}")


def main():
    """主函数"""
    print("===== 温度数据分析工具 =====")
    
    # 选择两个Excel文件
    file1_path, file2_path = select_files()
    if not file1_path or not file2_path:
        print("未选择文件，程序退出")
        return
    
    # 检查文件是否存在
    if not os.path.exists(file1_path):
        messagebox.showerror("错误", f"文件 '{file1_path}' 不存在")
        print(f"错误: 文件 '{file1_path}' 不存在")
        return
    
    if not os.path.exists(file2_path):
        messagebox.showerror("错误", f"文件 '{file2_path}' 不存在")
        print(f"错误: 文件 '{file2_path}' 不存在")
        return
    
    try:
        # 读取两个Excel文件
        df1 = read_excel_file(file1_path, "第一个文件")
        df2 = read_excel_file(file2_path, "第二个文件")
        
        # 查找日期列和温度列
        date_col1, temp_cols1 = find_date_and_temp_columns(df1)
        date_col2, temp_cols2 = find_date_and_temp_columns(df2)
        
        if not date_col1 or not date_col2:
            messagebox.showerror("错误", "无法找到日期列")
            print("错误: 无法找到日期列")
            return
        
        if not temp_cols1 or not temp_cols2:
            messagebox.showerror("错误", "无法找到温度列")
            print("错误: 无法找到温度列")
            return
        
        # 按日期合并
        merged_df = merge_by_date(df1, df2, date_col1, date_col2)
        
        # 合并温度列
        all_temp_cols = temp_cols1 + temp_cols2
        
        # 计算平均温度
        merged_df = calculate_average_temperature(merged_df, all_temp_cols)
        
        # 筛选高温数据
        high_temp_df = filter_high_temperature(merged_df)
        
        # 选择保存位置
        save_path = select_save_file()
        if not save_path:
            print("未选择保存位置，程序退出")
            return
        
        # 保存筛选后的数据
        save_filtered_data(high_temp_df, save_path)
        
        print("\n处理完成!")
        
    except Exception as e:
        messagebox.showerror("错误", f"处理过程中出现错误: {str(e)}")
        print(f"错误: {str(e)}")


if __name__ == "__main__":
    main() 